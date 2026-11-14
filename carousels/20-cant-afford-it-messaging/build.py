"""Carousel 20: why your clients say "your price is too high" -> it's a messaging problem (Arabic).
Run, then: node shotall.js <this dir>"""
O = "#F2531E"
o = lambda t: f'<em>{t}</em>'
H = '<div class="foot"><img src="avatar.png"><div><b>Itscoachhiba</b><span>@itscoachhiba</span></div></div>'
ARROW = '<svg class="swipe" viewBox="0 0 120 60"><path d="M100 30 H18 M40 10 L18 30 L40 50" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

slides = [
    ["ما في شي أصعب من إنك تحكي مع وحدة باين عليها متحمسة تشتغل معك…",
     "…وأول ما تقوليلها السعر، بتقلك «ما عندي إمكانية إني ادفع هالمبلغ»."],
    ["إذا صارت مرة أو مرتين… طبيعي.",
     "بس إذا صارت كل شوي… بتبلشي تقنعي حالك إنو لازم تنزلي سعرك.",
     f"بس لاحظتي إنك حتى لما بتنزليه… {o('بيضلوا ما يشتروا؟')}",
     "<b>وهاد السبب.</b>"],
    ["إنك تجذبي ناس ما بيقدروا يستثمروا، مش مشكلة بسعرك.",
     f"هي فعليا مشكلة {o('بالـ messaging')} تبعك، بمحتواكي وببزنسك.",
     "والرسالة الغلط بتجيبلك العميلات الغلط."],
    [f"يعني ممكن تكوني عم تعملي محتوى للناس اللي عرضك {o('بيقدر')} يساعدهم…",
     f"بدل الناس اللي عرضك {o('انعمل إلهم')}.",
     "والفرق بين الاتنين كبير كتير."],
    ["أكيد إنتي خبيرة، وبتقدري تساعدي ناس كتير بمستويات مختلفة.",
     f"بس إذا عرضك مصمم لوحدة صار عندها بزنس ودخل، لازم محتواك يحكي {o('معها هي وبس')}."],
    ["أول ما تفكري «ما بدي خسر حدا»… خسرتي.",
     f"لأنو رسالتك بتصير تحكي مع {o('الكل')}:",
     "اللي لسا مبلشة. اللي صار عندها خبرة. اللي جاهزة تستثمر. واللي لأ."],
    ["هاد اللي ما بتنتبهله أغلب الأشخاص اللي عندهم خدمات أو منتجات رقمية…",
     f"العميلة اللي بدك ياها مشاكلها وأولوياتها وأهدافها {o('غير تماما')} عن وحدة لسا عم تبلش.",
     f"وإذا رسالتك ما بتحكي عن {o('واقعها هي')}، رح تضلي تجذبي الناس الغلط."],
    [f"الرسالة الواضحة والـ messaging الصح هي {o('أول شي')} لازم تبلشي تغيريه.",
     "وإذا بدك تعرفي كيف بالزبط بتقدري تبني براند شخصي قوي وتزيدي دخلك،",
     f"علقي بكلمة {o('«مكالمة»')} لتحجزي مكالمة استشارية مجانية."],
]

import re
def clean(t):
    t = re.sub("[أإآ]", "ا", t)
    t = t.replace("،", "").replace(", ", " ").replace(",", "")
    t = re.sub(r"^…", "", t)
    t = re.sub(r"…(</em>)?$", r".\1", t)
    t = re.sub(r"…(</em>)?$", r"\1", t)
    t = re.sub(r"…\s*", " ", t)
    return re.sub(r"\s+", " ", t).strip()
slides = [[clean(p) for p in ps] for ps in slides]
html = ['''<section class="slide cover"><img src="cover.jpg"><div class="shade"></div>
<h1>ليش العملاء اللي بيجوكي دايما بيقولولك <span>«سعرك غالي عليي»</span>؟</h1></section>''']
for k, ps in enumerate(slides):
    html.append('<section class="slide txt"><div class="box">' + "".join(f"<p>{p}</p>" for p in ps) + f'</div>{H}{ARROW if k < len(slides)-1 else ""}</section>')

css = f'''@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}}@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}}@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}}
*{{margin:0;box-sizing:border-box}}body{{background:#333}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;direction:rtl}}
.cover img{{position:absolute;width:1458px;left:-260px;top:-560px}}
.cover .shade{{position:absolute;left:0;right:0;bottom:0;height:62%;background:linear-gradient(transparent,rgba(0,0,0,.72))}}
.cover h1{{position:absolute;left:70px;right:70px;bottom:120px;color:#fff;font-weight:700;font-size:86px;line-height:1.18;text-align:right;text-shadow:0 3px 18px rgba(0,0,0,.35)}}
.cover h1 span{{color:{O}}}
.txt{{background:#0d0d0d;color:#f2f2f2}}
.txt .box{{position:absolute;top:0;bottom:120px;left:110px;right:110px;display:flex;flex-direction:column;justify-content:center;gap:40px;text-align:center}}
.txt p{{font-weight:500;font-size:46px;line-height:1.5}}
.txt b{{font-weight:700}}
.txt em{{font-style:normal;color:{O};font-weight:700}}
.foot{{position:absolute;left:60px;bottom:60px;display:flex;align-items:center;gap:22px;direction:ltr;color:#fff}}
.foot img{{width:104px;height:104px;border-radius:50%;border:3px solid #333}}
.foot div{{display:flex;flex-direction:column;text-align:left}}.foot b{{font-weight:700;font-size:40px}}.foot span{{font-weight:500;font-size:30px;color:#bbb}}
.swipe{{position:absolute;right:70px;bottom:80px;width:110px}}'''
open("carousel.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(html)}</body></html>')
