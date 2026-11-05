import sys
from PIL import Image

U = "/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
# English reads left to right, so keep the original orientation:
# weak hand (scissors) on the LEFT is read first.
for src, dst in [("8397c717-image.png", "hands_en.png"), ("712eacb3-image.png", "coffee_en.png")]:
    im = Image.open(U + src).convert("RGB")
    im = im.point(lambda v: 255 if v >= 238 else int(v * 255 / 238))
    im.save(dst)

P = [("wait for a rich husband", "become the rich one"),
     ("explain your dreams", "show your results"),
     ("wait for the right time", "start now"),
     ("wait for a raise", "set your own price"),
     ("use your skills for someone else", "turn them into a digital business"),
     ("chase clients", "attract clients"),
     ("post and pray", "post and sell"),
     ("lower your prices", "raise your value")]

h = '<div class="h">@itscoachhiba</div>'
s = ""
for w, st in P:
    s += f'<section class="slide"><div class="pair"><p class="w">{w}</p><i></i><p class="s">{st}</p></div><img class="img" src="hands_en.png">{h}</section>'
s += ('<section class="slide end"><div class="top"><p class="big">Your skills already make someone rich.</p>'
      '<p class="big o">Make it you.</p></div><img class="img" src="coffee_en.png">'
      '<div class="cta">Comment <b>BRAND</b> and I\'ll send you how to turn your skills into a digital business</div>' + h + '</section>')

css = '''@font-face{font-family:P;font-weight:700;src:url(ibm-plex-sans-arabic-latin-700.woff2)}
@font-face{font-family:P;font-weight:500;src:url(ibm-plex-sans-arabic-latin-500.woff2)}
*{margin:0;box-sizing:border-box}body{background:#ddd}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;color:#111;font-family:P;text-align:center}
.img{position:absolute;left:0;top:560px;width:1080px;mix-blend-mode:multiply}
.pair{position:absolute;top:400px;left:60px;right:60px;display:flex;align-items:center;justify-content:center}
.pair p{flex:1;font-size:44px;line-height:1.3;text-wrap:balance;padding:0 26px}
.pair .w{font-weight:500;color:#222}.pair .s{font-weight:700;color:#F2531E}
.pair i{width:2px;height:120px;background:#111;flex:none}
.h{position:absolute;bottom:56px;left:0;right:0;font-weight:500;font-size:28px;color:#9a9a9a}
.end .img{top:470px}
.end .top{position:absolute;top:180px;left:80px;right:80px}
.big{font-weight:700;font-size:62px;line-height:1.25;text-wrap:balance}.big.o{color:#F2531E;margin-top:14px}
.cta{position:absolute;top:1090px;left:110px;right:110px;font-weight:500;font-size:38px;line-height:1.45;text-wrap:balance}
.cta b{color:#F2531E;font-weight:700}'''

open(sys.argv[1], "w", encoding="utf-8").write(
    f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body>{s}</body></html>')
