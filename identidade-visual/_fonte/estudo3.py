"""Página do estudo 3: conceitos criativos de símbolo, já com a Prata."""
import sys
import gerar as g, criativo as cr

FONTS = sys.argv[1]
NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
prata = g.Txt(f"{FONTS}/prata-400.ttf")
TAG = g.TAG_FULL

def word(color, cls, text=g.WORD, track=0.14, font=None):
    t = font or prata; size = 100
    d, w = t.path(text, size, track, 0, 0); cap = t.cap_h(size)
    return f'<svg class="{cls}" viewBox="-2 {-cap-2:.1f} {w+4:.1f} {cap+4:.1f}" role="img" aria-label="{text}"><path fill="{color}" d="{d}"/></svg>'

def tag(color, cls):
    t = g.inter; size = 100
    d, w = t.path(TAG, size, 0.2, 0, 0); cap = t.cap_h(size); top = cap * 1.32
    return f'<svg class="{cls}" viewBox="-2 {-top:.1f} {w+4:.1f} {top+4:.1f}" role="img" aria-label="{TAG}"><path fill="{color}" d="{d}"/></svg>'

def sym(k, color, px=None, small=False, sw=None, cls=""):
    return cr.svg(k, color, px, sw if sw else (4.6 if small else 2.6), small, cls=cls)

ORDER = ["portal", "alvorada", "didone", "plantabaixa"]
NOTES = {
  "portal": ("Recomendado", "Lê bem até 24 px. O arco funciona como moldura do perfil sem ser círculo nem escudo. Atenção: arcos estão em alta em marcas de decoração, então o diferencial está no pendente e no piso que atravessa o vão."),
  "alvorada": ("Mais ousado", "Nenhuma marca de móveis de fora de Brasília poderia usar. Atenção: a coluna do Alvorada aparece em muitos símbolos da cidade; o desenho precisa continuar sendo sofá primeiro."),
  "didone": ("Mais tipográfico", "Amarra símbolo e nome na mesma linguagem. Atenção: o contraste exige impressão boa; em bordado e carimbo pede a versão de traço único."),
  "plantabaixa": ("Mais conceitual", "Fala de projeto e de casa inteira. Atenção: quem não é da área pode demorar a reconhecer o sofá visto de cima."),
}

def card(k):
    c = cr.C[k]; badge, note = NOTES[k]
    rec = " rec" if k == "portal" else ""
    tests = "".join(f'<figure><div class="tb">{sym(k, NAVY, px, px <= 32, 3.2 if px == 48 else None)}</div><figcaption>{px} px</figcaption></figure>' for px in (48, 32, 24))
    return f'''<section class="cc{rec}" id="{k}" aria-labelledby="h-{k}">
  <div class="cc-head"><div><h2 id="h-{k}">{c["title"]}</h2><p class="lema">{c["lema"]}</p></div><span class="pill">{badge}</span></div>
  <div class="cc-grid">
    <div class="big light">{sym(k, NAVY, None, False, 2.0, "bigs")}</div>
    <div class="big dark">{sym(k, LINEN, None, False, 1.7, "bigs")}</div>
    <div class="cc-text">
      <p class="ideia">{c["ideia"]}</p>
      <p class="nt">{note}</p>
      <div class="tests">{tests}</div>
    </div>
  </div>
  <div class="locks">
    <div class="lk light"><div class="lh">{sym(k, NAVY, None, False, 3.0, "lh-i")}<div class="lh-t">{word(NAVY, "lh-w")}{tag(NAVY, "lh-tag")}</div></div></div>
    <div class="lk dark"><div class="lv">{sym(k, LINEN, None, False, 2.4, "lv-i")}{word(LINEN, "lv-w")}</div></div>
    <div class="lk avatar-wrap"><div class="avatar">{sym(k, LINEN, None, False, 3.4)}</div></div>
  </div>
</section>'''

nav = "".join(f'<a href="#{k}">{sym(k, NAVY, 34, False, 3.4)}<span>{cr.C[k]["title"]}</span></a>' for k in ORDER)

