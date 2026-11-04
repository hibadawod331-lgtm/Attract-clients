const {chromium}=require('playwright'); const fs=require('fs'); const path=require('path');
(async()=>{
  const [,,mode,outdir,fromF,toF]=process.argv; const FPS=30;
  const tl=JSON.parse(fs.readFileSync('timeline.json','utf8'));
  fs.mkdirSync(outdir,{recursive:true});
  const b=await chromium.launch(); const p=await b.newPage({viewport:{width:1080,height:1920}});
  await p.goto('file://'+path.resolve('overlay.html')); await p.evaluate(()=>document.fonts.ready);
  await p.evaluate(([tl,mode])=>setup(tl,mode),[tl,mode]);
  let last=null,lastFile=null,shots=0;
  const frames=[];
  for(let f=+fromF; f<+toF; f++){
    const t=f/FPS;
    
    const key=await p.evaluate(t=>render(t),t);
    const file=path.join(outdir,String(f).padStart(5,'0')+'.png');
    if(key===last){ fs.copyFileSync(lastFile,file);} else { await p.screenshot({path:file,omitBackground:true}); shots++; last=key; lastFile=file;}
  }
  console.log(mode,'shots',shots); await b.close();
})();
