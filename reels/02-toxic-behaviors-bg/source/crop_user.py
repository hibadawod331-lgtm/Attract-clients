from PIL import Image
U="/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
M={ # section_idx: (file, fx, fy)
"hook_0":("669fbafa",.5,.42),"hook_1":("1b29d690",.5,.35),"hook_2":("b6b814f4",.5,.40),"hook_3":("ef386230",.5,.35),
"p1_0":("33221e90",.5,.62),"p1_1":("10cb9c7c",.5,.5),
"p2_0":("e1750696",.5,.45),"p2_1":("be898132",.5,.5),
"p3_0":("8c5b6168",.5,.5),"p3_1":("342fd161",.5,.45),
"p4_0":("94a67aa6",.45,.4),"p4_1":("bb14f396",.5,.35),
"p5_0":("aa57494c",.5,.42),"p5_1":("5ea81c23",.5,.4),
"end_0":("33654cd0",.5,.3),"end_1":("62a8cdb1",.45,.45)}
for k,(f,fx,fy) in M.items():
    im=Image.open(U+f+"-image.jpg").convert("RGB"); w,h=im.size; r=0.8
    if w/h<r: cw,ch=w,w/r
    else: cw,ch=h*r,h
    x0=min(max(fx*w-cw/2,0),w-cw); y0=min(max(fy*h-ch/2,0),h-ch)
    im.crop((x0,y0,x0+cw,y0+ch)).resize((480,600),Image.LANCZOS).save(f"img/{k}.jpg",quality=92)
