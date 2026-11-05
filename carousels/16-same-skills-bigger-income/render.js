const {chromium} = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1080, height: 1350}, deviceScaleFactor: 1});
  await p.goto('file://' + path.resolve('carousel.html'));
  await p.evaluate(() => document.fonts.ready);
  const els = await p.$$('section');
  for (let i = 0; i < els.length; i++) await els[i].screenshot({path: `slide_${i + 1}.png`});
  console.log(els.length); await b.close();
})();
