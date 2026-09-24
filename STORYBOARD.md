---
format: 1080x1920
duration: 120s
message: "किसान क्रेडिट कार्ड अब ऑनलाइन — एक साल, एक सीमा, पाँच साल की वैधता, और समय पर चुकाने पर पूरा लाभ"
arc: listicle (hook → name the news → 4 changes, each a short run → fine print → CTA → brand)
audience: Madhya Pradesh farmers, PACS managers and DCCB branch staff, watching on WhatsApp
mode: autonomous
music: warm acoustic guitar with subtle Indian flute, hopeful and institutional
---

## Video direction

**Source.** Every fact is from MP Commissioner Cooperation circular क्र. 1458/2026 and the attached GoMP order
F 12-01/2020/15-1 dt 30.06.2026. Do not add figures. Do not imitate a government letterhead or seal.

**Voice-anchored timing (load-bearing).** Narration is ElevenLabs "Devi" (Hindi). Every Scene window below is
keyed to real word timestamps (frame-local seconds, shown as `@t`). An element enters on the word that names
it — start its entrance tween 0.08–0.15s BEFORE the word's `@t` so it is visibly arriving as the word lands.
Nothing appears before its cue. Numbers count up so they LAND on their word.

**Palette (frame.md).** Paper #f3f7fa ground on every frame; curved circle-swells in #dfe6ee / #e6f5fd /
#e7f8f1 running off an edge. Colour = the ramp sky #38bdf8 / #0284c7 → teal #0d9488 → emerald #34d399 / #059669,
used only as SHAPE (arcs, halftone dots, bars, rings, chips, the two heads). Type is ink #0f172a, body #35455c,
muted #64748b. Teal allowed on giant numerals only. White rounded cards (36px radius) with soft two-layer shadow.

**Type.** Hindi in Noto Sans Devanagari (700 headlines, 500 body), `letter-spacing: normal` ALWAYS on Devanagari.
Numerals in Heebo 900, tabular. Latin eyebrow "SAHKARAI EXPLAINS" in Heebo 700 tracked 0.14em.

**Chrome.** Top-left at y≈110: two small glowing dots (sky + emerald, the "two heads") + eyebrow
"SAHKARAI EXPLAINS". Frames 3–9 add a top-right chip "बदलाव N / 4" (N as Devanagari numeral १ २ ३ ४) with a
tiny ramp ring that fills N quarters. Chrome enters in the first 0.4s and stays still.

**Layout.** 1080×1920 portrait. 80px side gutters. All content above y=1590 (caption band below). Heroes anchor
near y≈806. Stack vertically. The hero element fills 40–60% of the frame.

**Motion grammar.** power3.out / expo.out entrances, 0.5–0.8s; back.out(1.4) only on chips, nodes and pills.
Arcs draw on via stroke-dashoffset; bars fill left→right; halftone dots bloom from the horizon/centre outward
with a stagger by distance. Once resolved, HOLD STILL — at most a very slow (≤2%) drift on the background
halftone. No bouncing idles. Both failure modes are banned: slideshow (front-load then freeze) and screensaver
(everything floating).

**Rhythm / holds.** Frame 2 ends on a held "४ बड़े बदलाव" beat; frame 9 holds on the three-stat stack for the last
1.5s; frame 12 holds the lockup ~2.5s.

**Never.** Black or dark frames; purple-blue AI gradients; bokeh; stock photos; people's faces; emoji;
letter-spaced Devanagari; ramp colours as body text; government emblems or letterhead.

**Captions.** Karaoke Hindi captions run in the bottom band (built by the pipeline). Frames never place text there.

## Frame 1 — The old headache

- scene: two separate calendars (खरीफ़ / रबी) with different limits and due dates split apart; tangled arithmetic scribbles pile up
- voiceover: "खरीफ़ की अलग सीमा… रबी की अलग तारीख़… और हर बार नया हिसाब।"
- duration: 6.13s
- transition_in: cut
- status: animated
- src: compositions/frames/01-old-headache.html
- type: hook
- persuasion: Pain validation + contrast setup
- beat: recognition
- blueprint: kinetic-type-beats (Adapt)
- focal: two season cards, pulled apart
- roles: halftone field (dawn over furrows, dim ~35%, lower 45% of frame) = background · खरीफ़ card + रबी card = foreground · ghost calculation marks = supporting
- sfx: tick

