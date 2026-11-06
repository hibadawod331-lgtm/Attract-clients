from PIL import Image
U="/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
M={"hook_0":("98a1856a",.5,.45),"hook_1":("eb82c02e",.5,.5),"hook_2":("8ee3cd26",.4,.5),"hook_3":("15710b25",.5,.45),
"p1_0":("824eec85",.5,.45),"p1_1":("709e8da0",.45,.5),
"p2_0":("f598451e",.5,.45),"p2_1":("32195510",.5,.4),
"p3_0":("a1b28f86",.5,.55),"p3_1":("6a77c37c",.5,.35),
"p4_0":("34f131f0",.5,.45),"p4_1":("d2efbf1d",.5,.4),
"p5_0":("2b0d2a6d",.5,.55),"p5_1":("efa55e3b",.5,.4),
"p6_0":("d5d065a9",.5,.45),"p6_1":("be51ba1b",.5,.5)}
for k,(f,fx,fy) in M.items():
    im=Image.open(U+f+"-image.jpg").convert("RGB"); w,h=im.size; r=0.8
    cw,ch=(w,w/r) if w/h<r else (h*r,h)
    x0=min(max(fx*w-cw/2,0),w-cw); y0=min(max(fy*h-ch/2,0),h-ch)
    im.crop((x0,y0,x0+cw,y0+ch)).resize((480,600),Image.LANCZOS).save(f"fx/img/{k}.jpg",quality=92)
