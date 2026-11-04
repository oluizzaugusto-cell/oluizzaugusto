// Gera prévias PNG dos modelos, com Prata e Inter carregadas localmente.
// Uso: node kit_previa.js <pasta-fontes> <pasta-kit>
const fs = require('fs'), path = require('path'); const { chromium } = require('playwright');
const [F, KIT] = process.argv.slice(2);
const M = path.join(KIT, 'modelos'), OUT = path.join(M, 'previa'); fs.mkdirSync(OUT, { recursive: true });
const face = (fam, file, w) => `@font-face{font-family:'${fam}';font-weight:${w};src:url('file://${F}/${file}')}`;
const css = face('Prata', 'prata-400.ttf', 400) + ['300','400','500','600'].map(w => face('Inter', `inter-${w}.ttf`, w)).join('');
(async () => {
  const b = await chromium.launch();
  for (const f of fs.readdirSync(M).filter(f => f.endsWith('.svg'))) {
    let s = fs.readFileSync(path.join(M, f), 'utf8');
    const vb = s.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
    const W = vb[2] > 300 ? Math.min(vb[2], 1080) : 1080 * (vb[2] / Math.max(vb[2], vb[3]));
    const w = Math.round(vb[2] > 300 ? W : (vb[2] >= vb[3] ? 900 : 640)); const h = Math.round(w * vb[3] / vb[2]);
    s = s.replace(/<svg([^>]*?) width="[^"]*" height="[^"]*"/, `<svg$1 width="${w}" height="${h}"`);
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await p.setContent(`<html><head><style>${css} body{margin:0}</style></head><body>${s}</body></html>`);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
    await p.screenshot({ path: path.join(OUT, f.replace('.svg', '.png')) }); await p.close();
  }
  await b.close(); console.log('previa ok');
})();
