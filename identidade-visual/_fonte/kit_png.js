// Exporta PNGs transparentes @1x/@2x/@3x, favicons e marca d'água a partir dos SVGs do kit.
// Uso: node kit_png.js <pasta-kit>
const fs = require('fs'), path = require('path');
const { chromium } = require('playwright');
const KIT = process.argv[2];
const SVG = path.join(KIT, 'svg');
const base = n => n.startsWith('nobre-living-c-') ? 512 : n.includes('vertical') ? 480 : n.includes('assinatura') || n.includes('horizontal') ? 900 : 600;

async function render(page, svgText, w, scale, out, extraCss = '', bg = 'transparent') {
  const vb = svgText.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
  const h = Math.round(w * vb[3] / vb[2]);
  await page.setViewportSize({ width: w, height: h });
  await page.setContent(`<html><body style="margin:0;background:${bg}">` +
    `<div style="width:${w}px;height:${h}px;${extraCss}">${svgText.replace(/<svg[^>]*>/, t => t.replace(/ width="[^"]*" height="[^"]*"/, '').replace('<svg ', `<svg style="width:${w}px;height:${h}px;display:block" `))}</div></body></html>`);
  await page.screenshot({ path: out, omitBackground: bg === 'transparent', clip: { x: 0, y: 0, width: w, height: h } });
}

(async () => {
  const b = await chromium.launch();
  let n = 0;
  for (const scale of [1, 2, 3]) {
    const page = await b.newPage({ deviceScaleFactor: scale });
    const dir = path.join(KIT, 'png', `@${scale}x`); fs.mkdirSync(dir, { recursive: true });
    for (const f of fs.readdirSync(SVG).filter(f => f.endsWith('.svg'))) {
      const name = f.replace('.svg', '');
      await render(page, fs.readFileSync(path.join(SVG, f), 'utf8'), base(name), scale,
        path.join(dir, `${name}${scale > 1 ? '@' + scale + 'x' : ''}.png`)); n++;
    }
    await page.close();
  }
  // favicons: versão micro em 16/32, redução em 48/64, completo em 180/512 (fundo marinho)
  const fav = path.join(KIT, 'favicon'); fs.mkdirSync(fav, { recursive: true });
  const page = await b.newPage({ deviceScaleFactor: 1 });
  const read = f => fs.readFileSync(path.join(SVG, f), 'utf8');
  const navyBg = (svg) => svg.replace('<g ', '<rect x="-8" y="-8" width="112" height="112" fill="#14263D"/><g ').replace(/viewBox="[^"]+"/, 'viewBox="-8 -8 112 112"');
  for (const [px, lvl] of [[16, 'micro'], [32, 'micro'], [48, 'reducao'], [64, 'reducao'], [180, 'icone'], [192, 'icone'], [512, 'icone']]) {
    const src = lvl === 'icone' ? 'nobre-living-c-icone-offwhite.svg' : `nobre-living-c-icone-${lvl}-offwhite.svg`;
    await render(page, navyBg(read(src)), px, 1, path.join(fav, px === 180 ? 'apple-touch-icon.png' : `favicon-${px}.png`)); n++;
  }
  fs.writeFileSync(path.join(fav, 'favicon.svg'), navyBg(read('nobre-living-c-icone-reducao-offwhite.svg')));
  // marca d'água: horizontal off-white a 55% e marinho a 45%, fundo transparente
  const wm = path.join(KIT, 'marca-dagua'); fs.mkdirSync(wm, { recursive: true });
  for (const [c, op] of [['offwhite', .55], ['marinho', .45]]) {
    for (const s of [1, 2]) {
      const p2 = await b.newPage({ deviceScaleFactor: s });
      await render(p2, read(`nobre-living-b-horizontal-${c}.svg`), 600, s,
        path.join(wm, `nobre-living-marca-dagua-${c}${s > 1 ? '@2x' : ''}.png`), `opacity:${op}`); n++;
      await p2.close();
    }
  }
  await b.close();
  console.log('png', n);
})();
