import json, sys, os, subprocess, numpy as np
from PIL import Image, ImageFilter
tl=json.load(open("timeline.json",encoding="utf-8"))
segs=json.load(open("../cv3.json",encoding="utf-8"))
FPS=30; W,H=1080,1920
SRC="../cut_v3.mp4"
N=int(round(tl["DUR"]*FPS))
def inK(t): return any(a<=t<b for a,b,_,_ in tl["K"])
# zoom targets: alternate per segment, punch-in during keywords
starts=[s["start"] for s in segs]
def target(t):
    if inK(t): return 1.15
    i=max([k for k,s in enumerate(starts) if s<=t] or [0])
    return 1.07 if i%2 else 1.0
z=np.zeros(N); cur=1.0
for f in range(N):
    tg=target(f/FPS); cur+= (tg-cur)*0.28; z[f]=cur
def zoom(img,zz):
    if zz<1.001: return img
    cw,ch=W/zz,H/zz; cx,cy=W*0.5,H*0.36
    x0=min(max(cx-cw/2,0),W-cw); y0=min(max(cy-ch/2,0),H-ch)
    return img.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+cw,y0+ch))
sess=None
def person_mask(img):
    global sess
    from rembg import remove, new_session
    if sess is None: sess=new_session("isnet-general-use")
    small=img.resize((540,960))
    m=remove(small,session=sess,only_mask=True)
    return m.resize((W,H),Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.5))
def run(f0,f1,out):
    dec=subprocess.Popen(["ffmpeg","-v","error","-ss",str(f0/FPS),"-i",SRC,"-frames:v",str(f1-f0),"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
    enc=None
    if out.endswith(".mp4"):
        enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
             "-c:v","libx264","-preset","medium","-crf","17","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE)
    for f in range(f0,f1):
        raw=dec.stdout.read(W*H*3)
        if len(raw)<W*H*3: break
        img=zoom(Image.frombytes("RGB",(W,H),raw),z[f]).convert("RGBA")
        t=f/FPS; name=f"{f:05d}.png"
        if inK(t) and os.path.exists("back/"+name):
            m=person_mask(img.convert("RGB"))
            img.alpha_composite(Image.open("back/"+name))
            person=img.copy(); 
            base=zoom(Image.frombytes("RGB",(W,H),raw),z[f]).convert("RGBA")
            img=Image.composite(base,img,m)
        if os.path.exists("front/"+name): img.alpha_composite(Image.open("front/"+name))
        if enc: enc.stdin.write(img.convert("RGB").tobytes())
        else: img.convert("RGB").save(f"{out}/{name}")
    if enc: enc.stdin.close(); enc.wait()
if __name__=="__main__":
    run(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