narrativeRole: Opens on the friction every KCC holder knows — two seasons, two limits, two dates.
keyMessage: The old system split one farmer's year into two separate loan cycles.

Adapt: keep the statement-builds-across-beats signature; each beat is a card rather than a word swap.
Scene 1 (0.0–0.5s): paper ground with a pale sky circle-swell top-right; halftone furrows faintly bloom at the bottom (behind, dim). Chrome fades in.
Scene 2 (0.5–2.2s): @0.60 "खरीफ़" — a white rounded card slides up into the upper-left third: label "खरीफ़" (h1, ink) with a small sky-dot, beneath it a chip "अलग सीमा" that pops @1.51 "सीमा". Card tilts −4°.
Scene 3 (2.2–3.9s): @2.33 "रबी" — a second card slides in lower-right third, tilted +4°: "रबी" + emerald-dot; chip "अलग तारीख़" pops @3.15 "तारीख़". A hairline dashed gap line between the cards stretches apart as they drift away from each other (the split).
Scene 4 (3.9–6.13s): @3.99 "और हर बार" — small ghost calculation fragments (₹ … + … = ?) in faint #94a3b8 scatter in around the cards (3–5 pieces, staggered to @4.23/@4.45/@4.72); @4.96 "हिसाब" — a large ink "?" (Heebo 900) punches in centred between the cards, scale 0.6→1 with a subtle overshoot. Hold.

## Frame 2 — Four big changes

- scene: the split resolves — a ramp arc sweeps in and a big "४" lands with "बड़े बदलाव", scheme name above
- voiceover: "अब यह सब बदल गया है। शून्य प्रतिशत ब्याज फसल ऋण योजना में — चार बड़े बदलाव।"
- duration: 7.94s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/02-four-changes.html
- type: product_intro
- persuasion: Frame-then-fill (announce the shape: four changes) + signposting
- beat: relief + anticipation
- blueprint: titlecard-reveal (Adapt)
- focal: a giant "4" (Heebo 900, teal→emerald ramp fill) inside a drawn ramp ring
- roles: large circle swell (mint, off left edge) = background · scheme-name pill = supporting · "4" + ring = foreground
- sfx: whoosh-soft, chime

narrativeRole: Names the news and promises its structure, so the viewer knows what's coming.
keyMessage: The zero-percent crop-loan scheme has four big changes.

Adapt: keep one clean title with one restrained move; add a ring draw-on as the signature landing.
Scene 1 (0.0–2.1s): @0.30 "अब यह सब" — headline "अब सब बदल गया है" rises word-by-word (per-word reveal on @0.30/@0.83/@1.06) at y≈360, h1 ink. A huge mint circle swell slides in from the left edge behind.
Scene 2 (2.1–5.9s): @2.32 "शून्य प्रतिशत" — a big "0%" (Heebo 900, ink, ~220px) pops at y≈640 with the label under it building on cue: "शून्य प्रतिशत ब्याज" (@2.32–@3.65) then "फसल ऋण योजना" (@4.06–@5.04) as a white pill card.
Scene 3 (5.9–7.94s): @6.11 "चार" — the 0% block lifts and fades up; a ramp ring (sky→emerald gradient stroke, ~520px) draws on around y≈980 and a giant "४" (Devanagari numeral, Heebo/Noto 900, teal) counts/lands inside it on @6.11; @6.70 "बदलाव" — label "बड़े बदलाव" (h1) slides up beneath the ring. Four small dots around the ring pop in sequence (quarter marks). Hold still.

## Frame 3 — One limit for the whole year

- scene: two season bars (खरीफ़ / रबी) merge into one long ramp bar labelled "पूरे साल · एक साख सीमा", then splits into cash + kind sub-limits inside it
- voiceover: "पहला बदलाव — खरीफ़ और रबी, दोनों के लिए अब पूरे साल की एक ही साख सीमा। नकद और वस्तु ऋण, दोनों इसी के अंदर।"
- duration: 10.78s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/03-one-limit.html
- type: feature_showcase
- persuasion: Before/after merge (concretization)
- beat: "aha"
- blueprint: compose
- focal: the merging bar
- roles: 12-month ruler (jan…dec ticks, faint) = supporting · two season segments → one ramp bar = foreground · white card holding the bar = midground · sky circle swell top-right = background
- sfx: whoosh-soft, pop

