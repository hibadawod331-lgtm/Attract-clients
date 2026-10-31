import json, re
segs=json.load(open("cv3.json",encoding="utf-8"))
FIX=["لو معي مهارة وحدة و30 يوم بس وهدفي حولها لبزنس يجيبلي 10 آلاف دولار بالشهر",
"هاد بالضبط اللي رح ركز عليه",
"من اليوم الأول لليوم التالت رح حدد شو الشي اللي أنا فعلاً شاطرة فيه",
"مو بس شو بحب أعمل",
"شو الشي اللي فعلاً فيني ساعد حدا يصير أحسن فيه",
"من اليوم الرابع لليوم السابع رح دور على الشخص اللي عنده مشكلة واضحة بهالمجال",
"لأنه بالنهاية ما بدي إني ابني عرضي على الشي اللي بس أنا بعرفه",
"بدي ابنيه على المشكلة اللي الناس مستعدة تدفع لتخلص منها",
"من اليوم التامن للعاشر رح حول هالمشكلة لنتيجة واضحة",
"يعني ما رح قول أنا بعلمك كيف تعملي سوشيال ميديا",
"لأ بقول أنا بساعدك تحولي صفحتك على الإنستغرام لمصدر دخل مستمر",
"ويحولك المتابعين لعملاء",
"من اليوم 11 لليوم 13 اختبري فكرتك قبل ما تعرضيها على السوق",
"بدنا نتأكد إذا الجمهور فعلاً بدو النتيجة ومستعد يدفع كرمالها",
"من اليوم 14 لليوم 20 رح ابني العرض حوالين النتيجة",
"وسعر العرض اللي ما رح حدده على عدد الساعات اللي رح قضيها مع العميل",
"بل رح حدده على قيمة النتيجة اللي عم ساعده يوصلها",
"من اليوم 21 لليوم 30 رح بلش بالبيع",
"رح بلش أعمل محتوى عن المشكلة رح احكي مع الناس اللي عندهم هالمشكلة",
"واسمع اعتراضاتهم وببلش طور بالعرض تبعي",
"بس أعرف فعلاً إذا بدهم يشتروا لأنه أكبر غلطة ممكن تعمليها",
"إنك تقضي 6 شهور تبني شي وبعدين تكتشفي إنه ما حدا بدو يشتري",
"بدك مهارة مشكلة واضحة نتيجة الناس فعلاً بترغب فيها عرض قوي الناس بسعادة تدفع كرماله",
"وهيك بتحولي أي مهارة عندك لبزنس حقيقي"]
assert len(FIX)==len(segs)
strip=lambda s: re.sub("[ً-ْٰ]","",s)
def ts(t):
    h=int(t//3600); m=int(t%3600//60); s=t%60
    return f"{h}:{m:02d}:{s:05.2f}"
words=[]
for seg,txt in zip(segs,FIX):
    ws=strip(txt).split(); ww=seg["words"]
    if len(ww)==len(ws):
        tm=[(w["s"],w["e"]) for w in ww]
    else:
        a=ww[0]["s"] if ww else seg["start"]; b=ww[-1]["e"] if ww else seg["end"]
        L=[len(w)+1 for w in ws]; tot=sum(L); acc=a; tm=[]
        for l in L: d=(b-a)*l/tot; tm.append((acc,acc+d)); acc+=d
    words+= [(w,s,e) for w,(s,e) in zip(ws,tm)]
# chunk: merge short words with the next one, max 2 words
SHORT={"من","رح","شو","بس","مو","ما","لو","و","على","عن","اللي","لأ","بل","أنا","إني","مع","عم","إذا","أي","10","6"}
chunks=[];i=0
while i<len(words):
    w,s,e=words[i]
    if (w in SHORT or len(w)<=2) and i+1<len(words) and words[i+1][1]-e<0.35:
        w2,s2,e2=words[i+1]; chunks.append((w+" "+w2,s,e2)); i+=2
    else: chunks.append((w,s,e)); i+=1
H="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,IBM Plex Sans Arabic,88,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,5,3,2,60,60,945,1
Style: Lab,IBM Plex Sans Arabic,46,&H007AC2E8,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,3,2,8,60,60,175,1
Style: Ttl,El Messiri,74,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,4,3,8,60,60,240,1
Style: Hdl,IBM Plex Sans Arabic,30,&H40FFFFFF,&H00FFFFFF,&H00000000,&H96000000,1,0,0,0,100,100,0,0,1,2,1,4,50,50,0,1
Style: End,El Messiri,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,0,0,5,60,60,0,1
Style: Box,IBM Plex Sans Arabic,10,&H50000000,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ev=[]
for k,(w,s,e) in enumerate(chunks):
    nxt=chunks[k+1][1] if k+1<len(chunks) else e+0.4
    end=min(max(e,s+0.18),nxt) if nxt-e<0.6 else e+0.15
    ev.append(f"Dialogue: 2,{ts(s)},{ts(end)},Cap,,0,0,0,,{{\\fscx80\\fscy80\\t(0,90,\\fscx100\\fscy100)}}{w}")
S=lambda i: segs[i]["start"]; E=lambda i: segs[i]["end"]
SECT=[(0,1,"مهارة وحدة · 30 يوم","كيف بحولها لبزنس 10,000$ بالشهر؟"),
      (2,4,"اليوم 1 – 3","اكتشفي مهارتك"),
      (5,7,"اليوم 4 – 7","لاقي الشخص اللي عنده المشكلة"),
      (8,11,"اليوم 8 – 10","حولي المشكلة لنتيجة واضحة"),
      (12,13,"اليوم 11 – 13","اختبري فكرتك"),
      (14,16,"اليوم 14 – 20","ابني العرض"),
      (17,21,"اليوم 21 – 30","ابلشي بالبيع"),
      (22,23,"المعادلة","مهارة + مشكلة + نتيجة + عرض")]
for a,b,lab,ttl in SECT:
    st=0 if a==0 else S(a)-0.1; en=(S(b+1)-0.1) if b+1<len(segs) else E(b)
    ev.append(f"Dialogue: 1,{ts(st)},{ts(en)},Lab,,0,0,0,,{{\\fad(250,150)}}{lab}")
    ev.append(f"Dialogue: 1,{ts(st)},{ts(en)},Ttl,,0,0,0,,{{\\fad(250,150)}}{ttl}")
T=105.89
ev.append(f"Dialogue: 0,{ts(0)},{ts(T)},Hdl,,0,0,0,,{{\\pos(50,1000)}}@itscoachhiba")
ev.append(f"Dialogue: 3,{ts(T)},{ts(T+1.8)},Box,,0,0,0,,{{\\fad(300,0)\\p1}}m 0 0 l 1080 0 1080 1920 0 1920{{\\p0}}")
ev.append(f"Dialogue: 4,{ts(T+0.15)},{ts(T+1.8)},End,,0,0,0,,{{\\fad(300,0)}}@itscoachhiba")
open("reel.ass","w",encoding="utf-8").write(H+"\n".join(ev)+"\n")
print(len(chunks),"caption chunks")
