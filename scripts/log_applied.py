#!/usr/bin/env python3
"""Log an application into the jobsearch pipeline.

Called as a jobradar hook when a posting is marked `applied` in the TUI (or via
`jobradar mark <uid> applied`). Reads the posting as JSON on stdin, then:

  * finds an existing issue for the same posting (jobradar uid marker, posting URL,
    or company + role title) and updates it, or
  * writes docs/opportunities/<company>-<role>.md and creates the issue from
    .github/ISSUE_TEMPLATE/opportunity.md, labelled and on the board at Contacted.

Everything the tool cannot know (hard-filter verdict, tier, JD analysis,
application answers) is left explicitly unreviewed rather than guessed silently.

Usage:  log_applied.py [--dry-run] [--evidence pre-project] [--tier a|b|c] [--market ch|de|eu-remote|fr-bridge]
        echo '{"company": "...", ...}' | log_applied.py
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from os.path import commonprefix
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PROJECT_ID = "PVT_kwHOAGop3M4Bi8S3"
STAGE_FIELD = "PVTSSF_lAHOAGop3M4Bi8S3zhhygD8"
STAGE_CONTACTED = "832d8f86"

MARKET_LABELS = {
    "de": "market:de",
    "ch": "market:ch",
    "fr": "market:fr-bridge",
    "eu-remote": "market:eu-remote",
    "au": "market:eu-remote",  # remote-first employer; the AU dimension goes in the body
}
TITLE_PREFIX = {"de": "DE", "ch": "CH", "fr": "FR", "eu-remote": "EU-REMOTE", "au": "EU-REMOTE", "other": "??"}
TIER_SIGNALS = ("ml-platform", "mlops", "ml-infra", "ai-platform", "ai-infra", "serving")
AI_SIGNALS = TIER_SIGNALS + ("ai-ml",)
WEB3_SIGNALS = ("web3", "blockchain", "crypto", "protocol", "staking", "web3-tech", "web3-infra")
MARKET_OVERRIDES = {"ch": "market:ch", "de": "market:de", "eu-remote": "market:eu-remote", "fr-bridge": "market:fr-bridge"}
MARKET_NAMES = {
    "market:ch": "CH",
    "market:de": "DE",
    "market:eu-remote": "EU-remote",
    "market:fr-bridge": "FR-bridge",
}


def market_name(label: str | None) -> str:
    """Human-facing market name; the label itself only ever goes on the issue."""
    return MARKET_NAMES.get(label or "", "UNREVIEWED")
RULES = "uid `{}` · score {} · lane `{}`"


# ---------------------------------------------------------------- helpers


def gh(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(["gh", *args], cwd=str(REPO), capture_output=True, text=True, check=check)


def gh_json(args: list[str]):
    result = gh(args)
    return json.loads(result.stdout or "[]")


def slugify(value: str, limit: int = 60) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-")
    return slug[:limit].strip("-")


def normalise(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (value or "").lower()).strip()


def add_business_days(start: date, count: int) -> date:
    """Weekends only — public holidays are not modelled."""
    current, remaining = start, count
    while remaining > 0:
        current += timedelta(days=1)
        if current.weekday() < 5:
            remaining -= 1
    return current


def say(message: str) -> None:
    print(message, flush=True)


# ---------------------------------------------------------------- decisions


def decide_tier(job: dict, override: str | None) -> tuple[str, str]:
    if override:
        return override, "set explicitly"
    reasons = [r.lstrip("+-") for r in (job.get("reasons") or [])]
    if any(signal in reasons for signal in TIER_SIGNALS):
        return "b", f"heuristic from jobradar signals ({', '.join(reasons)})"
    return "c", f"no ML-platform signal in jobradar reasons ({', '.join(reasons) or 'none'})"


def decide_track(job: dict, override: str | None = None) -> tuple[str, str]:
    """Funnel dimension: AI/ML-platform, Web3 infrastructure, or non-AI bridge.

    Both tracks are in scope; AI/ML is the preferred direction, so it wins when a
    posting carries signals for both.
    """
    if override:
        return override, "set explicitly"
    reasons = [r.lstrip("+-") for r in (job.get("reasons") or [])]
    ai = [r for r in reasons if r in AI_SIGNALS]
    web3 = [r for r in reasons if r in WEB3_SIGNALS]
    if ai:
        return "track:ai", f"AI/ML signals ({', '.join(ai)})"
    if web3:
        return "track:web3", f"Web3 signals ({', '.join(web3)})"
    return "track:bridge", "no AI/ML or Web3 signal in jobradar reasons"


def decide_market(lane: str, override: str | None) -> tuple[str | None, str]:
    if override:
        return MARKET_OVERRIDES.get(override), "set explicitly"
    lane = (lane or "").lower()
    if lane in MARKET_LABELS:
        return MARKET_LABELS[lane], f"lane {lane}"
    return None, f"lane {lane!r} maps to no market label — assign one manually"


def find_issue(job: dict) -> tuple[dict | None, str]:
    issues = gh_json(["issue", "list", "--state", "all", "--limit", "300", "--json", "number,title,url,body"])
    marker = f"jobradar-uid: {job['uid']}"
    for issue in issues:
        if marker in (issue.get("body") or ""):
            return issue, "uid marker"
    url = (job.get("url") or "").rstrip("/")
    if url:
        for issue in issues:
            if url in (issue.get("body") or ""):
                return issue, "posting URL"
    company, title = normalise(job.get("company", "")), normalise(job.get("title", ""))
    if company and title:
        for issue in issues:
            issue_title = normalise(issue.get("title", ""))
            if company in issue_title and title in issue_title:
                return issue, "company + role"
    return None, ""


def find_doc(job: dict) -> Path | None:
    """Reuse an existing opportunity doc only when both employer and role match.

    Matching on the employer alone reuses the wrong doc when one company has several
    open roles (it happened with Nebius).
    """
    docs = REPO / "docs" / "opportunities"
    if not docs.is_dir():
        return None
    role_slug = slugify(job.get("title", ""))
    company_token = (slugify(job.get("company", "")).split("-") or [""])[0]
    if not role_slug or not company_token:
        return None
    for candidate in sorted(docs.glob("*.md")):
        stem = candidate.stem
        if company_token not in stem:
            continue
        tail = stem.split(company_token, 1)[1].lstrip("-")
        role_prefix = commonprefix([role_slug, tail])
        # JDs decorate titles ("(d/f/m)", "(m/w/d)"), so the doc slug is usually a
        # prefix of the role slug rather than an exact match.
        if len(role_prefix) >= min(20, len(role_slug), len(tail)):
            return candidate
    return None


def item_stage(item_id: str) -> str | None:
    """Read the Stage back off a board item. Trusting the write response is not enough."""
    query = (
        '{ node(id: "%s") { ... on ProjectV2Item { fieldValues(first: 20) { nodes { '
        "... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2SingleSelectField { name } } } } } } } }"
    ) % item_id
    try:
        data = gh_json(["api", "graphql", "-f", f"query={query}"])
        for node in data["data"]["node"]["fieldValues"]["nodes"]:
            if (node.get("field") or {}).get("name") == "Stage":
                return node.get("name")
    except Exception:
        return None
    return None


def add_to_board(issue_url: str) -> tuple[str, str]:
    item = gh_json(["project", "item-add", "1", "--owner", "alchimestre", "--url", issue_url, "--format", "json"])
    item_id = item["id"]
    gh(
        [
            "project", "item-edit", "--id", item_id, "--project-id", PROJECT_ID,
            "--field-id", STAGE_FIELD, "--single-select-option-id", STAGE_CONTACTED,
        ]
    )
    return item_id, item_stage(item_id) or "unverified"


# ---------------------------------------------------------------- rendering


def doc_text(job: dict, market: str | None, tier: str, tier_note: str, evidence: str, today: date, track: str = "track:bridge") -> str:
    f1a, f1b = add_business_days(today, 5), add_business_days(today, 7)
    f2a, f2b = add_business_days(today, 10), add_business_days(today, 14)
    return f"""# {job['company']} — {job['title']}