narrativeRole: Makes "single annual limit" visible as two pieces becoming one.
keyMessage: One credit limit now covers the whole year — Kharif and Rabi together.

Scene 1 (0.0–1.5s): chrome + chip "बदलाव १ / ४" (ring 1/4 filled). @0.30 "पहला बदलाव" — eyebrow "पहला बदलाव" (label, muted) then headline slot empty.
Scene 2 (1.5–4.0s): inside a large white card (y≈560–1180): @1.59 "खरीफ़" — a sky segment bar labelled "खरीफ़" grows in on the left half; @2.40 "रबी" — an emerald segment labelled "रबी" grows on the right half, with a visible GAP between them (old world). A faint 12-tick month ruler sits under the bars.
Scene 3 (4.0–6.6s): @4.35 "पूरे साल" — the gap closes: both segments slide together and fuse into ONE continuous ramp-gradient bar spanning the ruler (signature merge); @5.32 "एक ही" — headline "पूरे साल की एक साख सीमा" (h2, ink) rises above the card at y≈420; pop sfx on fuse.
Scene 4 (6.6–10.78s): @7.02 "नकद" — the bar gains an inner divider; left portion labelled "नकद" chip; @7.63 "वस्तु" — right portion chip "वस्तु" (kind: seeds/fertiliser icon-less, just the word). @8.69 "दोनों इसी के अंदर" — a thin bracket arcs over both chips joining them under the single bar label "एक सीमा". Hold.

## Frame 4 — Due date: 12 months

- scene: a circular 12-segment dial; a marker at "पहली निकासी" and the ring fills clockwise to "12 माह"
- voiceover: "और चुकाने की तारीख़? पहली बार ऋण लेने के दिन से — पूरे बारह महीने।"
- duration: 6.56s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/04-due-date.html
- type: feature_showcase
- persuasion: Question→answer pairing + demonstration
- beat: clarity
- blueprint: dataviz-countup (Adapt)
- focal: 12-segment ring dial with counting centre numeral
- roles: dial = foreground · question headline = supporting · emerald swell bottom-left = background
- sfx: tick

narrativeRole: Pins the new due-date rule to one concrete picture — the clock starts at the first drawal.
keyMessage: Repayment is due 12 months from the day of the first drawal.

Adapt: keep the count-up ring signature; the ring is 12 month-segments.
Scene 1 (0.0–1.8s): chip "बदलाव १ / ४" stays. @0.30 "और चुकाने की तारीख़?" — question headline "चुकाने की तारीख़?" (h1) rises at y≈330.
Scene 2 (1.8–4.4s): @1.92 "पहली बार" — a 12-segment ring (~620px, faint segments) draws in at y≈880; a teal pin/marker drops at 12 o'clock labelled "पहली निकासी" (pill) @2.92 "ऋण लेने" ; @3.69 "दिन से" — the pin pulses once.
Scene 3 (4.4–6.56s): @4.59 "पूरे" — the ring segments fill clockwise with the ramp gradient (tick sfx per few segments) while a centre numeral counts 0→12 (Heebo 900) landing exactly on @4.96 "बारह"; @5.36 "महीने" — "माह" label under the numeral. Hold.

## Frame 5 — Apply online, auto-filled

- scene: a phone-shaped rounded card with an application form; fields fill themselves from two sources: Samagra ID (KYC) and Bhu-Abhilekh (land)
- voiceover: "दूसरा बदलाव — नया किसान क्रेडिट कार्ड, अब पूरी तरह ऑनलाइन। समग्र आईडी से केवाईसी, और भू-अभिलेख से ज़मीन की जानकारी — अपने आप।"
- duration: 13.23s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/05-online.html
- type: feature_showcase
- persuasion: Demonstration (show the mechanism running) + causal chain
- beat: delight
- blueprint: device-surface-showcase (Adapt)
- focal: a simplified phone/app card "नया KCC आवेदन"
- roles: phone card = foreground · two source badges (समग्र ID, भू-अभिलेख) = supporting · halftone swell behind phone = background
- sfx: whoosh-soft, pop, pop, chime

