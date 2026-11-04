"""Página do estudo 4: variações do Portal."""
import sys
import gerar as g, portal as P
from estudo3 import word, tag  # reaproveita wordmark Prata e linha de categoria

NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
REC = "pendente-tapete"
ORDER = ["pendente", "quadro", "pendente-tapete", "quadro-tapete", "vaso", "completo"]
ELEM = {"pendente": ["Pendente"], "quadro": ["Quadro"], "pendente-tapete": ["Pendente", "Tapete"],
        "quadro-tapete": ["Quadro", "Tapete"], "vaso": ["Pendente", "Vaso"], "completo": ["Quadro", "Vaso", "Tapete"]}
LEIT = {"pendente": "Excelente", "quadro": "Excelente", "pendente-tapete": "Muito boa", "quadro-tapete": "Muito boa",
        "vaso": "Boa", "completo": "Limitada"}

def sym(k, color, px=None, small=False, sw=None, cls=""):
    return P.svg(k, color, px, sw if sw else (4.6 if small else 2.4), small, cls=cls)

def card(k):
    v = P.V[k]; rec = " rec" if k == REC else ""
    chips = "".join(f'<span class="chip">{e}</span>' for e in ELEM[k])
    tests = "".join(f'<figure><div class="tb">{sym(k, NAVY, px, True)}</div><figcaption>{px} px</figcaption></figure>' for px in (32, 24))
    return f'''<article class="vc{rec}" aria-labelledby="h-{k}">
  <header><h2 id="h-{k}">{v["title"]}</h2>{'<span class="pill">Recomendado</span>' if rec else ''}</header>
  <div class="chips">{chips}</div>
  <div class="pair"><div class="sq light">{sym(k, NAVY, None, False, 2.0, "bigs")}</div><div class="sq dark">{sym(k, LINEN, None, False, 1.8, "bigs")}</div></div>
  <div class="row">
    <div class="tests">{tests}</div>
    <div class="av">{sym(k, LINEN, None, False, 3.0)}</div>
  </div>
  <p class="desc">{v["desc"]}</p>
  <p class="leit">Leitura em tamanho pequeno: <b>{LEIT[k]}</b></p>
</article>'''