**Posting:** {job.get('url', '')} · {job.get('location') or 'location n/a'}
**Market:** {market_name(market)} · **Tier:** {tier.upper()} ({tier_note}) · **Channel:** ATS · **Track:** {track.removeprefix('track:')}
**Applied:** ✅ {today.isoformat()} · **Stage:** Contacted
**Follow-ups:** 1st due {f1a} → {f1b} · final {f2a} → {f2b}
**Evidence version used:** {evidence}
**Source:** jobradar `{job['uid']}` · score {job.get('score')} · lane `{job.get('lane')}` · \
reasons `{', '.join(job.get('reasons') or []) or 'none'}`

## To review

Auto-logged when the posting was marked applied in the pipeline tool. Outstanding:

- Confirm the §2 hard-filter verdict (below) against the JD.
- Confirm market and tier — both were assigned mechanically (`{tier_note}`).
- Write the application-answer / outreach record if one is needed before the screen.

## Hard-filter checklist (from `docs/12-week-strategy.md` §2)

- [ ] Not a Staff/Principal role (3–6 yrs expected)
- [ ] Compensation ≥ CHF 110k (CH) / €80k (DE) / €70k (bridge)
- [ ] On-site CH/DE allows 8–12 week remote start from France or provides relocation assistance
- [ ] No day-one direct GPU / training / serving expertise requirement
- [ ] Has AI workload exposure AND architectural scope (no generic runbook role)
"""


def issue_body(job: dict, market: str | None, tier: str, tier_note: str, evidence: str, today: date, track: str = "track:bridge") -> str:
    template = REPO / ".github" / "ISSUE_TEMPLATE" / "opportunity.md"
    f1a, f1b = add_business_days(today, 5), add_business_days(today, 7)
    f2a, f2b = add_business_days(today, 10), add_business_days(today, 14)
    values = {
        "Company:": f"Company: {job['company']}",
        "Role:": f"Role: {job['title']}",
        "Posting URL:": f"Posting URL: {job.get('url', '')}",
        "Market (CH / DE / EU-remote / FR):": f"Market (CH / DE / EU-remote / FR): {market_name(market)}",
        "Employer tier (A / B / C):": f"Employer tier (A / B / C): {tier.upper()} — {tier_note}",
        "Channel (outreach / ATS / recruiter):": "Channel (outreach / ATS / recruiter): ATS",
        "Evidence version used (pre-project / early Python / completed Python / Go):": f"Evidence version used (pre-project / early Python / completed Python / Go): {evidence}",
        "Contacted / applied:": f"Contacted / applied: {today.isoformat()} (applied, marked in jobradar)",
        "Follow-up 1 due (5–7 business days):": f"Follow-up 1 due (5–7 business days): {f1a} → {f1b}",
        "Follow-up 2 due (10–14 business days):": f"Follow-up 2 due (10–14 business days): {f2a} → {f2b}",
    }
    if not template.is_file():
        return "\n".join(values.values()) + f"\n\n<!-- jobradar-uid: {job['uid']} -->\n"
    lines = []
    for line in template.read_text().splitlines():
        if line.startswith("---") and not lines:  # front matter
            continue
        # Template fields are bullets in "## Target", bare labels in "## Timeline".
        stripped = line.strip().lstrip("-").strip()
        if stripped in values:
            prefix = "- " if line.strip().startswith("-") else ""
            lines.append(prefix + values[stripped])
        else:
            lines.append(line)
    body = "\n".join(lines).strip()
    body += (
        f"\n\n---\n\n_Logged automatically by `jobradar` ({RULES}) when the posting was marked applied. "
        f"Track `{track}`, market and tier are mechanical defaults: {tier_note}. Hard-filter verdict outstanding._\n"
        f"\n<!-- jobradar-uid: {job['uid']} -->\n"
    )
    return body


# ---------------------------------------------------------------- main


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="print the plan; make no changes")
    parser.add_argument("--evidence", default="pre-project")
    parser.add_argument("--tier", choices=["a", "b", "c"])
    parser.add_argument("--market", choices=["ch", "de", "eu-remote", "fr-bridge"])
    parser.add_argument("--track", choices=["track:ai", "track:web3", "track:bridge"])
    parser.add_argument("--doc-only", action="store_true", help="write the opportunity doc if missing, touch nothing else")
    args = parser.parse_args(argv)

    raw = sys.stdin.read().strip()
    if not raw:
        print("log_applied: no JSON on stdin", file=sys.stderr)
        return 1
    try:
        job = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"log_applied: invalid JSON on stdin: {exc}", file=sys.stderr)
        return 1
    for field in ("uid", "company", "title", "url"):
        if not job.get(field):
            print(f"log_applied: missing '{field}' in the posting", file=sys.stderr)
            return 1

    today = date.today()
    tier, tier_note = decide_tier(job, args.tier)
    market, market_note = decide_market(job.get("lane", ""), args.market)
    track, track_note = decide_track(job, args.track)
    rules = RULES.format(job["uid"], job.get("score"), job.get("lane"))

    existing, how = find_issue(job)
    if args.doc_only:
        doc = find_doc(job) or (REPO / "docs" / "opportunities" / f"{slugify(job['company'])}-{slugify(job['title'])}.md")
        if doc.exists():
            say(f"doc already present: {doc.relative_to(REPO)}")
            return 0
        if args.dry_run:
            say(f"[dry-run] would write {doc.relative_to(REPO)}")
            return 0
        doc.write_text(doc_text(job, market, tier, tier_note, args.evidence, today, track))
        say(f"doc written: {doc.relative_to(REPO)}")
        return 0
    if existing:
        body = (
            f"Applied {today.isoformat()} — marked in `jobradar` ({rules}).\n\n"
            f"Matched this issue by {how}. Stage set to Contacted.\n\n"
            f"<!-- jobradar-uid: {job['uid']} -->"
        )
        if args.dry_run:
            say(f"[dry-run] would comment on #{existing['number']} (matched by {how}) and set Stage=Contacted")
            return 0
        gh(["issue", "comment", str(existing["number"]), "--body", body])
        item_id, stage = add_to_board(existing["url"])
        note = "" if stage == "Contacted" else f" (board stage reads '{stage}' — check the board)"
        say(f"#{existing['number']} updated (matched by {how}) → Stage Contacted{note}")
        return 0

    doc = find_doc(job)
    doc_path = doc or (REPO / "docs" / "opportunities" / f"{slugify(job['company'])}-{slugify(job['title'])}.md")
    labels = ["channel:ats"] + ([market] if market else []) + [f"tier:{tier}", track]
    title = f"[{TITLE_PREFIX.get((job.get('lane') or '').lower(), '??')}] {job['company']} — {job['title']}"
    body = issue_body(job, market, tier, tier_note, args.evidence, today, track)

    if args.dry_run:
        say(f"[dry-run] title:      {title}")
        say(f"[dry-run] labels:     {' '.join(labels)}")
        say(f"[dry-run] doc:        {doc_path.relative_to(REPO)}")
        say(f"[dry-run] issue body: {len(body)} chars")
        say(f"[dry-run] note:       {market_note} / {tier_note} / {track_note}")
        say(body)
        return 0

    if not doc_path.exists():
        doc_path.write_text(doc_text(job, market, tier, tier_note, args.evidence, today, track))
        doc_note = f"doc {doc_path.name}"
    else:
        doc_note = f"doc {doc_path.name} (existing, untouched)"

    body_file = Path("/tmp") / f"log-applied-{job['uid']}.md"
    body_file.write_text(body)
    created = gh(
        [
            "issue", "create", "--title", title, "--body-file", str(body_file),
            *[arg for label in labels for arg in ("--label", label)],
        ]
    )
    issue_url = created.stdout.strip().splitlines()[-1] if created.stdout.strip() else ""
    if not issue_url:
        print("log_applied: gh issue create returned no URL", file=sys.stderr)
        return 1
    number = issue_url.rstrip("/").split("/")[-1]
    item_id, stage = add_to_board(issue_url)
    note = "" if stage == "Contacted" else f" · board stage reads '{stage}' — check the board"
    say(f"issue #{number} created ({' '.join(labels)}) → Stage Contacted · {doc_note}{note}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or "").strip().splitlines()
        print(f"log_applied: gh failed: {detail[-1] if detail else exc}", file=sys.stderr)
        raise SystemExit(1) from exc
