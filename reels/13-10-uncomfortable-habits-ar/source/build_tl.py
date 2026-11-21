import json
W=json.load(open('../reel13_words.json'))
FIX={'عشة':'عشرة','مومريحة':'مو مريحة','تجرأي':'تجرئي','تعتزري':'تعتذري','والايمة':'والقيمة','اثنان':'اتنين','قداش':'قديش','وقداش':'وقديش',
'ثلاثة':'تلاتة','تمدحية':'تمدحي','لقيك':'رايك','توفقك':'توافقك','الرأي':'الراي','لان':'لانو','نو':'لا','حملاء':'عملاء','شرطة':'شرط',
'اشتر':'اشطر','لحد':'لحتى','ايمة':'القيمة','بالشغلك':'بشغلك','ماحدة':'ما حدا','اربعة':'اربعة'}
words=[[FIX.get(w,w).replace('أ','ا').replace('إ','ا'),a,b] for w,a,b in W]
for i,x in enumerate(words):
    if x[0]=='الارقام' and abs(x[1]-16.16)<0.05: x[0]='ارقام'
# -> "لانو مو مجرد"
for i,(w,a,b) in enumerate(words):
    if w=='هو' and i>0 and words[i-1][0]=='لانو' and words[i+1][0]=='مجرد': words[i][0]='مو'
DUR=2259/30
T=lambda n,t:f'<bdi dir="ltr">{n}.</bdi> {t}'
sec=[[0,5.8,'hook','',4],[5.8,14.82,'p1',T(1,'تجرئي ترفعي اسعارك بدون ما تعتذري'),2],[14.82,24.0,'p2',T(2,'تفتحي ارقام البزنس تبعك'),2],
[24.0,34.26,'p3',T(3,'تتعلمي تسوقي لحالك كل يوم'),2],[34.26,42.08,'p4',T(4,'تحكي رايك حتى لو في ناس بتختلف معك'),2],
[42.08,55.22,'p5',T(5,'تاخدي المحتوى تبعك بجدية'),2],[55.22,DUR,'p6',T(5,'تاخدي المحتوى تبعك بجدية'),2]]
caps=[]
for i,(w,a,b) in enumerate(words):
    if a<5.8: continue
    nxt=words[i+1][1] if i+1<len(words) else b+0.5
    caps.append([w,a,round(nxt if nxt-b<0.6 else b+0.3,2)])
segst=[];t=0.0
for s in sec:
    t=s[0]
    while t<s[1]-1.5: segst.append(round(t,2)); t+=3.7
json.dump({'caps':caps,'sec':sec,'segst':segst,'dur':DUR},open('fx/timeline.json','w'),ensure_ascii=False)
print(' '.join(c[0] for c in caps))
