// CV 3_white — apply the 2026-09-11 resume edits (2nd amendment).
// Run in Figma desktop: Plugins → Scripter → paste → Run (Cmd+Enter).
// Reports per rule in the Scripter console AND as a toast, then applies.
//
// Idempotent: every rule carries a `guard`. If the guard text is already present
// the rule is skipped, so re-running is a no-op and cannot duplicate text.
// Self-repairing: the location rule that duplicated its own suffix is fixed by a
// collapse rule, and the rule set re-runs per node until the text stops changing.
// Undo with Cmd+Z if anything looks wrong.
//
// Rules exist in two variants where the file has already been edited by hand:
// the pre-export wording (v3) and the wording present in v5. Only the matching
// variant fires; the other reports MISS, which is expected, not an error.

const DRY_RUN = false; // true = report only, false = apply
const SCOPE = "document"; // "document" | "page" | "selection"
const MAX_PASSES = 5; // per node; lets collapse rules converge

// ---------------------------------------------------------------- edit table
// [find, replace, guard?]
//   find  — literal text to match. A space matches any whitespace (including a
//           line break), any dash matches -, ‑, –, —, and ' also matches ’.
//   guard — if this text already exists in the node, skip the rule.
const REPLACEMENTS = [
  // 1. Title — v3 wording, then v5 wording
  [
    "Site Reliability & Platform Engineer",
    "Site Reliability Engineer — moving into ML Platform / MLOps",
    "ML Platform / MLOps",
  ],
  [
    "Site Reliability Engineer — moving into AI Infrastructure",
    "Site Reliability Engineer — moving into ML Platform / MLOps",
    "ML Platform / MLOps",
  ],

  // 2. Location line — guarded so it can never append its own suffix twice
  [
    "Aix-en-Provence, France",
    "Aix-en-Provence, France · Open to EU-remote, Berlin, Switzerland",
    "Open to EU-remote",
  ],
  // 2b. Repair: collapse a location line that the unguarded version duplicated
  [
    "Open to EU-remote, Berlin, Switzerland · Open to EU-remote, Berlin, Switzerland",
    "Open to EU-remote, Berlin, Switzerland",
  ],

  // 3. Profile paragraph — v3 full-text variant
  [
    "Infrastructure-focused SRE building scalable platforms for compute-intensive and GPU workloads. Combines deep expertise in distributed systems, multi-environment Kubernetes, and high-availability architecture. Driven by optimizing performance, reducing cloud costs, and hardening production systems.",
    "Production SRE with 4 years operating high-availability distributed infrastructure across regulated healthcare, crypto, and multi-protocol systems. Moving into ML platform / MLOps — bringing Kubernetes reliability, observability, and cost-aware platform operations to the platform that builds, ships, and serves models.",
    "platform that builds, ships, and serves models",
  ],
  // 3b. Profile paragraph — v5 tail variant
  [
    "Moving into AI infrastructure — bringing Kubernetes reliability, observability, and cost-aware platform operations to the compute and serving layers AI workloads depend on.",
    "Moving into ML platform / MLOps — bringing Kubernetes reliability, observability, and cost-aware platform operations to the platform that builds, ships, and serves models.",
    "platform that builds, ships, and serves models",
  ],

  // 4. Kiln — Helm in the IaC bullet, then the architecture-translation bullet
  [
    "Designed and maintained Infrastructure-as-Code (Terraform) across multi-environment Kubernetes clusters",
    "Designed and maintained Terraform IaC and Helm charts across multi-environment Kubernetes clusters",
    "Helm charts across multi-environment Kubernetes clusters",
  ],
  [
    "Collaborated with engineering and product teams to translate infrastructure constraints into scalable architectural decisions.",
    "Translated infrastructure constraints into scalable architectural decisions with engineering and product teams",
    "Translated infrastructure constraints",
  ],

  // 5. Cometh — Helm at cluster level (25% and Oct 2023 already correct)
  [
    "Managed multi-zone Kubernetes clusters on GCP in a production environment",
    "Managed multi-zone Kubernetes clusters on GCP in production, deploying services with Helm charts",
    "deploying services with Helm charts",
  ],

  // 6. Skills — drop the GPU ownership claim and the crypto keyword
  ["GPU Workloads · Ethereum", "GPU exposure", "GPU exposure"],
  ["GPU Workloads", "GPU exposure", "GPU exposure"], // fallback if the list is split
  [" · Ethereum", "", "GPU exposure"], // leading separator: never hits Bitgen's "Ethereum services"

  // 7. Spelling
  ["Application Developper Degree", "Application Developer Degree", "Application Developer Degree"],
];

