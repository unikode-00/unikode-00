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
