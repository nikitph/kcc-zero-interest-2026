import json,re,sys
proj=sys.argv[1]
g=json.load(open(f"{proj}/caption_groups.json"))
words=[(x["frame"],w) for x in g["groups"] for w in x["words"]]
groups=[];cur=[];cf=None
def flush():
    global cur
    if cur: groups.append((cf,cur)); cur=[]
for k,(f,w) in enumerate(words):
    nxt=words[k+1][1]["text"] if k+1<len(words) and words[k+1][0]==f else ""
    if cf is not None and f!=cf: flush()
    cf=f; cur.append(dict(w))
    t=w["text"]; chars=sum(len(x["text"]) for x in cur)
    if (re.search(r"[।?…!]$",t)) or (t.endswith(",") and len(cur)>=2) or ((len(cur)>=5 or chars>=26) and not re.search(r'[।?…!]$',nxt)): flush()
flush()
out=[]
for i,(f,ws) in enumerate(groups):
    for j,w in enumerate(ws): w["id"]=f"caption-word-{i}-{j}"
    out.append({"id":f"caption-group-{i}","frame":f,"start":ws[0]["start"],"end":ws[-1]["end"],"text":" ".join(w["text"] for w in ws),"words":ws})
g["groups"]=out; json.dump(g,open(f"{proj}/caption_groups.json","w"),ensure_ascii=False,indent=1)
h=open(f"{proj}/compositions/captions.html").read()
a=h.index("var GROUPS = ")+len("var GROUPS = "); b=h.index(";\n",a)
h=h[:a]+json.dumps(out,ensure_ascii=False,separators=(",",":"))+h[b:]
open(f"{proj}/compositions/captions.html","w").write(h)
print(len(out),"groups"); print(" | ".join(x["text"] for x in out[:14]))
