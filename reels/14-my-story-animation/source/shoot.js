const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const pl=JSON.parse(fs.readFileSync('../plan.json','utf8'));fs.mkdirSync('../caps',{recursive:true});
const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+path.resolve('cap.html'));await p.evaluate(()=>document.fonts.ready);
for(let i=0;i<pl.caps.length;i++){const s=pl.caps[i][0].replace(/[|]/g,'<br>');
 await p.evaluate(s=>{document.getElementById('c').innerHTML=s;document.getElementById('b').style.display='none'},s);
 await p.screenshot({path:`../caps/c${String(i).padStart(2,'0')}.png`,omitBackground:true});}
const pos=[[160,760],[560,620],[330,480]];
for(let i=0;i<3;i++){await p.evaluate(([t,x,y])=>{document.getElementById('c').innerHTML='';const e=document.getElementById('b');e.style.display='block';e.textContent='+$'+t;e.style.left=x+'px';e.style.top=y+'px'},[pl.badges[i][0],...pos[i]]);
 await p.screenshot({path:`../caps/b${i}.png`,omitBackground:true});}
await b.close();})();
