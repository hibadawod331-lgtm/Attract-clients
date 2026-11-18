"""Carousel 22: digital products vs physical products, and why digital wins (Arabic).
Run, then: node shotall.js <this dir>"""
import re
O = "#F2531E"
o = lambda t: f'<em>{t}</em>'
D = lambda t: f'<bdi dir="ltr">{t}</bdi>'
FOOT = '<div class="foot"><img src="avatar.png"><div><b>Itscoachhiba</b><span>@itscoachhiba</span></div></div>'
ARROW = '<svg class="swipe" viewBox="0 0 120 60"><path d="M100 30 H18 M40 10 L18 30 L40 50" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def clean(t):
    t = re.sub("[أإآ]", "ا", t)
    return t.replace("،", "").replace("…", "")

def ul(items, mark):
    return f'<ul class="{mark}">' + "".join(f"<li><span>{i}</span></li>" for i in items) + "</ul>"

slides = [
    # 2 difference
    f'''<img class="vis" src="v2.jpg">
<p class="big">شو الفرق؟</p>
<p><b>المنتج الملموس</b> شي بينلمس: ملابس مكياج شموع اكسسوارات</p>
<p><b class="o">المنتج الرقمي</b> شي بيتحمل او بينحضر اونلاين: كورس كتاب الكتروني تمبلت ورشة برنامج كوتشينغ</p>''',
    # 3 physical
    f'''<img class="vis" src="v3.jpg">
<p class="big">المنتج الملموس بيحتاج:</p>
{ul(["راس مال من البداية", "مخزون وتخزين", "شحن وتغليف ومرتجعات", "ربح اقل بكل قطعة بعد التكاليف"], "x")}
<p>وكل ما بدك تبيعي اكتر لازم تصنعي او تشتري اكتر</p>''',
    # 4 digital
    f'''<img class="vis" src="v4.jpg">
<p class="big">المنتج الرقمي:</p>
{ul([f"بتعمليه {o('مرة وحدة')} وبتبيعيه {o('مرات غير محدودة')}", "ما في مخزون ولا شحن", "تكلفة البداية تقريبا صفر", f"ربحك ممكن يوصل لاكتر من {o(D('90%'))} من كل بيعة"], "v")}''',
    # 5 why now
    f'''<img class="vis" src="v5.jpg">
<p class="big">ليش الرقمي هو {o('الافضل')} هلا؟</p>
<p>لانو بتبيعي {o('خبرتك')} مش بضاعة</p>
<p>وبتوصلي لعميلات بكل العالم من تلفونك</p>
<p>وبتقدري تكبري بزنسك بدون ما تكبر تكاليفك</p>''',
    # 6 market + proof
    f'''<p class="big">وما رح تكوني لحالك بهالسوق</p>
<p>سوق التعليم الاونلاين لحاله مقدر بحوالي {o(D('$276') + ' مليار')} بـ {D('2026')} ومتوقع يوصل لاكتر من {o(D('$500') + ' مليار')} بـ {D('2032')}</p>
<div class="chart"><div class="ch-l">
<div class="ch-t">سوق التعليم الاونلاين</div><div class="ch-s">حجم السوق بمليارات الدولارات</div>
<div class="bars">
<div class="bar"><span class="v">{D('$275.9')}</span><i style="height:163px"></i><span class="y">{D('2026')}</span></div>
<div class="bar"><span class="v">{D('$305.8')}</span><i style="height:181px"></i><span class="y">{D('2027')}</span></div>
<div class="gap"><span class="cagr">نمو سنوي<br><b>{D('10.62%')}</b></span></div>
<div class="bar big"><span class="v">{D('$506.6')}</span><i style="height:300px"></i><span class="y">{D('2032')}</span></div>
</div></div>
<div class="ch-r">
<div class="st"><span>حجم السوق {D('2027')}</span><b>{D('$305.8')} مليار</b></div>
<div class="st"><span>حجم السوق {D('2032')}</span><b>{D('$506.6')} مليار</b></div>
<div class="st"><span>نسبة النمو السنوي</span><b>{D('10.62%')}</b></div>
<div class="st"><span>اكبر سوق</span><b>امريكا الشمالية</b></div>
<div class="st"><span>الاسرع نموا</span><b>اسيا والمحيط الهادئ</b></div>
</div></div>
<p class="src">المصدر: {D('Mordor Intelligence')}</p>
<p>واقتصاد صناع المحتوى متوقع يتعدى {o(D('$500') + ' مليار')} بـ {D('2030')}</p>''',
    # 7 why pick
    f'''<img class="vis" src="v7.jpg">
<p class="big">يعني الناس {o('عم تدفع')} لتتعلم من حدا عاش التجربة</p>
<p>واذا عندك خبرة بشي فانتي عندك منتج</p>
<p>السؤال مش اذا في سوق</p>
<p class="big">السؤال {o('امتى رح تبلشي')}</p>''',
    # 8 examples
    f'''<p class="big">خبرتك هي {o('منتجك')}</p>
<div class="ex">''' + "".join(f'<div class="row"><span class="k">{a}</span><span class="ar">←</span><span class="vv">{b}</span></div>' for a, b in [
        ("اخصائية تغذية", "برنامج 6 اسابيع لنزول الوزن"),
        ("مصممة غرافيك", "تمبلتات انستغرام وكانفا"),
        ("مدربة رياضة", "برنامج تمارين بالبيت"),
        ("محاسبة", "ورشة ادارة مصاري البزنس"),
        ("معلمة لغات", "كورس محادثة اونلاين"),
        ("خبيرة مكياج", "كورس مكياج خطوة بخطوة"),
        ("ام عندها تجربة", "دليل تنظيم وقت الام العاملة"),
        ("مسوقة سوشال ميديا", "كورس جيبي عميلات من انستغرام"),
    ]) + f'''</div>
<p class="big2">شو الشي اللي الناس دايما بتسالك عنه؟<br>{o('هاد هو منتجك الاول')}</p>''',
    # 9 CTA
    f'''<p class="huge">اذا بدك تعرفي كيف تحولي خبرتك لمنتج رقمي بيجيبلك دخل</p>
<p class="huge">{o('علقي بكلمة «براند»')}</p>
<p class="big">وببعتلك كل التفاصيل بالخاص</p>''',
]
slides = [clean(s) for s in slides]

