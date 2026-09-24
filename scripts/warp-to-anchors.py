"""Time-warp a re-voiced take so chosen anchor words land where the original take's did.

usage: warp-to-anchors.py NEW.json NEW.mp3 OLD.json OUT.mp3 word_index[,word_index...]
Piecewise atempo between anchors (pitch preserved); visuals keyed to the old timestamps stay on cue.
"""
import json, subprocess, sys
new, newaudio, old, out, idx = sys.argv[1:6]
N, O = json.load(open(new)), json.load(open(old))
assert len(N["words"]) == len(O["words"]), "word count differs"
ks = [int(i) for i in idx.split(",")]
nb = [0.0] + [N["words"][k]["start"] for k in ks] + [N["duration_s"]]
ob = [0.0] + [O["words"][k]["start"] for k in ks] + [O["duration_s"]]
parts, labels = [], []
for i in range(len(nb) - 1):
    nd, od = nb[i + 1] - nb[i], ob[i + 1] - ob[i]
    # speed up freely (<=1.6x); slow down at most to 0.92x, then fill the rest with a pause
    r = min(1.6, nd / od) if nd >= od else max(0.92, nd / od)
    pad = max(0.0, od - nd / r)
    chain = f"atempo={r:.4f}" + (f",apad=pad_dur={pad:.3f}" if pad > 0.005 else "")
    parts.append(f"[0:a]atrim={nb[i]:.3f}:{nb[i+1]:.3f},asetpts=PTS-STARTPTS,{chain},atrim=0:{od:.3f}[s{i}]")
    labels.append(f"[s{i}]")
    print(f"seg {i}: {nd:.2f}s -> {od:.2f}s (x{r:.3f} +{pad:.2f}s pause)")
fc = ";".join(parts) + ";" + "".join(labels) + f"concat=n={len(labels)}:v=0:a=1[o]"
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", newaudio, "-filter_complex", fc, "-map", "[o]", "-b:a", "192k", out], check=True)