narrativeRole: Shows that the application now fills itself from government records — no paperwork run-around.
keyMessage: New KCC applications are fully online; KYC and land details auto-fill from Samagra ID and land records.

Adapt: keep "a device surface held as hero while its screen changes state"; no cursor, no real app — a clean invented form.
Scene 1 (0.0–1.8s): chip "बदलाव २ / ४". @0.30 "दूसरा बदलाव" — eyebrow. A soft halftone dot-disc (sky→teal) blooms behind centre.
Scene 2 (1.8–5.8s): @1.86 "नया किसान क्रेडिट कार्ड" — a tall rounded phone card (≈560×900, white, 56px radius, shadow float) rises to y≈560–1460 with title "नया KCC आवेदन" and 4 empty field rows (नाम, KYC, ज़मीन, फसल). @4.79 "ऑनलाइन" — a pill "100% ऑनलाइन" with a green check pops above the phone (y≈420).
Scene 3 (5.8–8.6s): @6.43 "समग्र आईडी" — a sky badge "समग्र ID" slides in from the left edge; a dotted arc (circle-struck) draws from badge to the KYC row; @7.68 "केवाईसी" — the KYC row fills with a check and "सत्यापित".
Scene 4 (8.6–13.23s): @8.92 "भू-अभिलेख" — an emerald badge "भू-अभिलेख" slides in from the right; arc draws to the ज़मीन row; @10.06 "ज़मीन की जानकारी" — ज़मीन row fills ("खसरा ✓"); @11.84 "अपने आप" — all filled rows glint with a single light sweep across the phone, and a pill "अपने आप" pops at bottom of phone. Hold.

## Frame 6 — Limit calculated automatically, up to ₹3 lakh

- scene: two inputs (फसल, रकबा) feed a gauge that counts up to ₹3,00,000 — the max
- voiceover: "फसल और रकबा भरिए — साख सीमा ख़ुद गिनी जाएगी। अधिकतम, तीन लाख रुपये तक।"
- duration: 7.72s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/06-auto-limit.html
- type: social_proof
- persuasion: Worked example with real numbers (the cap) + count-up
- beat: confidence
- blueprint: dataviz-countup (Reproduce)
- focal: semicircle gauge with ₹ count-up
- roles: gauge = foreground · two input chips = supporting · paper-2 circle swell = background
- sfx: tick, chime

narrativeRole: Turns "limit auto-calculated per the SLTC scale of finance" into one satisfying number.
keyMessage: Enter crop and area — the limit computes itself, up to a maximum of ₹3 lakh.

Scene 1 (0.0–2.2s): chip "बदलाव २ / ४". @0.30 "फसल" — chip "फसल: गेहूँ" pops at y≈380 left; @1.03 "रकबा" — chip "रकबा: हेक्टेयर" pops right; thin arcs from both chips converge downward.
Scene 2 (2.2–4.7s): @2.28 "साख सीमा" — a large semicircle gauge (~760px wide) draws on at y≈760–1180 (faint track); @3.20 "ख़ुद गिनी जाएगी" — the gauge arc fills with ramp gradient; centre ₹ number counts up from ₹0 (Heebo 900, ink, Indian digit grouping ₹ 1,20,000…).
Scene 3 (4.7–7.72s): @4.82 "अधिकतम" — a teal tick mark + label "अधिकतम" appears at the gauge's end; the count continues and lands at "₹ 3,00,000" exactly on @6.07 "लाख" (arc reaches the end); @6.36 "रुपये तक" — caption line "तीन लाख रुपये तक" (h2) rises under the gauge; chime. Small note "SLTC ऋणमान के अनुसार" (label, muted). Hold.

## Frame 7 — Approval path: PACS → Board → Bank branch → Download

