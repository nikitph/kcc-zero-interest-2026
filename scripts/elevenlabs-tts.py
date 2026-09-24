import os, re, json, base64, sys, subprocess, urllib.request
KEY=os.environ["ELEVENLABS_API_KEY"]
# Pronunciation respellings sent to TTS only; captions keep the correct spelling.
SAY={"ऋण":"रुण"}
OUTDIR=os.environ.get("VO_OUT","assets/vo"); VOICE=sys.argv[1]; proj=sys.argv[2]; only=sys.argv[3:] 
src=open(f"{proj}/SCRIPT.md",encoding="utf8").read()
lines=re.findall(r"## Line (\d+).*?\n(?:.*?\n)*?\n    (.+)\n", src)
out={}
for n,text in lines:
    n=int(n)
    if only and str(n) not in only: continue
    spoken=text
    for a,b in SAY.items(): spoken=spoken.replace(a,b)
    body=json.dumps({"text":spoken,"model_id":"eleven_multilingual_v2","language_code":"hi",
      "voice_settings":{"stability":0.5,"similarity_boost":0.8,"style":0.25,"use_speaker_boost":True}}).encode()
    req=urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}/with-timestamps?output_format=mp3_44100_128",
        data=body,headers={"xi-api-key":KEY,"Content-Type":"application/json"})
    try: r=json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e: print(n,e.read()[:300]); continue
    mp3=f"{proj}/{OUTDIR}/{n:02d}.mp3"; wav=f"{proj}/{OUTDIR}/{n:02d}.wav"
    open(mp3,"wb").write(base64.b64decode(r["audio_base64"]))
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",mp3,"-ar","44100","-ac","1",wav],check=True)
    a=r["alignment"]; ch,st,en=a["characters"],a["character_start_times_seconds"],a["character_end_times_seconds"]
    words=[];cur="";s=None;e=None
    for c,cs,ce in zip(ch,st,en):
        if c.isspace():
            if cur.strip(): words.append((cur,s,e))
            cur="";s=None
        else:
            if s is None: s=cs
            cur+=c;e=ce
    if cur.strip(): words.append((cur,s,e))
    inv={b:a for a,b in SAY.items()}
    words=[(next((w.replace(b,a) for b,a in inv.items() if b in w),w),s,e) for w,s,e in words]
    dur=float(subprocess.check_output(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",wav]).strip())
    wl=[{"id":f"w{i}","text":w,"start":round(s,3),"end":round(e,3)} for i,(w,s,e) in enumerate(words)]
    json.dump({"frame":n,"path":f"assets/vo/{n:02d}.wav","duration_s":round(dur,3),"words":wl},open(f"{proj}/{OUTDIR}/{n:02d}.json","w"),ensure_ascii=False,indent=1)
    print(n, round(dur,2), " ".join(f"{w['text']}@{w['start']:.2f}" for w in wl))
