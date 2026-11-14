"""Carousel 21: how I helped Lana (dietitian) go from 0 to her first $10K month in 90 days (Arabic).
Run, then: node shotall.js <this dir>"""
O = "#F2531E"
o = lambda t: f'<em>{t}</em>'
D = lambda t: f'<bdi dir="ltr">{t}</bdi>'
FOOT = '<div class="foot"><img src="avatar.png"><div><b>Itscoachhiba</b><span>@itscoachhiba</span></div></div>'
ARROW = '<svg class="swipe" viewBox="0 0 120 60"><path d="M100 30 H18 M40 10 L18 30 L40 50" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

slides = [
    # 2: who + proof
    f'''<p class="big">لانا اخصائية تغذية وعندها خبرة سنين</p>
<p class="big">بس لما تواصلت معي كان دخلها من شغلها اونلاين تقريبا صفر</p>
<p class="big">{o('وخلال 90 يوم عملت اول')} {o(D('$10,000'))} {o('بالشهر')}</p>
<img class="proof" src="proof.jpg">''',
    # 3: problems
    f'''<p class="big">لما قعدنا سوا لقينا:</p>
<ul><li>عرضها كان «استشارة تغذية» بالجلسة بدون نتيجة واضحة</li>
<li>عم تحكي مع كل حدا بدو ينحف بدل عميلة وحدة واضحة</li>
<li>سعرها بالساعة ورخيص</li>
<li>محتواها مفيد بس ما عم يجيبلها ولا رسالة</li>
<li>وبالخاص عم تعطي كل شي ببلاش</li></ul>
<p class="big">{o('يعني الخبرة موجودة بس ما في شي عم يحولها لمبيعات.')}</p>''',
    # 4: offer
    f'''<p class="big">اول شي ما زدنا محتوى</p>
<p class="big">{o('صلحنا العرض')}</p>
<p>من «استشارة تغذية» لبرنامج واضح: لمين هو وشو المشكلة اللي بيحلها وشو النتيجة وبكم اسبوع</p>
<p>ولما صار في نتيجة واضحة {o('رفعنا السعر')} لانو صار يستاهل</p>''',
    # 5: messaging
    f'''<p class="big">بعدها {o('صلحنا الرسالة')}</p>
<p>حددنا مين العميلة اللي بدها ياها بالزبط وصار كل محتواها يحكي عن {o('مشاكلها هي')} وواقعها هي</p>
<p class="big">فصاروا يجوها ناس {o('جاهزين يستثمروا')} مش بس يسألوا</p>''',
    # 6: content -> sales + result
    f'''<p class="big">وبطلنا نعطي كل شي ببلاش</p>
<p>كل محتوى صار ينتهي بدعوة واضحة للخاص وبنينا طريقة محادثة بتحول الاهتمام لقرار شراء بدل «بفكر وبرجعلك»</p>
<p class="big">والنتيجة؟</p>
<p class="huge">{o(D('$10,000'))} بالشهر خلال 90 يوم</p>
<p class="big">من عرض واحد واضح</p>''',
    # 7: CTA
    f'''<p class="big">اذا انتي مدربة وعندك خبرة بس عرضك ما عم يبيع</p>
<p class="big">{o('علقي بكلمة «براند»')} وببعتلك كل التفاصيل بالخاص</p>''',
]

html = [f'''<section class="slide cover"><img class="bg" src="cover.jpg"><div class="shade"></div>
<h1>كيف ساعدت عميلتي توصل من {D('0')} لـ {D('$10,000')} بالشهر كمدربة بمجالها</h1><div class="sub">مع الدليل!!</div></section>''']
for k, s in enumerate(slides):
    html.append(f'<section class="slide txt"><div class="box">{s}</div>{FOOT}{ARROW if k < len(slides)-1 else ""}</section>')

css = f'''@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}}@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}}@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}}
*{{margin:0;box-sizing:border-box}}body{{background:#333}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;direction:rtl}}
.cover .bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}}
.cover .shade{{position:absolute;left:0;right:0;bottom:0;height:55%;background:linear-gradient(transparent,rgba(0,0,0,.82))}}
.cover h1{{position:absolute;left:70px;right:70px;bottom:190px;color:#fff;font-weight:700;font-size:76px;line-height:1.25;text-align:center}}
.cover .sub{{position:absolute;left:0;right:0;bottom:90px;text-align:center;color:{O};font-weight:700;font-size:64px}}
.txt{{background:#000;color:#fff}}
.txt .box{{position:absolute;top:60px;bottom:200px;left:80px;right:80px;display:flex;flex-direction:column;justify-content:center;gap:30px;text-align:center}}
.txt p{{font-weight:500;font-size:44px;line-height:1.45}}
.txt .big{{font-weight:700;font-size:54px;line-height:1.35}}
.txt .huge{{font-weight:700;font-size:76px;line-height:1.2}}
.txt em{{font-style:normal;color:{O}}}
.txt ul{{list-style:none;padding:0;display:flex;flex-direction:column;gap:14px}}
.txt li{{font-weight:500;font-size:42px;line-height:1.4;color:#fff}}
.txt li::before{{content:"✗  ";color:{O};font-weight:700}}
.proof{{width:780px;align-self:center;border-radius:18px;margin-top:6px}}
.foot{{position:absolute;left:60px;bottom:60px;display:flex;align-items:center;gap:22px;direction:ltr;color:#fff}}
.foot img{{width:104px;height:104px;border-radius:50%;border:3px solid #333}}
.foot div{{display:flex;flex-direction:column;text-align:left}}.foot b{{font-weight:700;font-size:40px}}.foot span{{font-weight:500;font-size:30px;color:#bbb}}
.swipe{{position:absolute;right:70px;bottom:80px;width:110px}}'''
open("carousel.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(html)}</body></html>')