- scene: a vertical 4-step path; each node lights as it's named; ends in a downloadable approval letter card
- voiceover: "फिर पैक्स जाँच करेगी, संचालक मंडल अनुशंसा करेगा, और ज़िला बैंक शाखा स्वीकृति देगी। स्वीकृति पत्र — सीधे लॉगिन से डाउनलोड।"
- duration: 11.29s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/07-approval-path.html
- type: feature_showcase
- persuasion: Signposting (first… then… finally) + causal chain
- beat: momentum
- blueprint: compose
- focal: the vertical node path
- roles: step nodes + connecting ramp line = foreground · letter card = foreground payoff · sky swell = background
- sfx: pop, pop, pop, chime

narrativeRole: Shows who does what after the farmer applies, so nobody wonders where the file is.
keyMessage: PACS verifies, the board recommends, the DCCB branch approves — and the approval is downloaded from the login.

Scene 1 (0.0–2.0s): chip "बदलाव २ / ४". A vertical spine line (faint) at x≈230 from y≈330 to y≈1250. @0.66 "पैक्स" — node 1 (ring ◯ with Heebo "1") pops; label "पैक्स" (h2) + sub "जाँच" (@1.00) to its right.
Scene 2 (2.0–4.5s): @2.13 "संचालक मंडल" — ramp line draws down to node 2; node pops; label "संचालक मंडल" + sub "अनुशंसा" (@3.14).
Scene 3 (4.5–7.5s): @5.04 "ज़िला बैंक शाखा" — line draws to node 3; label "ज़िला बैंक शाखा"; @6.35 "स्वीकृति" — a teal check badge stamps onto node 3 (sub "स्वीकृति").
Scene 4 (7.5–11.29s): @7.63 "स्वीकृति पत्र" — a white letter card ("KCC स्वीकृति पत्र", faux lines, NO emblem) slides up at y≈1080–1420 on the right; @8.96 "सीधे लॉगिन से" — three small login pills appear under it: "किसान · पैक्स · शाखा"; @10.01 "डाउनलोड" — a download arrow in a sky circle drops into the card corner with a bounce. Hold.

## Frame 8 — Valid for 5 years

- scene: five year-blocks in a row light up one after another; "हर साल नया आवेदन" gets struck through
- voiceover: "तीसरा बदलाव — ऑनलाइन केसीसी अब पाँच साल के लिए मान्य। ज़मीन या फसल न बदले, तो हर साल नया आवेदन नहीं।"
- duration: 11.56s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/08-five-years.html
- type: feature_showcase
- persuasion: Count-up + contrast (strike-through the old chore)
- beat: relief
- blueprint: grid-card-assemble (Adapt)
- focal: giant "5" with five year tiles
- roles: giant numeral "5 वर्ष" = foreground · five year tiles = foreground · struck-through old line = supporting · halftone field band = background
- sfx: tick, pop

narrativeRole: Makes validity tangible — one approval, five seasons of use.
keyMessage: Online KCC approval is valid for five years; no fresh application each year unless land or crop changes.

Adapt: keep the staggered cascade of N items; N = five year tiles.
Scene 1 (0.0–3.5s): chip "बदलाव ३ / ४". @0.30 "तीसरा बदलाव" eyebrow. @1.93 "ऑनलाइन केसीसी" — a small KCC card (rounded, ramp stripe, "KCC" in Heebo) floats in at y≈330.
Scene 2 (3.5–6.0s): @3.84 "पाँच" — giant "5" (Heebo 900, ~380px, teal) counts 1→5 landing on @3.84–@4.19 at y≈700 with "वर्ष" beside it; @4.19 "साल" — five rounded year tiles (2026-27 … 2030-31) cascade in a row/2-row grid at y≈1000–1200, each lighting with ramp tint in sequence; @5.12 "मान्य" — pill "मान्य ✓" pops.
Scene 3 (6.0–11.56s): @6.24 "ज़मीन या फसल न बदले" — a line "ज़मीन / फसल में बदलाव नहीं?" (body) appears at y≈1300; @8.66 "हर साल नया आवेदन" — a card "हर साल नया आवेदन" appears at y≈1420 then @10.45 "नहीं" — a teal strike-through line draws across it and a small "ज़रूरत नहीं" chip pops. Hold.

## Frame 9 — Interest terms 2026-27

