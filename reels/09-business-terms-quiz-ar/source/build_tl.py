import json
segs=json.load(open('main.json'))
OFF=[(39.22,58.45,0.0),(61.13,68.62,577/30)]
def m(t):
    for a,b,o in OFF:
        if a-0.05<=t<b+0.05: return round(min(max(t,a),b)-a+o,2)
T=[(42.60,'هامش الربح','Profit Margin'),(43.68,'CAC','تكلفة جذب العميلة'),(44.36,'قمع المبيعات','Sales Funnel'),
   (45.60,'Positioning','التموضع'),(46.64,'LTV','قيمة العميلة على المدى الطويل'),(47.74,'ROI','العائد على الاستثمار'),
   (48.68,'الدخل المتكرر','Recurring Revenue'),(49.94,'Conversion Rate','معدل التحويل'),(51.34,'الهوية التجارية','Brand Identity'),
   (52.78,'Client Retention','الحفاظ على العميلات'),(54.12,'Client Acquisition','جذب العميلات'),(55.72,'Unique Selling Point','الشي اللي بيميزك عن غيرك')]
cards=[]
for i,(t,ti,sub) in enumerate(T):
    a=m(t)-0.05; b=(m(T[i+1][0])-0.05) if i+1<len(T) else m(58.30)
    cards.append([round(a,2),round(b,2),i+1,ti,sub])
fix={'قدرت':'قدرتي','أدش':'قديش','انت':'إنتي','بالبزنس.':'بالبزنس','وعمد':'وعم','تبقيها':'تطبقيها','فأنتي':'فإنتي','بزنز':'بزنس'}
caps=[]
ws=[(fix.get(w.strip(),w.strip()),m(a),m(b) if m(b) is not None else None) for s in segs for a,b,w in s['w'] if m(a) is not None]
outro=m(61.10)
for i,(w,a,b) in enumerate(ws):
    if a<outro: continue
    b=b or a+0.4
    nxt=ws[i+1][1] if i+1<len(ws) else b+0.5
    caps.append([w,a,round(min(max(b,a+0.25),nxt if nxt-b<0.6 else b+0.35),2)])
DUR=802/30
hook_end=m(42.55)
punch=[0.0,outro,m(66.20)]
json.dump({'caps':caps,'cards':cards,'sec':[[p,p+1,'x','',0] for p in punch],'segst':[0.0,outro],'dur':DUR,'hook_end':hook_end,'list_end':m(58.30)},open('fx/timeline.json','w'),ensure_ascii=False)
print(hook_end,DUR); print(cards[:2]); print(' '.join(c[0] for c in caps))
