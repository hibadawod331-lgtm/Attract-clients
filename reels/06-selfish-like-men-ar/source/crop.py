from PIL import Image
U="/root/.claude/uploads/15b7e2dc-92de-5f80-9fdc-4b214987c2b7/"
M={"hook_0":("c39d89a4",.5,.4),"hook_1":("00af3c88",.5,.45),"hook_2":("d0a0c841",.7,.3),"hook_3":("6a53fc1d",.5,.5),
"s1_0":("880afaba",.5,.45),"s1_1":("63b76009",.4,.6),
"s2_0":("bb9d652d",.5,.45),"s2_1":("4a62b1e6",.5,.5),
"s3_0":("959dacf9",.5,.5),"s3_1":("88159c3b",.5,.45),
"s4_0":("f37edc3b",.5,.45),"s4_1":("1784865a",.5,.5),
"s5_0":("bb9d652d",.5,.45),"s5_1":("c39d89a4",.5,.4)}
for k,(f,fx,fy) in M.items():
    im=Image.open(U+f+"-image.jpg").convert("RGB"); w,h=im.size; r=0.8
    cw,ch=(w,w/r) if w/h<r else (h*r,h)
    x0=min(max(fx*w-cw/2,0),w-cw); y0=min(max(fy*h-ch/2,0),h-ch)
    im.crop((x0,y0,x0+cw,y0+ch)).resize((480,600),Image.LANCZOS).save(f"fx/img/{k}.jpg",quality=92)
