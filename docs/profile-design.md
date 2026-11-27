# Profile design

## Direction

The profile keeps its programmer shell, plain-text `.plan`, reproducible two-file example and dated activity and usage snapshots. The composition gives the central sentence more weight, connects two source swarms to a review node, and presents a separate mobile layout.

The visible surface uses the official unikode wordmark, Plus Jakarta Sans for prose and JetBrains Mono for commands. All type in the SVG artwork is outlined. The images are self-contained, static and independent of remote fonts or statistics services.

## Source and preservation

- Baseline: `75ea41079273ed5b01cd3cbc6b642f4517e85b97`.
- Design: `unikode-00/design` release `v3.0.0`, commit `ea6a0d74d2d19dedc5f72395db60e72f6e99367b`.
- Official dark wordmark SHA-256: `aa0fecd5423f59d78afce453e83e80409a64c1873299d6d8e8b79e65a15cf1d0`.
- Fonts: the Design release's Plus Jakarta Sans and JetBrains Mono assets, with their SIL Open Font Licenses in `assets/source/`.
- `.plan`, both source example files, the usage chart images and all recorded numerical values are preserved.
- Counts remain the November 27, 2026 snapshot. Trackers have overlapping coverage; their totals must not be summed.

## Rendering contract

The native GitHub page owns scrolling, link focus, themes and disclosure controls. The authored shell stays on its accepted charcoal ground in both GitHub themes. It uses no simulated controls, status badges, gradients, decorative frames or JavaScript.

The image source switches to a stacked composition at viewport widths of 1100px and below, including GitHub's narrow desktop content column. Native text supplies the `.plan`, example and statistics independently of the image. Both SVGs have titles and descriptions, and README images have meaningful alt text.

Applicable Design patterns: DES-LAW-001, DES-LAW-006, DES-LAW-008, DP-UXUI-001, DP-UXUI-004, DP-UXUI-005 and DP-UXUI-012. Scope: static README, native GitHub disclosures and links. Custom interaction choreography and application shell behavior do not apply.

## Rebuild

With Python, `fonttools` and `brotli` installed, run:

```sh
python tools/build_profile.py
```

The generator reads the pinned files in `assets/source/` and writes the two shell SVGs. Keep the wordmark geometry intact. Inspect both outputs at their rendered sizes before publishing.

## Verification

Reviewed on November 27, 2026:

- An independent visual review passed the desktop artwork and the mobile artwork rendered at 320px wide, with no clipping or collisions.
- GitHub rendered the desktop SVG at 838px wide from the candidate branch. The image loaded at its expected 1440px intrinsic width, and the two-file example link resolved to its directory and rendered instructions.
- All nine external links returned HTTP 200; the mail, chat and app anchors exist. Relative links resolve to repository files or directories.
- The displayed commands reproduce the two source files' diff. All original numerical values and preserved source files were checked against the baseline.
- The candidate had no configured status checks or workflow runs; validation was performed directly rather than attributed to CI.

Reviewed artwork SHA-256:

```text
shell-v2.svg         d823d1f16d1b1762c407664be1dcb4d7bb64532bfd57942fae253d92a9148e83
shell-mobile-v2.svg  550b1cc6f7a523c83e49237428e57f244de3d5e4656954fe46ec613440e8dc26
```
