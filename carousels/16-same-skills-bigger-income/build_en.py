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
s += ('<section class="slide end"><div class="top"><p class="big">Your skills are already making someone rich.</p>'
      '<p class="big o">Why not you?</p></div><img class="img" src="coffee_en.png">'
      '<div class="cta">Comment <b>BRAND</b> and I\'ll send you how to turn your skills into a digital business</div>' + h + '</section>')

css = '''@font-face{font-family:S;font-style:normal;src:url(instrument-serif-400-normal.woff2)}
@font-face{font-family:S;font-style:italic;src:url(instrument-serif-400-italic.woff2)}
*{margin:0;box-sizing:border-box}body{background:#ddd}
.slide{width:1080px;height:1350px;position:relative;overflow:hidden;background:#fff;color:#111;font-family:S;font-weight:400;text-align:center;letter-spacing:-0.01em}
.img{position:absolute;left:0;top:560px;width:1080px;mix-blend-mode:multiply}
.pair{position:absolute;top:395px;left:60px;right:60px;display:flex;align-items:center;justify-content:center}
.pair p{flex:1;font-size:60px;line-height:1.1;text-wrap:balance;padding:0 30px}
.pair .w{color:#111}.pair .s{color:#F2531E;font-style:italic}
.pair i{width:1.5px;height:130px;background:#111;flex:none}
.h{position:absolute;bottom:52px;left:0;right:0;font-size:32px;color:#9a9a9a}
.end .img{top:470px}
.end .top{position:absolute;top:170px;left:90px;right:90px}
.big{font-size:88px;line-height:1.05;text-wrap:balance}.big.o{color:#F2531E;font-style:italic;margin-top:22px}
.cta{position:absolute;top:1085px;left:120px;right:120px;font-size:50px;line-height:1.15;text-wrap:balance}
.cta b{color:#F2531E;font-weight:400;font-style:italic}'''

open(sys.argv[1], "w", encoding="utf-8").write(
    f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}</style></head><body>{s}</body></html>')
