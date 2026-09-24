# SahkarAI explains — शून्य प्रतिशत ब्याज फसल ऋण योजना (MP, 2026-27)

A 2:00, 1080×1920 Hindi explainer of MP Commissioner Cooperation circular क्र. 1458/2026 and the attached
GoMP order F 12-01/2020/15-1 (30.06.2026): the new online Kisan Credit Card process, one annual credit
limit with a 12-month due date, 5-year validity, and the 2026-27 interest terms.

Built with [HyperFrames](https://hyperframes.heygen.com) (faceless-explainer workflow). Brand: SahkarAI
ramp on paper, Noto Sans Devanagari + Heebo (vendored in `assets/fonts/`).

## Layout

| Path | What |
| --- | --- |
| `BRIEF.md`, `STORYBOARD.md`, `SCRIPT.md` | intent, frame-by-frame plan (scene windows keyed to word timestamps), locked narration |
| `frame.md` | design spec |
| `compositions/frames/NN-*.html` | the 12 frames · `compositions/captions.html` karaoke captions |
| `index.html` | assembled root composition |
| `assets/vo/` | ElevenLabs narration (voice "Devi", `MF4J4IDTRo0AxOO4dpFR`, eleven_multilingual_v2) + per-word timings |
| `assets/audio/` | BGM + SFX (HeyGen audio library) |
| `audio_meta.json` | voice / BGM / SFX placement consumed by the assembler |

## Rebuild

```bash
# narration (only if SCRIPT.md changes) — key via env, never committed
ELEVENLABS_API_KEY=... python3 scripts/elevenlabs-tts.py MF4J4IDTRo0AxOO4dpFR .
# then re-run the 1.08× tempo + padding step and audio_meta.json (see git history), and:
npx hyperframes check
npx hyperframes preview --background
npx hyperframes render --quality high --output renders/video.mp4
ffmpeg -i renders/video.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k -movflags +faststart renders/kcc-shunya-byaj-2026-hi.mp4
```

After rebuilding captions (`captions.mjs build`), run `python3 scripts/regroup-captions.py .` to regroup
them into Hindi phrase-sized groups.

Renders are not committed (`renders/` is git-ignored).
