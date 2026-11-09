// node pdf.js a.html b.html ...  -> a.pdf b.pdf (A4, running header + page numbers)
const {chromium} = require('playwright'); const path = require('path'); const fs = require('fs');
const font = w => `@font-face{font-family:P;font-weight:${w};src:url(data:font/woff2;base64,${
  fs.readFileSync(path.join(__dirname, 'fonts', `ibm-plex-sans-arabic-${w}.woff2`)).toString('base64')})}`;
const F = font(400) + font(500);
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const f of process.argv.slice(2)) {
    await p.goto('file://' + path.resolve(f)); await p.evaluate(() => document.fonts.ready);
    const head = await p.$eval('meta[name=running-head]', m => m.content);
    const st = `<style>${F}*{font-family:P}</style>`;
    await p.pdf({path: path.resolve(f).replace(/\.html$/, '.pdf'), format: 'A4', printBackground: true,
      displayHeaderFooter: true, preferCSSPageSize: true,
      headerTemplate: `${st}<div dir="rtl" style="width:100%;font-size:8px;color:#999;padding:0 20mm;display:flex;justify-content:space-between"><span>${head}</span><span style="color:#F2531E;font-weight:500">برنامج الإرشاد الفردي</span></div>`,
      footerTemplate: `${st}<div dir="rtl" style="width:100%;font-size:8px;color:#999;text-align:center">صفحة <span class="pageNumber"></span> من <span class="totalPages"></span> · <span dir="ltr">@itscoachhiba</span></div>`});
    console.log(f);
  }
  await b.close();
})();