html = [f'''<section class="slide cover"><img class="bg" src="cover.jpg"><div class="shade"></div>
<h1>منتجات رقمية ولا منتجات ملموسة؟</h1><div class="sub">وين لازم تحطي وقتك وطاقتك بـ {D('2026')}</div></section>''']
for k, s in enumerate(slides):
    html.append(f'<section class="slide txt"><div class="box">{s}</div>{FOOT}{ARROW if k < len(slides)-1 else ""}</section>')

css = f'''@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}}@font-face{{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}}@font-face{{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}}
*{{margin:0;box-sizing:border-box}}body{{background:#333}}
.slide{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P;direction:rtl}}
.cover .bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%}}
.cover .shade{{position:absolute;left:0;right:0;bottom:0;height:55%;background:linear-gradient(transparent,rgba(0,0,0,.85))}}
.cover h1{{position:absolute;left:70px;right:70px;bottom:200px;color:#fff;font-weight:700;font-size:84px;line-height:1.2;text-align:center}}
.cover .sub{{position:absolute;left:60px;right:60px;bottom:100px;text-align:center;color:{O};font-weight:700;font-size:52px}}
.txt{{background:#000;color:#fff}}
.txt .box{{position:absolute;top:50px;bottom:190px;left:80px;right:80px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:22px;text-align:center}}
.vis{{width:920px;height:470px;object-fit:cover;border-radius:28px;margin-bottom:10px}}
.chart{{width:920px;background:#fff;color:#111;border-radius:22px;padding:26px 28px;display:flex;gap:26px;text-align:right}}
.ch-l{{flex:1.15}}.ch-r{{flex:1;display:flex;flex-direction:column;gap:12px;border-right:2px solid #eee;padding-right:24px}}
.ch-t{{font-weight:700;font-size:30px}}.ch-s{{font-weight:500;font-size:22px;color:#777}}
.bars{{display:flex;align-items:flex-end;gap:18px;height:400px;border-bottom:2px solid #ddd;margin:6px 0 44px;direction:ltr}}
.bar{{display:flex;flex-direction:column;align-items:center;width:84px;position:relative}}
.bar i{{display:block;width:72px;border-radius:8px 8px 0 0;background:linear-gradient(#ff8a5c,{O})}}
.bar .v{{font-weight:700;font-size:24px;margin-bottom:6px}}.bar .y{{position:absolute;bottom:-38px;font-weight:700;font-size:24px;color:#444}}
.gap{{flex:1;align-self:center;text-align:center}}.cagr{{font-weight:500;font-size:22px;color:#666;direction:rtl;display:block}}.cagr b{{font-size:34px;color:{O}}}
.st{{display:flex;flex-direction:column;border-bottom:1px solid #eee;padding-bottom:8px}}.st span{{font-weight:500;font-size:22px;color:#777}}.st b{{font-weight:700;font-size:28px;color:#111}}
.src{{margin-top:22px!important}}
.src{{font-size:28px!important;color:#999;margin-top:-10px}}
.txt p{{font-weight:500;font-size:40px;line-height:1.45}}
.txt .big{{font-weight:700;font-size:54px;line-height:1.3}}
.txt .big2{{font-weight:700;font-size:44px;line-height:1.4;margin-top:10px}}
.txt .huge{{font-weight:700;font-size:70px;line-height:1.3}}
.txt em{{font-style:normal;color:{O}}}
.txt b.o{{color:{O}}}
.txt ul{{list-style:none;padding:0;display:flex;flex-direction:column;gap:12px;align-items:center}}
.txt li{{font-weight:500;font-size:40px;line-height:1.4;display:flex;gap:16px;align-items:baseline}}
.txt ul.x li::before{{content:"✗";color:{O};font-weight:700}}
.txt ul.v li::before{{content:"✓";color:{O};font-weight:700}}
.ex{{width:920px;display:flex;flex-direction:column;gap:14px}}
.row{{display:flex;align-items:center;gap:18px;background:#141414;border:2px solid #262626;border-radius:20px;padding:14px 26px;font-size:36px}}
.row .k{{font-weight:700;color:{O};white-space:nowrap}}.row .ar{{color:#777}}.row .vv{{font-weight:500;text-align:right}}
.foot{{position:absolute;left:60px;bottom:60px;display:flex;align-items:center;gap:22px;direction:ltr;color:#fff}}
.foot img{{width:104px;height:104px;border-radius:50%;border:3px solid #333}}
.foot div{{display:flex;flex-direction:column;text-align:left}}.foot b{{font-weight:700;font-size:40px}}.foot span{{font-weight:500;font-size:30px;color:#bbb}}
.swipe{{position:absolute;right:70px;bottom:80px;width:110px}}'''
open("carousel.html", "w", encoding="utf-8").write(
    f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(html)}</body></html>')
