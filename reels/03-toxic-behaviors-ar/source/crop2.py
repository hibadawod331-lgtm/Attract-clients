from PIL import Image
U="/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
M={
"hook_0":("162cc887",.5,.35),"hook_1":("8ee46fb3",.5,.4),"hook_2":("969cf7ef",.5,.4),"hook_3":("d5a144fa",.5,.35),
"p1_0":("f598451e",.5,.45),"p1_1":("efa55e3b",.5,.4),
"p2_0":("3590a170",.5,.45),"p2_1":("02a8bae5",.5,.45),
"p3_0":("ac1d6a5a",.45,.55),"p3_1":("6a77c37c",.5,.35),
"p4_0":("d4197a83",(60,60,1060,1310)),"p4_1":("665a08da",.5,.4),
"p5_0":("5bb1cc8e",.5,.45),"p5_1":("c21e3925",.5,.4),
"end_0":("21168a0a",.5,.45),"end_1":("864d87d0",.5,.35)}
for k,v in M.items():
    im=Image.open(U+v[0]+"-image.jpg").convert("RGB"); w,h=im.size; r=0.8
    if len(v)==2: box=v[1]
    else:
        fx,fy=v[1],v[2]; cw,ch=(w,w/r) if w/h<r else (h*r,h)
        x0=min(max(fx*w-cw/2,0),w-cw); y0=min(max(fy*h-ch/2,0),h-ch); box=(x0,y0,x0+cw,y0+ch)
    im.crop(box).resize((480,600),Image.LANCZOS).save(f"fx/img/{k}.jpg",quality=92)
