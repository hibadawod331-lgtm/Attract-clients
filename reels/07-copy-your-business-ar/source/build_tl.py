import json
segs=json.load(open('main.json'))
OFF=[(113.80,154.82,0.0),(168.12,181.45,1231/30)]
def m(t):
    for a,b,o in OFF:
        if a-0.05<=t<=b+0.4: return round(min(max(t,a),b)-a+o,2)
fix={'سبعك':'تبعك','يبيعو':'يبيعوا','يقدمو':'يقدموا','يستخدمو':'يستخدموا','ولي':'واللي','انتي':'إنتي','انتِ':'إنتي','وهم':'وهون','البرسنال':'البرسونال',
     'تأدمي':'تقدمي','بالزات':'بالذات','بالذات؟':'بالذات','دائماً':'دايما','الأرخص':'الأرخص'}
words=[]
for s in segs:
    for a,b,w in s['w']:
        w=w.strip()
        if m(a) is None or m(b) is None: continue
        words.append([fix.get(w,w),m(a),m(b)])
HOOK_END=m(122.78)
caps=[]
for i,(w,a,b) in enumerate(words):
    if a<HOOK_END: continue
    nxt=words[i+1][1] if i+1<len(words) else b+0.6
    caps.append([w,a,round(min(max(b,a+0.25),nxt if nxt-b<0.6 else b+0.35),2)])
DUR=1631/30
punch=[0.0,HOOK_END,m(127.88),m(136.88),m(168.12),m(176.32),m(178.70)]
sec=[[0,HOOK_END,'hook','',0]]+[[HOOK_END,DUR,'body','',0]]
segst=[]
for s in segs:
    t=m(s['w'][0][0])
    if t is not None and (not segst or t-segst[-1]>=3.0): segst.append(t)
json.dump({'caps':caps,'sec':[[p,p+1,'x','',0] for p in punch],'secs':sec,'segst':segst,'dur':DUR,'hook_end':HOOK_END},open('fx/timeline.json','w'),ensure_ascii=False)
print(len(caps),HOOK_END,DUR); print(' '.join(c[0] for c in caps))