- scene: three stat cards stack up: base rate 9.75%, 1.25% subvention for all, +4% incentive for on-time repayment
- voiceover: "चौथा बदलाव — ब्याज की शर्तें। इस साल बेस रेट, नौ दशमलव सात पाँच प्रतिशत। हर किसान को सवा प्रतिशत ब्याज अनुदान… और समय पर चुकाने वालों को, चार प्रतिशत अतिरिक्त प्रोत्साहन।"
- duration: 19.29s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/09-interest-terms.html
- type: social_proof
- persuasion: Statistical proof + build-up (three stats, rule of three)
- beat: conviction
- blueprint: dataviz-countup (Adapt)
- focal: three stacked stat cards, each with a count-up numeral
- roles: stat cards = foreground · ramp side-bars on each card = supporting · large paper-2 circle swell = background
- sfx: tick, tick, chime

narrativeRole: Lays out the year's interest terms from the government order — the numbers farmers will be asked about.
keyMessage: For 2026-27 the base rate is 9.75%; every farmer gets 1.25% subvention, and on-time repayers get a further 4% incentive.

Adapt: keep count-up landing on the hero metric; three metrics stacked vertically, the third is the hero.
Scene 1 (0.0–4.5s): chip "बदलाव ४ / ४" (ring full). @0.30 "चौथा बदलाव" eyebrow; @2.68 "ब्याज की शर्तें" — headline "ब्याज की शर्तें" (h1) at y≈300, sub "वर्ष 2026-27" (label) under it @4.62 "इस साल".
Scene 2 (4.5–9.4s): @5.61 "बेस रेट" — card A (y≈500–760) slides in: left label "बेस रेट"; @6.74 "नौ दशमलव" — numeral counts 0.00 → 9.75 landing on @8.59 "प्रतिशत" as "9.75%" (Heebo 900, ink).
Scene 3 (9.4–13.5s): @9.84 "हर किसान को" — card B (y≈800–1060): label "सभी किसानों को · ब्याज अनुदान"; @10.81 "सवा प्रतिशत" — numeral "1.25%" counts in, landing on @11.20; a sky side-bar on the card fills.
Scene 4 (13.5–19.29s): @14.22 "समय पर चुकाने वालों को" — card C (y≈1100–1400, the hero: slightly larger, mint wash, emerald side-bar, soft float shadow) slides in with label "समय पर चुकाने पर · अतिरिक्त प्रोत्साहन"; @16.12 "चार प्रतिशत" — "+4%" (teal, largest numeral) counts in landing on @16.46; @17.81 "प्रोत्साहन" — a small calendar-check chip "देय तिथि तक चुकाएँ" pops; chime. Hold ~1.2s.

## Frame 10 — Fine print: minimum land 0.10 ha

- scene: a land-parcel square with a scale bar; label "कम से कम 0.10 हेक्टेयर"
- voiceover: "ध्यान रहे — नए केसीसी के लिए, कम से कम शून्य दशमलव एक हेक्टेयर ज़मीन ज़रूरी है।"
- duration: 7.59s
- transition_in: push-slide UP
- status: animated
- src: compositions/frames/10-min-land.html
- type: benefit_highlight
- persuasion: Concretization (show the plot)
- beat: focus
- blueprint: titlecard-reveal (Adapt)
- focal: a halftone field-plot square (furrows in emerald dots) with "0.10 ha"
- roles: plot = foreground · "ध्यान रहे" pill = supporting · sky swell = background
- sfx: pop

narrativeRole: Gives the one eligibility condition a farmer must check before applying.
keyMessage: A new KCC needs at least 0.10 hectare of land.

Scene 1 (0.0–2.6s): no change chip (fine-print beat). @0.30 "ध्यान रहे" — amber-free: a sky-outlined pill "ध्यान रहे" with an ⓘ-style ring pops at y≈360; @1.58 "नए केसीसी के लिए" — headline "नए KCC के लिए" (h2) rises.
Scene 2 (2.6–7.59s): @2.70 "कम से कम" — a square plot (~560px, rounded 28px) built from halftone furrow dots (emerald→teal) blooms at y≈560–1120; dimension brackets draw on two sides; @3.63 "शून्य दशमलव एक" — "0.10" counts in large on the plot (Heebo 900, ink on a white pill) landing @4.75; @5.03 "हेक्टेयर" — "हेक्टेयर" label; @6.14 "ज़रूरी" — line "न्यूनतम भूमि आवश्यक" (body) under the plot. Hold.

