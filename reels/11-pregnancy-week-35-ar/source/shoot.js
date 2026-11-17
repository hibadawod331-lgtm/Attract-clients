const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const tl=JSON.parse(fs.readFileSync('timeline.json','utf8'));fs.mkdirSync('caps',{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve('cap.html'));await p.evaluate(()=>document.fonts.ready);
for(let i=-1;i<tl.caps.length;i++){const s=i<0?'':tl.caps[i][0].replace(/\*([^*]+)\*/g,'<b>$1</b>').replace(/[|]/g,'<br>');
 await p.evaluate(s=>{document.getElementById('c').innerHTML=s},s);
 await p.screenshot({path:`caps/${i<0?'blank':String(i).padStart(3,'0')}.png`,omitBackground:true});}
await b.close();})();
