---
version: alpha
name: SahkarAI — Frame (video / frame layer, Hindi, 9:16)
description: >
  SahkarAI brand at frame scale, for a portrait (1080×1920) Hindi explainer. Paper grounds, never
  black. Colour is ONE ramp — sky → teal → emerald — used only as SHAPE (arcs, halftone dots, chips,
  bars, rings). Type is always ink on paper. Every curve is struck from a circle, because the mark is.
  Rounded elevated cards. Devanagari set in Noto Sans Devanagari and NEVER letter-spaced.
unit: the frame — 1080×1920 portrait
principle: ink type on paper · ramp colour as shape only · every curve is a circle · facts come from the circular

colors:
  canvas: "#f3f7fa"          # paper — every frame's ground
  paper-2: "#dfe6ee"         # deeper paper for curved ground swells
  ink: "#0f172a"             # headlines, numerals
  body: "#35455c"            # body copy
  muted: "#64748b"           # eyebrows, labels
  faint: "#94a3b8"           # hairlines, ghost numerals
  line: "#e2e9f0"            # card borders / rules
  card: "#ffffff"            # elevated card fill
  sky: "#38bdf8"             # ramp start — shape only
  sky-deep: "#0284c7"        # ramp start, deep — shape only
  teal: "#0d9488"            # ramp middle — shape only; the ONE colour allowed on large (≥64px) numerals
  emerald: "#34d399"         # ramp end — shape only
  emerald-deep: "#059669"    # ramp end, deep — shape only
  mint: "#e7f8f1"            # emerald 10% tint for chips/grounds
  skywash: "#e6f5fd"         # sky 10% tint for chips/grounds

ramp:
  gradient: "linear-gradient(90deg, #0284c7 0%, #0ea5e9 25%, #0d9488 45%, #10b981 65%, #059669 100%)"
  description: "The ribbon gradient from the mark. Use for arcs, progress bars, ring strokes, dot fields."

radii:
  card: "36px"
  chip: "999px"
  small: "18px"

shadows:
  card: "0 2px 4px rgba(15,23,42,.04), 0 18px 48px -12px rgba(15,23,42,.14)"
  float: "0 30px 80px -20px rgba(13,148,136,.28)"

typography:
  # Devanagari: Noto Sans Devanagari — NO letter-spacing, ever (tracking breaks the shirorekha).
  # Latin + numerals: Heebo. Tracking allowed on Latin eyebrows only.
  display: { fontFamily: "Noto Sans Devanagari", px: 104, weight: 700, lineHeight: 1.18, color: "ink" }
  h1:      { fontFamily: "Noto Sans Devanagari", px: 84,  weight: 700, lineHeight: 1.2,  color: "ink" }
  h2:      { fontFamily: "Noto Sans Devanagari", px: 60,  weight: 700, lineHeight: 1.25, color: "ink" }
  body:    { fontFamily: "Noto Sans Devanagari", px: 40,  weight: 500, lineHeight: 1.5,  color: "body" }
  label:   { fontFamily: "Noto Sans Devanagari", px: 32,  weight: 500, lineHeight: 1.4,  color: "muted" }
  numeral: { fontFamily: "Heebo", px: 260, weight: 900, lineHeight: 0.9, color: "ink", tabular: true }
  eyebrow-latin: { fontFamily: "Heebo", px: 26, weight: 700, tracking: "0.14em", upper: true, color: "muted" }

components:
  paper-ground:
    description: >
      Full-bleed #f3f7fa, plus one or two very large circles (diameter 1.4–2.2× canvas width) in
      paper-2 / skywash / mint running off an edge — the "curved ground". Never a flat empty field.
  halftone-field:
    description: >
      The brand's image language: a generated SVG halftone — offset dot grid (~14px pitch at 1080w),
      dot radius modulated by a field (a rising sun with exponential glow, perspective furrows converging
      to a horizon, or a soft radial swell). Dot colours sampled ONLY from the ramp (sky above horizon,
      teal→emerald in the fields). No photos, no people.
  card:
    backgroundColor: "{colors.card}"
    rounded: "{radii.card}"
    border: "1.5px solid {colors.line}"
    shadow: "{shadows.card}"
    description: "Rounded elevated white card on paper. Content cards, step cards, stat cards."
  chip:
    backgroundColor: "{colors.skywash} or {colors.mint}"
    rounded: "{radii.chip}"
    typography: "label, ink"
    description: "Pill label. A small ramp dot (sky or emerald circle) may lead it."
  ramp-bar:
    fill: "{ramp.gradient}"
    rounded: "{radii.chip}"
    description: "Progress / timeline / limit bars."
  step-node:
    description: "Circle node 96px, ring stroke in the ramp, ink numeral (Heebo 900) centered."
  two-heads:
    description: >
      Brand motif from the mark: a sky circle and an emerald circle (radial-lit, #7dd3fc→#0284c7 and
      #6ee7b7→#059669) — may stand in as bullets, avatars for 'farmer' and 'society', or the close.
  logo:
    description: "Use ../../sahkarai-lockup-light.svg / ../../sahkarai-mark.svg content inline (copied to assets/). Close only."
  frame-chrome:
    description: >
      Top-left: small Latin eyebrow 'SAHKARAI EXPLAINS' (Heebo, tracked) with the two-heads dot pair.
      Top-right: a chip showing the change number (e.g. '२ / ४') when inside the four-change run.
---

# SahkarAI — Frame (video / frame layer)

## Overview

A warm, confident public-information explainer that feels like SahkarAI's brand board in motion: light
paper, big Devanagari type in ink, and colour that only ever arrives as shape — a sweeping arc struck from
a circle, a halftone field of dawn over furrowed fields, a ramp-filled bar, two glowing heads. Nothing is
black; nothing imitates a government letterhead.

## Rules that are never broken

- **Paper ground on every frame**; curved circle-swells in paper-2 / skywash / mint for depth. No dark frames.
- **Type is ink.** Headlines ink #0f172a, body #35455c. Ramp colours never set text — except teal on very
  large numerals (≥64px) where contrast holds.
- **Devanagari is never letter-spaced**; `letter-spacing: normal` on every Devanagari element.
  Latin eyebrows may track.
- **Every curve is a circle** (arcs, rings, swells). No freeform blobs, no purple-blue AI gradients, no bokeh.
- **Rounded elevated cards** (36px radius, soft two-layer shadow) are the container for content.
- **Numerals in Heebo 900**, tabular.
- **Halftone** is the only "image" — generated dots in the ramp.
- `<meta charset="utf-8">` in every composition.

## Portrait layout

- 1080×1920. Side gutters 80px. Content lives in the top ~83% (caption band below ≈1590px).
- Anchor a centered hero near y ≈ 806. Chrome row at y ≈ 110.
- Stack vertically; one idea per frame; short Hindi lines (≤ 14 words per line block).

## Motion

- Long-tail eases (power3/expo out), smooth over bouncy; one gentle spring (back.out(1.4)) allowed on chips/nodes.
- Reveal each element when the Hindi VO names it; hold still once resolved.
- Arcs draw on (stroke-dashoffset), bars fill left→right, halftone dots bloom from the horizon outward.