## Frame 11 — Repay on time, get the full benefit

- scene: a recap stack of four tiny chips (एक सीमा · ऑनलाइन · 5 वर्ष · +4%) collapses into a calendar-check; then a PACS counter card "अपनी पैक्स समिति से मिलिए"
- voiceover: "तो समय पर चुकाइए, और योजना का पूरा लाभ उठाइए। ज़्यादा जानकारी के लिए — अपनी पैक्स समिति से मिलिए।"
- duration: 11.31s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/11-cta.html
- type: cta
- persuasion: Callback (recap the four) + distillation
- beat: resolve
- blueprint: kinetic-type-beats (Adapt)
- focal: headline "समय पर चुकाइए" with a calendar-check mark
- roles: recap chips = supporting · headline + check = foreground · big halftone dawn (sun rising over furrows, lower 50%) = background
- sfx: whoosh-soft, chime

narrativeRole: Turns the rules into one action and one place to go.
keyMessage: Repay on time to get the scheme's full benefit; ask your PACS for details.

Scene 1 (0.0–2.5s): the signature halftone "dawn over furrowed fields" blooms in the lower half (sun of full dots rising behind the horizon, sky→teal above, teal→emerald furrows below, dim ~55%). @0.98 "समय पर" — headline "समय पर चुकाइए" (display, ink) builds per-word at y≈420 with a teal calendar-check glyph (circle-struck) drawing on at @1.57.
Scene 2 (2.5–5.9s): @3.21 "योजना का पूरा लाभ" — four recap chips (एक सीमा · ऑनलाइन · 5 वर्ष · +4%) pop in a 2×2 at y≈640–860 in stagger to @4.18/@4.59; @4.91 "उठाइए" — the chips gently pull together and a sub-headline "पूरा लाभ उठाइए" (h2) lands. The sun rises slightly (≤40px) across the frame.
Scene 3 (5.9–11.31s): @6.00 "ज़्यादा जानकारी के लिए" — a white card (y≈1080–1380) slides up: small label "ज़्यादा जानकारी के लिए"; @8.51 "पैक्स समिति" — big "अपनी पैक्स समिति से मिलिए" (h2) in the card with the two-heads dots (sky+emerald) at its left. Hold.

## Frame 12 — SahkarAI sting

- scene: the two heads (sky & emerald) ride their ribbon arcs and cross, resolving into the SahkarAI lockup; tagline below
- voiceover: "सहकार ए आई — नियम, आपकी भाषा में।"
- duration: 6.95s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/12-sahkarai-sting.html
- type: branding
- persuasion: Distillation (brand promise in one line)
- beat: satisfaction
- blueprint: logo-assemble-lockup (Adapt)
- focal: SahkarAI mark (two ribbons + two heads) and wordmark
- roles: mark = foreground · wordmark + tagline = foreground · soft paper-2 double circle swell = background · source line = supporting
- sfx: whoosh-soft, chime

narrativeRole: Signs the explainer and states the brand's promise.
keyMessage: SahkarAI explains the rules in your language.

Adapt: keep "the mark comes to exist" — ribbon strokes draw on (stroke-dashoffset) with the heads riding their ends, crossing in the middle, then settle.
Scene 1 (0.0–2.0s): @0.30 "सहकार" — the two ribbon paths of the mark draw on from their outer ends toward the crossover (ramp gradient stroke, round caps); the sky and emerald heads pop onto the ribbon tips @0.98/@1.19 ("ए आई").
Scene 2 (2.0–3.9s): wordmark "SahkarAI" (Heebo 900, ink, "AI" in teal allowed at this size) rises under the mark; @2.05 "नियम" — tagline "नियम, आपकी भाषा में" (h2, ink) per-word reveal on @2.05/@2.72/@3.10/@3.48.
Scene 3 (3.9–6.95s): a hairline and tiny source line fades in at y≈1480: "स्रोत: आयुक्त सहकारिता, म.प्र. — परिपत्र क्र. 1458/2026" (label, muted). Hold still to the end; last 0.5s fade the whole frame to paper.