// ------------------------------------------------------------- implementation
const DASH_SENTINEL = "\u0000";

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function buildMatcher(text) {
  const body = escapeRegex(text.replace(/[-\u2010\u2011\u2012\u2013\u2014]/g, DASH_SENTINEL))
    .replace(/\s+/g, "\\s+")
    .replace(/'/g, "['\u2019]")
    .replace(new RegExp(DASH_SENTINEL, "g"), "[-\u2010\u2011\u2012\u2013\u2014]");
  return new RegExp(body);
}

const matcherCache = new Map();
function matcherFor(text) {
  if (!matcherCache.has(text)) matcherCache.set(text, buildMatcher(text));
  return matcherCache.get(text);
}

async function loadFonts(node) {
  const fonts =
    node.fontName === figma.mixed
      ? node.getRangeAllFontNames(0, node.characters.length)
      : node.fontName
        ? [node.fontName]
        : [];
  for (const font of fonts) {
    try {
      await figma.loadFontAsync(font);
    } catch (e) {
      throw new Error(`missing font "${font.family} ${font.style}"`);
    }
  }
}

function collectTextNodes(root) {
  const out = [];
  const walk = (n) => {
    if (n.type === "TEXT") out.push(n);
    else if ("children" in n) n.children.forEach(walk);
  };
  if (root.type === "TEXT") out.push(root);
  else if ("children" in root) root.children.forEach(walk);
  return out;
}

async function main() {
  const selection = figma.currentPage.selection;
  const roots =
    SCOPE === "document"
      ? [figma.root]
      : SCOPE === "auto" && selection.length > 0
        ? selection
        : [figma.currentPage];

  const nodes = roots.flatMap(collectTextNodes);
  const counts = REPLACEMENTS.map(() => 0);
  const skipped = [];
  const touched = [];

  for (const node of nodes) {
    const before = node.characters;
    let after = before;

    for (let pass = 0; pass < MAX_PASSES; pass++) {
      let changedThisPass = false;

      for (let i = 0; i < REPLACEMENTS.length; i++) {
        const [find, replace, guard] = REPLACEMENTS[i];
        if (guard && matcherFor(guard).test(after)) continue; // already applied
        const re = matcherFor(find);
        if (!re.test(after)) continue;
        const updated = after.replace(re, replace);
        if (updated !== after) {
          after = updated;
          counts[i] += 1;
          changedThisPass = true;
        }
      }

      if (!changedThisPass) break;
    }

    if (after === before) continue;

    try {
      await loadFonts(node);
      if (!DRY_RUN) node.characters = after;
      touched.push(`${node.name || node.id}${DRY_RUN ? " (would change)" : ""}`);
    } catch (e) {
      skipped.push(`${node.name || node.id}: ${e.message}`);
    }
  }

  const lines = REPLACEMENTS.map(([find], i) => {
    const label = find.length > 52 ? find.slice(0, 49) + "…" : find;
    return `${counts[i] > 0 ? "ok  " : "MISS"} ${counts[i]}x  ${label}`;
  });

  console.log(
    `${DRY_RUN ? "[dry run] " : ""}${nodes.length} text nodes scanned\n` +
      lines.join("\n") +
      `\nchanged (${touched.length}):\n` +
      (touched.length ? touched.map((t) => `  - ${t}`).join("\n") : "  (none)") +
      (skipped.length ? `\nskipped (font unavailable):\n${skipped.join("\n")}` : ""),
  );

  const applied = counts.reduce((a, b) => a + b, 0);
  figma.notify(
    `${DRY_RUN ? "Would apply" : "Applied"} ${applied} edit(s) in ${touched.length} node(s)` +
      ` · ${nodes.length} scanned` +
      (skipped.length ? ` · ${skipped.length} skipped` : ""),
  );
}

main();
