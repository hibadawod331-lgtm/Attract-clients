import sys
from PIL import Image, ImageOps

U = "/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
# Mirror both images so the weak hand (scissors) sits on the RIGHT,
# which Arabic readers see first; the strong hand (rock) is on the left.
for src, dst in [("8397c717-image.png", "hands.png"), ("712eacb3-image.png", "coffee.png")]:
    im = ImageOps.mirror(Image.open(U + src).convert("RGB"))
    # push the near-white studio background to pure white so it blends into the slide
    im = im.point(lambda v: 255 if v >= 238 else int(v * 255 / 238))
    im.save(dst)

P = [("استني عريس غني", "صيري انتي الغنية"),
     ("اشرحي وبرري أحلامك", "فرجيهم نتائجك"),
     ("استني الوقت المناسب", "ابدئي الآن"),
     ("استني زيادة براتبك", "سعري خبرتك بنفسك"),
     ("شغلي مهاراتك عند غيرك", "حولي مهاراتك لبزنس رقمي"),
     ("اركضي ورا العملاء", "اجذبي عملاء"),
     ("انشري وادعي", "انشري محتوى وبيعي"),
     ("نزلي أسعارك", "ارفعي قيمتك")]

h = '<div class="h">@itscoachhiba</div>'
s = ""
for w, st in P:
    s += f'<section class="slide"><div class="pair"><p class="w">{w}</p><i></i><p class="s">{st}</p></div><img class="img" src="hands.png">{h}</section>'
s += ('<section class="slide end"><div class="top"><p class="big">نفس المهارات. <b>دخل أكبر.</b></p>'
      '<p class="sub">الراتب مو خيارك الوحيد.</p></div><img class="img" src="coffee.png">'
      '<div class="cta">اكتبي <b dir="ltr">BRAND</b> بالكومنتات وببعتلك كيف تحولي مهاراتك لبزنس رقمي</div>' + h + '</section>')

css = '''@font-face{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-700.woff2)}@font-face{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2);unicode-range:U+0000-00FF}
@font-face{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-500.woff2)}@font-face{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2);unicode-range:U+0000-00FF}
*{margin:0;box-sizing:border-box}body{background:#ddd}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;color:#111;font-family:P;text-align:center}
.img{position:absolute;left:0;top:560px;width:1080px;mix-blend-mode:multiply}
.pair{position:absolute;top:400px;left:60px;right:60px;display:flex;align-items:center;justify-content:center}
.pair p{flex:1;font-size:46px;line-height:1.35;text-wrap:balance;padding:0 26px}
.pair .w{font-weight:500;color:#222}.pair .s{font-weight:700;color:#F2531E}
.pair i{width:2px;height:120px;background:#111;flex:none}
.h{position:absolute;bottom:56px;left:0;right:0;font-weight:500;font-size:28px;color:#9a9a9a;direction:ltr}
.end .img{top:470px}
.end .top{position:absolute;top:200px;left:80px;right:80px}
.big{font-weight:700;font-size:70px;line-height:1.3}.big b{color:#F2531E}
.sub{font-weight:500;font-size:48px;margin-top:22px;color:#222}
.cta{position:absolute;top:1090px;left:110px;right:110px;font-weight:500;font-size:40px;line-height:1.5;text-wrap:balance}
.cta b{color:#F2531E;font-weight:700}'''

open(sys.argv[1], "w", encoding="utf-8").write(
    f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{css}</style></head><body>{s}</body></html>')
