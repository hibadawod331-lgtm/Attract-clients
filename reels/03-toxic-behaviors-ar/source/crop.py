from PIL import Image
U="/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
M={
"hook_0":("1e8419d2",.5,.42),"hook_1":("3f8748b0",.5,.4),"hook_2":("7f7f3c3f",.5,.35),"hook_3":("c994afe0",.5,.5),
"p1_0":("520c4869",.5,.45),"p1_1":("32195510",.5,.4),
"p2_0":("31426370",.5,.42),"p2_1":("c24d08b1",.5,.55),
"p3_0":("a1b28f86",.5,.55),"p3_1":("284708d9",.5,.55),
"p4_0":("ec132cb3",.5,.6),"p4_1":("96507ae8",.45,.62),
"p5_0":("9d9f2fdc",.5,.55),"p5_1":("ef386230",.5,.35),
"end_0":("864d87d0",.5,.35),"end_1":("8c5b6168",.5,.5)}
for k,(f,fx,fy) in M.items():
    im=Image.open(U+f+"-image.jpg").convert("RGB"); w,h=im.size; r=0.8
    cw,ch=(w,w/r) if w/h<r else (h*r,h)
    x0=min(max(fx*w-cw/2,0),w-cw); y0=min(max(fy*h-ch/2,0),h-ch)
    im.crop((x0,y0,x0+cw,y0+ch)).resize((480,600),Image.LANCZOS).save(f"img/{k}.jpg",quality=92)