html = f'''<title>Nobre Living · Portal</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Prata&family=Inter:wght@300;400;600&display=swap">
<style>
/* Layout: grade 3 × 2 de variações comparáveis, depois a recomendada aplicada. Tema único, de marca. */
:root {{
  --navy: {NAVY}; --linen: {LINEN}; --graphite: {GRAF}; --gold: {GOLD};
  --paper: #FBFAF7; --muted: #5E6470; --line: rgba(20,38,61,.14);
  --display: "Prata", Georgia, "Times New Roman", serif;
  --text: "Inter", system-ui, "Segoe UI", sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--linen); color: var(--graphite); font: 400 16px/1.6 var(--text); }}
.wrap {{ max-width: 1160px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1, h2 {{ font-family: var(--display); font-weight: 400; color: var(--navy); margin: 0; text-wrap: balance; }}
.eyebrow {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 0 0 14px; }}
.top {{ background: var(--navy); }}
.top .wrap {{ padding-block: 56px; }}
.top h1 {{ color: var(--linen); font-size: clamp(34px, 5.5vw, 54px); line-height: 1.08; }}
.top .lead {{ color: rgba(245,242,236,.86); font-weight: 300; font-size: 18px; max-width: 64ch; margin: 18px 0 0; }}
.grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; padding-block: 48px 8px; }}
.vc {{ background: var(--paper); border: 1px solid var(--line); padding: 20px; display: flex; flex-direction: column; gap: 14px; min-width: 0; }}
.vc.rec {{ outline: 2px solid var(--gold); outline-offset: -2px; }}
.vc header {{ display: flex; justify-content: space-between; align-items: center; gap: 10px; }}
.vc h2 {{ font-size: 26px; line-height: 1.1; }}
.pill {{ font: 600 11px/1 var(--text); letter-spacing: .1em; text-transform: uppercase; color: var(--navy); background: var(--gold); padding: 6px 9px; white-space: nowrap; }}
.chips {{ display: flex; flex-wrap: wrap; gap: 6px; }}
.chip {{ font: 600 11px/1 var(--text); letter-spacing: .08em; text-transform: uppercase; color: var(--navy); border: 1px solid var(--line); padding: 5px 8px; }}
.pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.sq {{ aspect-ratio: 1; max-width: 100%; display: grid; place-items: center; }}
.sq.light {{ background: var(--linen); }} .sq.dark {{ background: var(--navy); }}
.bigs {{ width: 92%; height: auto; }}
.row {{ display: flex; justify-content: space-between; align-items: end; gap: 10px; }}
.tests {{ display: flex; gap: 8px; }}
.tests figure {{ margin: 0; text-align: center; }}
.tb {{ width: 60px; height: 60px; display: grid; place-items: center; background: var(--linen); }}
.tests figcaption {{ font-size: 12px; color: var(--muted); margin-top: 3px; }}
.av {{ width: 84px; height: 84px; border-radius: 50%; background: var(--navy); display: grid; place-items: center; flex: none; }}
.av svg {{ width: 78%; height: auto; }}
.desc {{ margin: 0; font-size: 14px; }}
.leit {{ margin: auto 0 0; font-size: 13px; color: var(--muted); }}
.leit b {{ color: var(--navy); }}
.apply {{ margin-top: 56px; background: var(--navy); }}
.apply .wrap {{ padding-block: 60px; }}
.apply h2 {{ color: var(--linen); font-size: clamp(30px, 4.5vw, 42px); line-height: 1.1; }}
.apply .lead2 {{ color: rgba(245,242,236,.86); max-width: 64ch; margin: 14px 0 28px; }}
.boards {{ display: grid; grid-template-columns: 1.6fr 1fr; gap: 16px; }}
.board {{ display: grid; place-items: center; padding: 44px 28px; min-height: 260px; min-width: 0; }}
.board.light {{ background: var(--linen); }} .board.dark {{ border: 1px solid rgba(245,242,236,.22); }}
.lh {{ display: flex; align-items: center; gap: 5%; width: 100%; max-width: 500px; }}
.lh-i {{ width: 25%; height: auto; flex: none; }}
.lh-t {{ flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 9px; }}
.lh-w, .lh-tag {{ width: 100%; height: auto; display: block; }}
.lh-tag {{ padding-top: 9px; border-top: 1px solid var(--gold); }}
.lv {{ display: flex; flex-direction: column; align-items: center; gap: 8px; width: 100%; max-width: 240px; }}
.lv-i {{ width: 62%; height: auto; }}
.lv-w {{ width: 100%; height: auto; }}
.q {{ margin-top: 28px; color: rgba(245,242,236,.9); max-width: 70ch; }}
.q b {{ color: var(--linen); }}
@media (max-width: 960px) {{ .grid {{ grid-template-columns: repeat(2, 1fr); }} .boards {{ grid-template-columns: 1fr; }} }}
@media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
</style>

<header class="top"><div class="wrap">
  <p class="eyebrow">Identidade visual · estudo 4 · 04/11/2026</p>
  <h1>Portal com a sala montada</h1>
  <p class="lead">O arco e o sofá ficam; o que muda é o que está na sala. Seis combinações de pendente, quadro, vaso e tapete, cada uma testada em tamanho pequeno e no perfil redondo.</p>
</div></header>

<main>
<div class="wrap"><div class="grid">{"".join(card(k) for k in ORDER)}</div></div>
<section class="apply" aria-labelledby="h-a"><div class="wrap">
  <p class="eyebrow">Recomendada, aplicada</p>
  <h2 id="h-a">Pendente + tapete</h2>
  <p class="lead2">A luz do alto e o tapete no chão fecham a cena de cima a baixo. O tapete em perspectiva dá profundidade sem pesar, e o símbolo continua legível a 24 px. Vaso e quadro funcionam melhor como ícones de apoio no Instagram do que dentro do símbolo principal.</p>
  <div class="boards">
    <div class="board light"><div class="lh">{sym(REC, NAVY, None, False, 2.8, "lh-i")}<div class="lh-t">{word(NAVY, "lh-w")}{tag(NAVY, "lh-tag")}</div></div></div>
    <div class="board dark"><div class="lv">{sym(REC, LINEN, None, False, 2.2, "lv-i")}{word(LINEN, "lv-w")}</div></div>
  </div>
  <p class="q"><b>Qual segue?</b> Se escolher, eu fecho o símbolo final e entrego o kit: versões A a E em SVG e PNG, favicon, os modelos das aplicações e o manual da marca.</p>
</div></section>
</main>
'''
open(sys.argv[2], "w").write(html)
print("ok", len(html))
