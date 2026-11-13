"""Carousel 19: the $500 client vs the $10,000 client (Arabic). Run, then: node shotall.js <this dir>"""
RED, GREEN, ORANGE = "#B3262B", "#2F5A3A", "#F2531E"
H = '<div class="h">@itscoachhiba</div>'

slides = []
# 1. cover: both women, labels above each (RTL: right = $500 thinking, left = $10K ready)
slides.append(f'''<section class="slide cover"><img class="full" src="both.jpg">
<h1>الفرق بين عميلة <span dir="ltr">$500</span><br>وعميلة <span dir="ltr">$10,000</span></h1>
<div class="lab r" style="color:{RED}">عميلة <span dir="ltr">$500</span><i style="background:{RED}"></i></div>
<div class="lab l" style="color:{GREEN}">عميلة <span dir="ltr">$10,000</span><i style="background:{GREEN}"></i></div>
<div class="swipe">اسحبي لتشوفي الفرق ←</div></section>''')

def quote(img, color, label, msgs, side, green=False):
    b = "".join(f'<div class="msg{" g" if green else ""}">{m}</div>' for m in msgs)
    seen = '<div class="seen">✓✓ تم الدفع</div>' if green else ''
    return f'''<section class="slide q {side}"><img class="half" src="{img}">
<div class="chat"><div class="tag" style="background:{color}">{label}</div>{b}{seen}</div>{H}</section>'''

slides.append(quote("thinking.jpg", RED, 'عميلة <span dir="ltr">$500</span>',
    ["بحس إنو بدي وقت لأفكر أكتر", "أنا بدي نتائج وإنتي لازم تجيبيها", "أنا عم أأتمنك على رزقنا وحياتنا",
     "لازم آخد رأي فلان قبل ما أبدأ", "في خيارات تقسيط على 6 شهور؟", "محتاجة معلومات أكتر"], "r"))
slides.append(quote("ready.jpg", GREEN, 'عميلة <span dir="ltr">$10,000</span>', ["حولت المصاري. شكرا."], "l", True))

slides.append(f'''<section class="slide txt"><div class="box">
<p class="big">العميلة اللي بتدفع أقل…<br><b style="color:{RED}">بتطلب أكتر.</b></p>
<p class="big">والعميلة اللي بتدفع أكتر…<br><b style="color:{GREEN}">بتثق أكتر.</b></p>
<p class="sub">لأنها ما عم تشتري ساعات من وقتك. عم تشتري نتيجة واضحة من شخص بتعرف شو بيقدم.</p>
</div>{H}</section>''')

slides.append(f'''<section class="slide txt"><div class="box">
<p class="big">سعرك مش بس رقم.<br><b style="color:{ORANGE}">سعرك بيختار عميلاتك.</b></p>
<p class="sub">عرض واضح، بسعر صح، بيجذب عميلات جاهزات يدفعوا، بدل ما تضلي تقنعي عميلات خايفات.</p>
<div class="cta">إذا بدك تعرفي كيف تحولي خبرتك لدخل وتكبري بزنسك، علقي بكلمة <b>«براند»</b> وببعتلك كل التفاصيل بالخاص</div>
</div>{H}</section>''')

css = f'''@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}}@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}}@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}}
*{{margin:0;box-sizing:border-box}}body{{background:#ddd}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;color:#1d1d1f;font-family:P;text-align:center;direction:rtl}}
.h{{position:absolute;bottom:44px;left:0;right:0;font-weight:500;font-size:28px;color:#9a9a9a;direction:ltr}}
.cover .full{{position:absolute;left:90px;top:240px;width:900px}}
.cover h1{{position:absolute;top:70px;left:40px;right:40px;font-weight:700;font-size:72px;line-height:1.3}}
.lab{{position:absolute;top:345px;font-weight:700;font-size:46px;width:440px}}
.lab i{{display:block;width:60px;height:5px;border-radius:3px;margin:14px auto 0}}
.lab.r{{right:122px}}.lab.l{{left:95px}}
.swipe{{position:absolute;bottom:24px;left:0;right:0;font-weight:500;font-size:34px;color:#333}}
.q .half{{position:absolute;bottom:-30px;height:1120px}}
.q.r .half{{left:-10px}}.q.l .half{{left:-60px}}
.tag{{color:#fff;font-weight:700;font-size:44px;padding:10px 34px;border-radius:40px;margin-bottom:14px}}
.chat{{position:absolute;top:80px;width:600px;display:flex;flex-direction:column;align-items:flex-start;gap:12px}}
.q.r .chat{{right:50px;width:560px}}.q.l .chat{{left:60px}}
.msg{{background:#EDEDF0;border-radius:28px 28px 28px 8px;padding:14px 26px;font-weight:500;font-size:36px;line-height:1.4;box-shadow:0 2px 8px rgba(0,0,0,.07)}}
.msg.g{{background:#2F5A3A;color:#fff;font-weight:700;font-size:48px;padding:20px 34px}}
.seen{{font-weight:500;font-size:28px;color:#2F5A3A;margin:0 12px}}

.bubble{{position:absolute;top:190px;width:560px;background:#fff;border:4px solid;border-radius:34px;padding:34px 38px;text-align:right;box-shadow:0 18px 50px rgba(0,0,0,.12)}}
.q.r .bubble{{left:60px}}.q.l .bubble{{right:60px;width:500px}}
.bubble p{{font-weight:500;font-size:40px;line-height:1.6}}
.q.l .bubble p{{font-weight:700;font-size:60px;text-align:center}}
.txt .box{{position:absolute;top:0;bottom:0;left:90px;right:90px;display:flex;flex-direction:column;justify-content:center;gap:56px}}
.big{{font-weight:700;font-size:68px;line-height:1.35}}
.sub{{font-weight:500;font-size:40px;line-height:1.6;color:#444}}
.cta{{font-weight:700;font-size:42px;line-height:1.5;background:#FEF0EA;border-radius:28px;padding:30px}}.cta b{{color:{ORANGE}}}'''

open("carousel.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(slides)}</body></html>')
