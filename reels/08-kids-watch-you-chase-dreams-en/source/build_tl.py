import json,re
segs=json.load(open('main_en.json'))
OFF=[(173.25,215.18,0.0),(252.52,288.15,1259/30),(144.96,157.42,(1259+1069)/30)]
def m(t):
    for a,b,o in OFF:
        if a-0.05<=t<=b+0.05: return round(min(max(t,a),b)-a+o,2)
words=[]
for s in segs:
    for a,b,w in s['w']:
        w=w.strip()
        if not any(x-0.05<=a<y-0.02 for x,y,_ in OFF): continue
        words.append([w,m(a),m(b) if m(b) is not None else m(a)+0.3])
words.sort(key=lambda x:x[1])
fix={'Building':'building','on':'on'}
out=[]
for i,(w,a,b) in enumerate(words):
    if w=='on' and i>0 and words[i-1][0]=='give': w='up on'
    out.append([fix.get(w,w),a,b])
# hook = first sentence (ends at 'theirs.')
he=[x for x in out if x[0].startswith('theirs')][0][2]+0.1
caps=[]
for i,(w,a,b) in enumerate(out):
    if a<he: continue
    nxt=out[i+1][1] if i+1<len(out) else b+0.6
    caps.append([w,a,round(min(max(b,a+0.22),nxt if nxt-b<0.6 else b+0.35),2)])
DUR=2702/30
key=['crazy','confident,','scared,','scratch,','hard','actually','powerful','example','possible','dreams','kids']
punch=[0.0,he]+[c[1] for c in caps if c[0] in ('crazy','scratch','scratch,','actually','powerful','example','theirs')]
segst=[]
for c in caps:
    if not segst or c[1]-segst[-1]>=3.0: segst.append(c[1])
json.dump({'caps':caps,'sec':[[p,p+1,'x','',0] for p in punch],'segst':segst,'dur':DUR,'hook_end':round(he,2)},open('fx/timeline.json','w'))
print(he,DUR,len(caps)); print(' '.join(c[0] for c in caps))
