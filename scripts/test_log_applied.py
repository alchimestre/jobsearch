#!/usr/bin/env python3
"""Self-checks for log_applied.py — no test framework, no network, no gh calls.

    python3 scripts/test_log_applied.py

Covers the pure decision logic: the parts that silently mis-file an application.
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

SCRIPT = Path(__file__).with_name("log_applied.py")
spec = importlib.util.spec_from_file_location("log_applied", SCRIPT)
log_applied = importlib.util.module_from_spec(spec)
spec.loader.exec_module(log_applied)

FAILURES: list[str] = []


def check(name: str, got, want) -> None:
    if got != want:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}")
        print(f"FAIL {name}: got {got!r}, want {want!r}")
    else:
        print(f"ok   {name}")


def job(company: str, title: str, **rest) -> dict:
    return {"uid": "abc123", "company": company, "title": title, "url": "https://example.invalid/1", **rest}


# ---- slugify -----------------------------------------------------------

check("slugify strips punctuation", log_applied.slugify("Nebius"), "nebius")
check("slugify handles brackets", log_applied.slugify("Senior Platform Engineer (m/f/d)"), "senior-platform-engineer-m-f-d")
check("slugify truncates", len(log_applied.slugify("x" * 200)), 60)

# ---- business days -----------------------------------------------------

monday = date(2026, 9, 28)
friday = date(2026, 10, 2)
check("+5 business days from Monday skips the weekend", log_applied.add_business_days(monday, 5), date(2026, 10, 5))
check("+7 business days from Monday", log_applied.add_business_days(monday, 7), date(2026, 10, 7))
check("+10 business days from Monday", log_applied.add_business_days(monday, 10), date(2026, 10, 12))
check("+14 business days from Monday", log_applied.add_business_days(monday, 14), date(2026, 10, 16))
check("+1 business day from Friday is Monday", log_applied.add_business_days(friday, 1), date(2026, 10, 5))

# ---- tier --------------------------------------------------------------

tier, note = log_applied.decide_tier(job("Nebius", "ML Infrastructure Engineer", reasons=["+ml-infra", "+infra"]), None)
check("ML-infra title scores tier b", tier, "b")
tier, _ = log_applied.decide_tier(job("Acme", "DevOps Engineer", reasons=["+devops"]), None)
check("no ML signal scores tier c", tier, "c")
tier, note = log_applied.decide_tier(job("Acme", "Anything", reasons=[]), "a")
check("explicit tier override wins", (tier, note), ("a", "set explicitly"))

# ---- market ------------------------------------------------------------

check("lane de maps to the DE label", log_applied.decide_market("de", None)[0], "market:de")
check("lane eu-remote maps to the remote label", log_applied.decide_market("eu-remote", None)[0], "market:eu-remote")
check("unmapped lane yields no label", log_applied.decide_market("other", None)[0], None)
check("explicit fr-bridge override", log_applied.decide_market("de", "fr-bridge")[0], "market:fr-bridge")
check("the doc shows a human market name, not the label", log_applied.market_name("market:eu-remote"), "EU-remote")
check("an unknown market reads UNREVIEWED", log_applied.market_name(None), "UNREVIEWED")

# ---- track -------------------------------------------------------------
# Web3 is in scope, so the funnel must be able to tell the two tracks apart.
check(
    "an ML/MLOps posting is track:ai",
    log_applied.decide_track(job("Acme", "MLOps Engineer", reasons=["+mlops", "+k8s"]))[0],
    "track:ai",
)
check(
    "a blockchain infrastructure posting is track:web3",
    log_applied.decide_track(job("Chainlink Labs", "Blockchain Infrastructure Engineer", reasons=["+infra", "+blockchain"]))[0],
    "track:web3",
)
check(
    "AI wins when a posting carries both signals",
    log_applied.decide_track(job("Acme", "ML Platform Engineer, Blockchain", reasons=["+ml-platform", "+blockchain"]))[0],
    "track:ai",
)
check(
    "no signal at all is track:bridge",
    log_applied.decide_track(job("Acme", "Platform Engineer", reasons=["+platform"]))[0],
    "track:bridge",
)
check("track override is honoured", log_applied.decide_track(job("Acme", "X", reasons=[]), "track:web3")[0], "track:web3")

# ---- doc matching ------------------------------------------------------
# Regression: matching on the employer alone made a second Nebius role reuse the
# first Nebius doc instead of getting its own.

fake_repo = Path(tempfile.mkdtemp())
(fake_repo / "docs" / "opportunities").mkdir(parents=True)
(fake_repo / "docs" / "opportunities" / "nebius-ml-infrastructure-engineer.md").write_text("# Nebius\n")
(fake_repo / "docs" / "opportunities" / "vivenu-senior-platform-engineer.md").write_text("# vivenu\n")
(fake_repo / "docs" / "opportunities" / "vcluster-ai-infrastructure-engineer.md").write_text("# vCluster\n")
original_repo = log_applied.REPO
log_applied.REPO = fake_repo
try:
    check(
        "same role reuses its doc",
        log_applied.find_doc(job("Nebius", "ML Infrastructure Engineer")).name,
        "nebius-ml-infrastructure-engineer.md",
    )
    check(
        "a different role at the same employer gets a new doc",
        log_applied.find_doc(job("Nebius", "Senior Site Reliability Engineer — Token Factory")),
        None,
    )
    check(
        "employer abbreviation still matches",
        log_applied.find_doc(job("vCluster Labs", "AI Infrastructure Engineer")).name,
        "vcluster-ai-infrastructure-engineer.md",
    )
    check(
        "doc reuse tolerates the parenthesised suffix in JDs",
        log_applied.find_doc(job("vivenu", "Senior Platform Engineer (d/f/m)")).name,
        "vivenu-senior-platform-engineer.md",
    )
    check("unknown employer yields no doc", log_applied.find_doc(job("NewCo", "ML Platform Engineer")), None)
finally:
    log_applied.REPO = original_repo
    shutil.rmtree(fake_repo)

# ---- issue body --------------------------------------------------------

body = log_applied.issue_body(job("Acme", "ML Platform Engineer"), "market:de", "b", "test", "pre-project", date(2026, 9, 29))
check("body carries the uid marker for idempotent re-runs", "<!-- jobradar-uid: abc123 -->" in body, True)
check("body has the review sections", "## Target" in body and "## Timeline" in body, True)
check("body records the follow-up window", "Follow-up 1 due (5–7 business days): 2026-10-06 → 2026-10-08" in body, True)
check("body does not leak YAML front matter", body.lstrip().startswith("---"), False)
check(
    "issue body fills the Target fields, bullets intact",
    "- Company: Acme" in body
    and "- Market (CH / DE / NL / EU-remote / FR): DE" in body
    and "- Employer tier (A / B / C): B — test" in body
    and "\n- Company: \n" not in body,
    True,
)
check(
    "issue body fills the Timeline dates",
    "- Contacted / applied: 2026-09-29" in body
    and "- Follow-up 2 due (10–14 business days): 2026-10-13 → 2026-10-19" in body,
    True,
)
check(
    "no template field is left blank",
    all(
        line.split(":", 1)[1].strip() or ":" not in line
        for line in body.splitlines()
        if line.startswith(("- Company:", "- Role:", "- Posting URL:", "- Contacted / applied:", "- Follow-up"))
    ),
    True,
)
doc = log_applied.doc_text(job("Acme", "ML Platform Engineer"), "market:de", "b", "test", "pre-project", date(2026, 9, 29), "track:ai")
check("doc renders the market name, not the label", "**Market:** DE ·" in doc, True)
check("doc carries the track", "**Track:** ai" in doc, True)
check("doc carries the jobradar uid", "abc123" in doc, True)

print()
if FAILURES:
    print(f"{len(FAILURES)} failure(s)")
    sys.exit(1)
print("all checks passed")
