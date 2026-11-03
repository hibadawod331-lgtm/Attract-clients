import re,sys
H,W=int(sys.argv[1]),1080
strip=lambda s: re.sub("[ً-ْٰ]","",s).replace("،","").replace(",","")
P=[("1. تكوني مهووسة إنك تكوني الخيار الأول",
    "مو بس بدك الناس تعرف إنك موجودة<br>بدك أول ما يحتاجوا الشي اللي بتقدميه يكون اسمك أول اسم يخطر ببالهم.",
    "وإذا خطر ببالهم حدا غيرك؟ معناها لسه في شغل 😅"),
   ("2. تدرسي منافسينك زيادة عن اللزوم",
    "مو لتقلديهم<br>بس لتفهمي شو عم يعملوا صح وشو ناقصهم ووين فيكي تتميزي عنهم لدرجة يصير صعب حدا ياخد مكانك.",
    "يعني ستوكينغ… بس بشكل احترافي 🕵️‍♀️"),
   ("3. تبطلي تحاولي تعجبي الكل",
    "تبطلي تخففي من آرائك أو تغيري طريقة كلامك خوفاً من إنك تزعلي حدا.<br>مو هدفك الكل يحبك<br>هدفك تكوني مميزة وما تنساكي الناس الصح.",
    "حتى البيتزا في ناس ما بتحبها… وعايشة عادي 🍕"),
   ("4. تصيري تعيدي نفس الكلام لدرجة تزهقي من حالك",
    "تحكي عن نفس رسالتك ونفس أفكارك بمية طريقة مختلفة لدرجة إنو الناس يصيروا يربطوا اسمك فيها.<br>لا تغيري تخصصك أو رسالتك بس لأنك إنتِ مليتي من تكرارها بينما الناس لسه عم تتعرف عليكي.",
    "إذا إنتي زهقتي… معناها الناس هلأ بلشت تحفظ 😂"),
   ("5. تصيري صارمة جداً بشو بتعطي وقتك واهتمامك",
    "تبطلي تعتبري كل فرصة فرصة لازم تستغليها.<br>إذا الشي ما عم يقوي اسمك أو يطور خبرتك أو يكبر جمهورك أو يزيد دخلك اسألي حالك:<br>ليش عم أعطيه من وقتي؟",
    "مو كل عزيمة عالقهوة اجتماع بزنس ☕")]
foot='<div class="foot"><img src="photos/avatar.png"><div><b>Itscoachhiba</b><span>@itscoachhiba</span></div></div>'
arrow='<svg class="swipe" viewBox="0 0 120 60"><path d="M100 30 H18 M40 10 L18 30 L40 50" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
s='<section class="slide cover"><i></i><div class="hook"><p class="w">10 تصرفات توكسيك</p><p class="o">لتصيري الاسم الأول بمجالك</p></div></section>'
for t,b,j in P:
    n,rest=t.split(". ",1)
    s+=f'<section class="slide txt"><div class="body"><h2><bdi dir="ltr">{n}.</bdi>&nbsp;{rest}</h2><p class="q">{b}</p><p class="j">{j}</p></div>{foot}{arrow}</section>'
s+=f'<section class="slide txt"><div class="body"><h2>وتذكري</h2><p class="q">ما بتصيري الاسم الأول بمجالك لأنك عم تحاولي تبهري الكل.</p><p class="q">بتصيري الاسم الأول لما تكوني واضحة جداً مين إنتِ وشو بيميزك وشو القيمة اللي بتقدميها<br>لدرجة إنو الشخص الصح ما عاد يفكر يروح لحدا غيرك.</p></div>{foot}{arrow}</section>'
s+=f'<section class="slide txt"><div class="body"><p class="q">إذا عم تعاني إنك تجذبي الانتباه على السوشيال ميديا وتحولي هالانتباه لمبيعات</p><h2 class="cta">ابعتيلي كلمة</h2><p class="kw" dir="ltr">BRAND</p><p class="q">بالخاص وبساعدك تكبري حسابك وتبيعي من خلال السوشيال ميديا</p></div>{foot}</section>'
css=f'''@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}}@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}}@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}}
*{{margin:0;box-sizing:border-box}}
.slide{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:#000;color:#fff;font-family:P,'Noto Color Emoji';font-weight:700;text-align:center}}
.cover{{background:url(photos/cover.jpg) 69% 30%/cover}}
.cover i{{position:absolute;inset:0;background:linear-gradient(to bottom,rgba(0,0,0,0) 40%,rgba(0,0,0,.55) 75%,rgba(0,0,0,.35))}}
.hook{{position:absolute;left:40px;right:40px;bottom:{int(H*0.2)}px}}
.hook p{{text-shadow:0 3px 8px rgba(0,0,0,.85),0 0 30px rgba(0,0,0,.6)}}
.hook .w{{font-size:92px;line-height:1.3}}.hook .o{{font-size:80px;line-height:1.3;color:#F2531E}}
.body{{position:absolute;left:80px;right:80px;top:0;bottom:200px;display:flex;flex-direction:column;justify-content:center;gap:50px}}
h2{{color:#F2531E;font-size:60px;line-height:1.4;text-wrap:balance}}
.q{{font-size:48px;line-height:1.55;text-wrap:balance}}
.j{{font-family:P,'Noto Color Emoji';font-weight:500;font-size:38px;color:#bdbdbd}}
.cta{{margin-top:0}}.kw{{font-size:170px;color:#F2531E;line-height:1}}
.foot{{position:absolute;left:60px;bottom:60px;display:flex;align-items:center;gap:22px;direction:ltr}}
.foot img{{width:104px;height:104px;border-radius:50%;border:3px solid #333}}
.foot div{{display:flex;flex-direction:column;text-align:left}}.foot b{{font-size:40px}}.foot span{{font-weight:500;font-size:30px;color:#bbb}}
.swipe{{position:absolute;right:70px;bottom:80px;width:110px}}'''
open(sys.argv[2],"w",encoding="utf-8").write(f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{strip(s)}</body></html>')
