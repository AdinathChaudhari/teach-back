"""Upgrade teach-back pages to layout v2.

The section index is pinned to the left edge of the window, the reading column is
centred in the window (Reader-view style), body text is a fixed 17px that the
A-/A/A+ control multiplies through --tb-scale, and wide tables and ASCII blocks
bleed evenly on both sides of the column. Phones (860px and under) keep the
top-bar index at 16px.

Usage: python3 scripts/patch_layout.py PAGE.html [...]
Idempotent: a page that already has the layout v2 block is skipped. Pages built
from kit/template.html after this change already have it.
"""
import sys

MARK = "/* layout v2 */"
CSS = MARK + """
:root { --tb-base: 106.25%; --measure: 34rem; --rail-w: 13rem; --rail-gap: 2.5rem; --edge: 1.5rem; --bleed-max: 12rem; }
html { font-size: calc(var(--tb-scale, 1) * var(--tb-base)); }
@media (max-width: 860px) { :root { --tb-base: 100%; --measure: 32rem; } }
@media (min-width: 861px) {
  .page {
    grid-template-columns:
      minmax(calc(var(--edge) + var(--rail-w) + var(--rail-gap)), 1fr)
      minmax(0, var(--measure))
      minmax(var(--edge), 1fr);
    column-gap: 0; max-width: none; margin: 0; padding: 0;
    container-type: inline-size;
  }
  .rail { justify-self: start; width: var(--rail-w); margin-left: max(var(--edge), env(safe-area-inset-left, 0px)); }
  main {
    max-width: none;
    --bleed: clamp(0rem, (100cqi - var(--measure)) / 2 - var(--edge) - var(--rail-w) - var(--rail-gap), var(--bleed-max));
  }
  .sec > .tblwrap, .sec > pre.ascii { margin-inline: calc(-1 * var(--bleed)); }
}
/* stepper goes wide only when diagram and caption fit side by side; otherwise it stays in the column */
@container (min-width: 90rem) {
  .sec > .pipeline > .stepper { margin-inline: calc(-1 * var(--bleed)); }
  .sec > .pipeline > .stepper:not([hidden]) {
    display: grid; grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); grid-template-rows: auto 1fr auto;
    column-gap: 2rem; align-items: start; padding: 1rem 1.25rem;
  }
  .sec > .pipeline > .stepper > svg { grid-row: 1 / span 3; max-width: none; margin: 0; }
}
@media (min-width: 861px) and (max-width: 1199px) { :root { --rail-w: 11.5rem; --rail-gap: 2rem; --edge: 1rem; } }
@media (min-width: 1600px) { :root { --rail-w: 14rem; --rail-gap: 3rem; --edge: 2rem; } }
"""
# The text-size control used to set html font-size directly; layout v2 sets a multiplier instead.
SUBS = [
    ("document.documentElement.style.fontSize = tbz;",
     "document.documentElement.style.setProperty('--tb-scale', parseFloat(tbz) / 100);"),
    ("root.style.fontSize = pct + '%';",
     "root.style.setProperty('--tb-scale', pct / 100);"),
    ("now.textContent = Math.round(16 * pct / 100 * 10) / 10 + 'px text';",
     "now.textContent = Math.round(parseFloat(getComputedStyle(root).fontSize) * 10) / 10 + 'px text';"),
]
END = "/* === KIT END (css) === */"
OLD = "/* fluid v1 */"  # an earlier interim block; replaced if present

bad = 0
for p in sys.argv[1:]:
    s = open(p, encoding="utf-8").read()
    if MARK in s:
        print("SKIP", p)
        continue
    if s.count(END) != 1:
        print("FAIL no KIT END", p)
        bad += 1
        continue
    for a, b in SUBS:
        s = s.replace(a, b)
    if "--tb-scale" not in s:
        print("FAIL size control not converted", p)
        bad += 1
        continue
    i, j = s.find(OLD), s.find(END)
    s = (s[:i] if 0 <= i < j else s[:j]) + CSS + s[j:]
    open(p, "w", encoding="utf-8").write(s)
    print("OK", p)
sys.exit(1 if bad else 0)
