import json,subprocess
dur={i:float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'vo/t{i}.wav'])) for i in range(8)}
G=0.35  # gap between question and answer
ans=[(None,None),(68.92,70.30),(53.40,58.05),(104.30,109.20),(129.15,139.30),(145.70,146.65),(149.40,158.00),(160.15,173.55)]
parts=[]
# P0 title: video 1.0 .. 1.0+vo+0.4, original muted
parts.append(dict(v0=46.0,v1=46.0+dur[0]+0.5,vo=0,vo_at=0.15,mute_until=99))
for i in range(1,8):
    a,b=ans[i]; v0=a-dur[i]-G-0.1
    parts.append(dict(v0=round(v0,2),v1=b,vo=i,vo_at=0.1,mute_until=round(a-0.05-v0,2)))
parts.append(dict(v0=290.90,v1=293.55,vo=None,vo_at=0,mute_until=0))
json.dump(parts,open('cut.json','w'),indent=0)
for k,p in enumerate(parts):
    L=p['v1']-p['v0']
    vf='scale=1080:1920,fps=30'
    af=f"[0:a]volume=enable='lt(t,{p['mute_until']})':volume=0,afade=t=in:d=0.02,afade=t=out:st={L-0.03}:d=0.03[o]"
    cmd=['ffmpeg','-v','error','-y','-ss',str(p['v0']),'-to',str(p['v1']),'-i','../reel9_dl/main.mp4']
    if p['vo'] is not None:
        cmd+=['-i',f"vo/t{p['vo']}.wav"]
        d=int(p['vo_at']*1000)
        af+=f";[1:a]adelay={d},volume=1.6,apad[v];[o][v]amix=inputs=2:duration=first:normalize=0[a]"
    else: af+=';[o]anull[a]'
    cmd+=['-filter_complex',af,'-map','0:v','-map','[a]','-vf',vf,'-c:v','libx264','-crf','16','-preset','fast','-c:a','aac','-b:a','192k','-ar','48000',f'parts/{k:02d}.mp4']
    subprocess.run(cmd,check=True)
    print(k,p,round(L,2))
