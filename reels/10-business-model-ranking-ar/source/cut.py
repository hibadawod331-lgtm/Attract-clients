import json,subprocess
dur={i:float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'vo/t{i}.wav'])) for i in range(8)}
G=0.35
ans=[None,(50.00,50.80),(53.40,58.05),(104.30,109.20),(129.15,139.30),(145.70,146.65),(149.40,158.00),(160.15,173.55)]
parts=[]
# P0: one continuous shot from 46s: title VO, straight into the UGC question, then her answer at 50.0
ugc_at=0.05+dur[0]+0.08
parts.append(dict(v0=46.0,v1=51.40,vos=[(0,0.05),(1,ugc_at)],mute_until=round(50.0-0.05-46.0,2),q=1))
for i in range(2,8):
    a,b=ans[i]; v0=a-dur[i]-G-0.1
    parts.append(dict(v0=round(v0,2),v1=b,vos=[(i,0.1)],mute_until=round(a-0.05-v0,2),q=i))
parts.append(dict(v0=290.90,v1=293.55,vos=[],mute_until=0,q=None))
json.dump(dict(parts=parts,ugc_at=ugc_at),open('cut.json','w'),indent=0)
for k,p in enumerate(parts):
    L=p['v1']-p['v0']
    af=f"[0:a]volume=enable='lt(t,{p['mute_until']})':volume=0,afade=t=in:d=0.02,afade=t=out:st={L-0.03}:d=0.03[o]"
    cmd=['ffmpeg','-v','error','-y','-ss',str(p['v0']),'-to',str(p['v1']),'-i','../reel9_dl/main.mp4']
    labs=[]
    for j,(vi,at) in enumerate(p['vos']):
        cmd+=['-i',f'vo/t{vi}.wav']
        af+=f";[{j+1}:a]adelay={int(at*1000)},volume=1.6,apad[v{j}]"; labs.append(f'[v{j}]')
    af+=f";[o]{''.join(labs)}amix=inputs={1+len(labs)}:duration=first:normalize=0[a]" if labs else ';[o]anull[a]'
    cmd+=['-filter_complex',af,'-map','0:v','-map','[a]','-vf','scale=1080:1920,fps=30','-c:v','libx264','-crf','16','-preset','fast','-c:a','aac','-b:a','192k','-ar','48000',f'parts/{k:02d}.mp4']
    subprocess.run(cmd,check=True)
