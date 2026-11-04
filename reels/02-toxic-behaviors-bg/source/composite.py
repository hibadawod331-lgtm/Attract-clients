import json, sys, os, subprocess, numpy as np
from PIL import Image, ImageFilter
from rembg import remove, new_session
tl=json.load(open("timeline.json")); FPS=30; W,H=1080,1920; SRC="../cut3.mp4"
N=int(round(tl["dur"]*FPS)); secst=[s[0] for s in tl["sec"]]; segst=tl["segst"]
def target(t):
    if any(a<=t<a+1.2 for a in secst): return 1.13
    i=max([k for k,s in enumerate(segst) if s<=t] or [0]); return 1.07 if i%2 else 1.0
z=np.zeros(N); cur=1.0
for f in range(N): cur+=(target(f/FPS)-cur)*0.2; z[f]=cur
def zoom(img,zz):
    if zz<1.001: return img
    cw,ch=W/zz,H/zz; cx,cy=W*0.5,H*0.33
    x0=min(max(cx-cw/2,0),W-cw); y0=min(max(cy-ch/2,0),H-ch)
    return img.resize((W,H),Image.BICUBIC,box=(x0,y0,x0+cw,y0+ch))
os.makedirs("masks",exist_ok=True); sess=new_session("isnet-general-use")
def run(f0,f1,out):
    dec=subprocess.Popen(["ffmpeg","-v","error","-ss",str(f0/FPS),"-i",SRC,"-frames:v",str(f1-f0),"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
    enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p",out],stdin=subprocess.PIPE) if out.endswith(".mp4") else None
    for f in range(f0,f1):
        raw=dec.stdout.read(W*H*3)
        if len(raw)<W*H*3: break
        base=zoom(Image.frombytes("RGB",(W,H),raw),z[f]); name=f"{f:05d}.png"; img=base.convert("RGBA")
        if os.path.exists("back/"+name):
            mp="masks/"+name
            if os.path.exists(mp): m=Image.open(mp)
            else: m=remove(base.resize((432,768)),session=sess,only_mask=True); m.save(mp)
            m=m.resize((W,H),Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.2))
            img.alpha_composite(Image.open("back/"+name)); img=Image.composite(base.convert("RGBA"),img,m)
        if os.path.exists("front/"+name): img.alpha_composite(Image.open("front/"+name))
        if enc: enc.stdin.write(img.convert("RGB").tobytes())
        else: img.convert("RGB").save(f"{out}/{name}")
    if enc: enc.stdin.close(); enc.wait()
if __name__=="__main__": run(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3])