def main():
  html = f'''<title>Nobre Living · Símbolos Autorais</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Prata&family=Inter:wght@300;400;600&display=swap">
<style>
/* Layout: um bloco largo por conceito (símbolo grande claro/escuro + texto), seguido das assinaturas com a Prata. Tema único, de marca. */
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
.fixed {{ display: flex; flex-wrap: wrap; gap: 8px 24px; margin-top: 22px; color: rgba(245,242,236,.75); font-size: 14px; }}
.fixed b {{ color: var(--linen); font-weight: 600; }}
.nav {{ display: flex; flex-wrap: wrap; gap: 10px; margin-top: 30px; }}
.nav a {{ display: inline-flex; align-items: center; gap: 10px; background: var(--linen); color: var(--navy); text-decoration: none; padding: 6px 16px 6px 8px; font-weight: 600; font-size: 14px; }}
.nav a:focus-visible, .nav a:hover {{ outline: 1px solid var(--gold); outline-offset: 2px; }}
.cc {{ padding-block: 64px 8px; }}
.cc + .cc {{ border-top: 1px solid var(--line); margin-top: 56px; }}
.cc-head {{ display: flex; justify-content: space-between; align-items: end; gap: 16px; margin-bottom: 24px; }}
.cc-head h2 {{ font-size: clamp(36px, 6vw, 56px); line-height: 1; }}
.lema {{ font: 300 19px/1.4 var(--text); color: var(--muted); margin: 8px 0 0; }}
.pill {{ font: 600 11px/1 var(--text); letter-spacing: .1em; text-transform: uppercase; color: var(--navy); background: var(--paper); border: 1px solid var(--line); padding: 7px 10px; white-space: nowrap; }}
.rec .pill {{ background: var(--gold); border-color: var(--gold); }}
.cc-grid {{ display: grid; grid-template-columns: 1fr 1fr 1.15fr; gap: 16px; align-items: stretch; }}
.big {{ aspect-ratio: 1; max-width: 100%; display: grid; place-items: center; }}
.big.light {{ background: var(--paper); border: 1px solid var(--line); }}
.big.dark {{ background: var(--navy); }}
.bigs {{ width: 86%; height: auto; }}
.cc-text {{ min-width: 0; display: flex; flex-direction: column; gap: 14px; padding-left: 8px; }}
.ideia {{ font: 400 21px/1.45 var(--display); color: var(--navy); margin: 0; text-wrap: pretty; }}
.nt {{ margin: 0; font-size: 14px; color: var(--muted); }}
.tests {{ display: flex; gap: 10px; margin-top: auto; }}
.tests figure {{ margin: 0; text-align: center; }}
.tb {{ width: 72px; height: 72px; display: grid; place-items: center; background: var(--paper); border: 1px solid var(--line); }}
.tests figcaption {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}
.locks {{ display: grid; grid-template-columns: 1.6fr 1fr 0.6fr; gap: 16px; margin-top: 16px; }}
.lk {{ display: grid; place-items: center; padding: 36px 28px; min-height: 220px; min-width: 0; }}
.lk.light {{ background: var(--paper); border: 1px solid var(--line); }}
.lk.dark {{ background: var(--navy); }}
.lk.avatar-wrap {{ background: transparent; padding: 0; }}
.lh {{ display: flex; align-items: center; gap: 5%; width: 100%; max-width: 480px; }}
.lh-i {{ width: 25%; height: auto; flex: none; }}
.lh-t {{ flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 9px; }}
.lh-w, .lh-tag {{ width: 100%; height: auto; display: block; }}
.lh-tag {{ padding-top: 9px; border-top: 1px solid var(--gold); }}
.lv {{ display: flex; flex-direction: column; align-items: center; gap: 8px; width: 100%; max-width: 240px; }}
.lv-i {{ width: 62%; height: auto; }}
.lv-w {{ width: 100%; height: auto; }}
.avatar {{ width: 100%; max-width: 160px; aspect-ratio: 1; border-radius: 50%; background: var(--navy); display: grid; place-items: center; }}
.avatar svg {{ width: 74%; height: auto; }}
.decide {{ margin-top: 72px; background: var(--navy); }}
.decide .wrap {{ padding-block: 60px; display: grid; grid-template-columns: 1fr 1.3fr; gap: 48px; }}
.decide h2 {{ color: var(--linen); font-size: clamp(30px, 4.5vw, 42px); line-height: 1.1; }}
.decide p, .decide li {{ color: rgba(245,242,236,.88); max-width: 62ch; }}
.decide ol {{ margin: 0; padding-left: 20px; display: grid; gap: 10px; }}
.decide b {{ color: var(--linen); }}
@media (max-width: 900px) {{
  .cc-grid {{ grid-template-columns: 1fr 1fr; }}
  .cc-text {{ grid-column: 1 / -1; padding-left: 0; }}
  .locks {{ grid-template-columns: 1fr 1fr; }}
  .lk.light {{ grid-column: 1 / -1; }}
  .decide .wrap {{ grid-template-columns: 1fr; }}
}}
@media (max-width: 480px) {{
  .cc-head {{ flex-direction: column; align-items: start; }}
  .lk {{ min-height: 180px; padding: 28px 18px; }}
}}
</style>

<header class="top"><div class="wrap">
  <p class="eyebrow">Identidade visual · estudo 3 · 04/11/2026</p>
  <h1>Quatro símbolos com ideia própria</h1>
  <p class="lead">O sofá continua no centro, mas agora cada símbolo conta uma história: a cidade, a fonte, o propósito ou o projeto. Todos já aparecem com a Prata e a linha de categoria atual.</p>
  <div class="fixed"><span><b>Fonte:</b> Prata</span><span><b>Linha:</b> Móveis e estofados · Brasília</span><span><b>Cores:</b> marinho, linho, grafite, dourado</span></div>
  <nav class="nav" aria-label="Conceitos">{nav}</nav>
</div></header>

<main><div class="wrap">
{"".join(card(k) for k in ORDER)}
</div>
<section class="decide" aria-labelledby="h-d"><div class="wrap">
  <div><p class="eyebrow">Recomendação</p><h2 id="h-d">Portal, com Alvorada como alternativa ousada</h2></div>
  <div>
    <p>O Portal desenha o propósito da marca: a casa pronta para receber. O arco dá ao símbolo uma silhueta própria, cabe no perfil redondo do Instagram e continua legível a 24 px. O pendente e o piso sugerem ambiente sem precisar listar tudo o que a loja vende.</p>
    <p>Se a vontade for ter o símbolo mais memorável possível, a Alvorada é a escolha. Ela amarra a marca a Brasília de um jeito que nenhuma concorrente de fora consegue copiar.</p>
    <ol>
      <li><b>Qual conceito segue?</b> Pode ser um destes ou a mistura de dois, como o Portal com o sofá da Alvorada.</li>
      <li><b>Algum elemento que você quer ver dentro do ambiente?</b> Quadro, vaso, tapete, poltrona.</li>
    </ol>
  </div>
</div></section>
</main>
'''
  open(sys.argv[2], "w").write(html)
  print("ok", len(html))

if __name__ == "__main__":
    main()
