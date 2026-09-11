// CV 3_white — apply the 2026-09-11 resume edits.
// Run in Figma desktop: Plugins → Scripter → paste → Run (Cmd+Enter).
// Reports per rule in the Scripter console AND as a toast, then applies.
// Idempotent: re-running after a successful pass reports 0 changes.
// Undo with Cmd+Z if anything looks wrong.
// If the CV frame is not on the active page, the document scope still finds it.
const DRY_RUN = false; // true = report only, false = apply
const SCOPE = "document"; // "document" | "page" | "selection"

// ---------------------------------------------------------------- edit table
// [find, replace]. In `find`, a space matches any whitespace (including a line
// break), a hyphen also matches -, ‑, –, —, and an apostrophe also matches ’.
const REPLACEMENTS = [
  // 1. Title
  [
    "Site Reliability & Platform Engineer",
    "Site Reliability Engineer — moving into AI Infrastructure",
  ],

  // 2. Location line
  [
    "Aix-en-Provence, France",
    "Aix-en-Provence, France · Open to EU-remote, Berlin, Switzerland",
  ],

  // 3. Profile paragraph (replace the entire body text)
  [
    "Infrastructure-focused SRE building scalable platforms for compute-intensive and GPU workloads. Combines deep expertise in distributed systems, multi-environment Kubernetes, and high-availability architecture. Driven by optimizing performance, reducing cloud costs, and hardening production systems.",
    "Production SRE with 4 years operating high-availability distributed infrastructure across regulated healthcare, crypto, and multi-protocol systems. Moving into AI infrastructure — bringing Kubernetes reliability, observability, and cost-aware platform operations to the compute and serving layers AI workloads depend on.",
  ],

  // 4. Kiln — add Helm, tighten the architecture-translation bullet
  [
    "Designed and maintained Infrastructure-as-Code (Terraform) across multi-environment Kubernetes clusters",
    "Designed and maintained Terraform IaC and Helm charts across multi-environment Kubernetes clusters",
  ],
  [
    "Collaborated with engineering and product teams to translate infrastructure constraints into scalable architectural decisions.",
    "Translated infrastructure constraints into scalable architectural decisions with engineering and product teams",
  ],

  // 5. Cometh — Helm at cluster level (25% and Oct 2023 confirmed; left untouched)
  [
    "Managed multi-zone Kubernetes clusters on GCP in a production environment",
    "Managed multi-zone Kubernetes clusters on GCP in production, deploying services with Helm charts",
  ],

  // 6. Skills — drop the GPU ownership claim and the crypto keyword, keep the
  //    honest "GPU exposure" wording. Helm is already present in the live file.
  ["GPU Workloads · Ethereum", "GPU exposure"],
  ["GPU Workloads", "GPU exposure"], // fallback if the list is split across nodes
  [" · Ethereum", ""], // leading separator kept in the match: never hits Bitgen's "Ethereum services"

  // 7. Spelling (confirmed against the export's text runs)
  ["Application Developper Degree", "Application Developer Degree"],
];

// ------------------------------------------------------------- implementation
function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function buildMatcher(find) {
  const body = escapeRegex(find)
    .replace(/\s+/g, "\\s+")
    .replace(/\\-/g, "[-\\u2010\\u2011\\u2013\\u2014]")
    .replace(/'/g, "['\\u2019]");
  return new RegExp(body);
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

  for (const node of nodes) {
    const before = node.characters;
    let after = before;

    for (let i = 0; i < REPLACEMENTS.length; i++) {
      const [find, replace] = REPLACEMENTS[i];
      const re = buildMatcher(find);
      if (!re.test(after)) continue;
      const updated = after.replace(re, replace);
      if (updated !== after) {
        after = updated;
        counts[i] += 1;
      }
    }
    if (after === before) continue;

    try {
      await loadFonts(node);
      if (!DRY_RUN) node.characters = after;
    } catch (e) {
      skipped.push(`${node.name || node.id}: ${e.message}`);
    }
  }

  const lines = REPLACEMENTS.map(([find], i) => {
    const label = find.length > 56 ? find.slice(0, 53) + "…" : find;
    return `${counts[i] > 0 ? "ok  " : "MISS"} ${counts[i]}x  ${label}`;
  });

  console.log(
    `${DRY_RUN ? "[dry run] " : ""}${nodes.length} text nodes scanned\n` +
      lines.join("\n") +
      (skipped.length ? `\nskipped (font unavailable):\n${skipped.join("\n")}` : ""),
  );

  const applied = counts.reduce((a, b) => a + b, 0);
  figma.notify(
    `${DRY_RUN ? "Would apply" : "Applied"} ${applied} edit(s) across ${nodes.length} text nodes` +
      (skipped.length ? ` · ${skipped.length} skipped` : ""),
  );
}

main();
