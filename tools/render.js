const {chromium}=require('playwright');const path=require('path');
(async()=>{const dir=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+path.join(dir,'carousel.html'));await p.evaluate(()=>document.fonts.ready);
const s=await p.$$('.slide');for(let i=0;i<s.length;i++){await s[i].screenshot({path:path.join(dir,`slide_${i+1}.png`)});}
console.log(s.length,'slides');await b.close();})();
