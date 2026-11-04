"""Página do estudo 2: opções de fonte (wordmark) e de símbolo 'casa toda'."""
import sys
import gerar as g, casa

FONTS = sys.argv[1]
NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
WORD = g.WORD

FONT_OPTS = [
  ("atual", "bodoni-28-500", "Bodoni Moda 500", "Versão atual",
   "Hastes verticais do N quase no limite da espessura. Some em tamanho pequeno e em fundo escuro."),
  ("bodoni600", "bodoni-11-600", "Bodoni Moda 600, corte de texto", "Mesma família",
   "Continua dentro do briefing. Hastes mais firmes e contraste menor. O N aparece inteiro, mas o nome fica mais pesado."),
  ("prata", "prata-400", "Prata", "Recomendada",
   "Didone com traços finos mais robustos e versais largas. Mantém o contraste elegante e o N fica nítido até em etiqueta."),
  ("playfair", "playfair-500", "Playfair Display 500", "Alternativa",
   "Didone de transição, contraste moderado. Muito legível, porém comum em sites e convites."),
  ("gilda", "gilda-400", "Gilda Display", "Mais próxima de 2025",
   "Serifa clássica de contraste baixo, parecida com o logo antigo. Mais suave, menos Didone."),
]
TXT = {k: g.Txt(f"{FONTS}/{f}.ttf") for k, f, *_ in FONT_OPTS}

def word_svg(key, color, cls="wm", text=WORD, track=0.14):
    t = TXT[key]; size = 100
    d, w = t.path(text, size, track, 0, 0)
    cap = t.cap_h(size)
    pad = 2
    return (f'<svg class="{cls}" viewBox="{-pad} {-cap-pad:.1f} {w+2*pad:.1f} {cap+2*pad:.1f}" role="img" '
            f'aria-label="{text}"><path fill="{color}" d="{d}"/></svg>')

def sym(key, color, px=None, small=False, sw=None, cls=""):
    s = casa.svg(key, color, px, sw if sw else (4.6 if small else 2.6), small)
    return s.replace("<svg ", f'<svg class="{cls}" role="img" aria-label="Símbolo" ', 1) if cls else s

def font_card(k, f, name, tagline, note):
    rec = " rec" if tagline == "Recomendada" else ""
    return f'''<article class="fc{rec}">
  <header><h3>{name}</h3><span class="pill">{tagline}</span></header>
  <div class="fc-big">{word_svg(k, NAVY)}</div>
  <div class="fc-row">
    <div class="fc-n">{word_svg(k, NAVY, "n", "N", 0)}</div>
    <div class="fc-small"><div class="sm-light">{word_svg(k, NAVY, "wm-s")}</div><div class="sm-dark">{word_svg(k, LINEN, "wm-s")}</div></div>
  </div>
  <p>{note}</p>
</article>'''

def sym_card(k):
    st = casa.STUDIES[k]
    rec = " rec" if k == "pendente" else ""
    tests = "".join(f'<figure><div class="tb">{sym(k, NAVY, px, px <= 32, 3.2 if px == 48 else None)}</div><figcaption>{px} px</figcaption></figure>' for px in (48, 32, 24))
    return f'''<article class="sc{rec}">
  <header><h3>{st["title"]}</h3>{'<span class="pill">Recomendado</span>' if rec else ''}</header>
  <div class="sc-pair"><div class="sp light">{sym(k, NAVY, None, False, 2.2, "big")}</div><div class="sp dark">{sym(k, LINEN, None, False, 1.9, "big")}</div></div>
  <div class="tests">{tests}</div>
  <p>{st["desc"]}</p>
</article>'''

def lock_h(font, s, color):
    return f'<div class="lh">{sym(s, color, None, False, 3.0, "lh-i")}{word_svg(font, color, "lh-w")}</div>'
def lock_v(font, s, color):
    return f'<div class="lv">{sym(s, color, None, False, 2.4, "lv-i")}{word_svg(font, color, "lv-w")}</div>'

fonts_html = "".join(font_card(*o) for o in FONT_OPTS if o[0] != "atual")
syms_html = "".join(sym_card(k) for k in casa.STUDIES)

html = f'''<title>Nobre Living · Fonte e Símbolo</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Prata&family=Inter:wght@300;400;600&display=swap">
<style>
/* Layout: estudo comparativo; faixa marinho, grade de cartões por opção, combinação recomendada em destaque. Tema único, de marca. */
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
h2 {{ font-size: clamp(30px, 4.6vw, 42px); line-height: 1.1; }}
h3 {{ font: 600 15px/1.3 var(--text); color: var(--navy); margin: 0; }}
.eyebrow {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 0 0 14px; }}
.top {{ background: var(--navy); }}
.top .wrap {{ padding-block: 56px; }}
.top h1 {{ color: var(--linen); font-size: clamp(34px, 5.5vw, 54px); line-height: 1.08; }}
.top p.lead {{ color: rgba(245,242,236,.86); font-weight: 300; font-size: 18px; max-width: 64ch; margin: 18px 0 0; }}
section.s {{ padding-block: 60px 8px; }}
.intro {{ max-width: 68ch; color: var(--graphite); margin: 14px 0 28px; }}
.why {{ display: grid; grid-template-columns: 220px 1fr; gap: 32px; align-items: center; background: var(--paper); border: 1px solid var(--line); padding: 28px; margin-bottom: 28px; }}
.why .bigN {{ width: 100%; height: auto; }}
.why p {{ margin: 0; max-width: 60ch; }}
.cur-l {{ font: 600 11px/1 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin: 0 0 10px !important; }}
.cur {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }}
.cur > svg {{ background: var(--linen); padding: 10px 12px; width: 144px; box-sizing: content-box; }}
.cur-d {{ background: var(--navy); padding: 10px 12px; display: flex; }}
.grid-f {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
.fc, .sc {{ background: var(--paper); border: 1px solid var(--line); padding: 22px; display: flex; flex-direction: column; gap: 18px; min-width: 0; }}
.fc.rec, .sc.rec {{ outline: 2px solid var(--gold); outline-offset: -2px; }}
.fc header, .sc header {{ display: flex; justify-content: space-between; align-items: center; gap: 12px; }}
.pill {{ font: 600 11px/1 var(--text); letter-spacing: .1em; text-transform: uppercase; color: var(--navy); background: var(--linen); padding: 6px 9px; white-space: nowrap; }}
.rec .pill {{ background: var(--gold); color: var(--navy); }}
.fc-big .wm {{ width: 100%; height: auto; display: block; }}
.fc-row {{ display: grid; grid-template-columns: 76px 1fr; gap: 16px; align-items: stretch; }}
.fc-n {{ background: var(--linen); display: grid; place-items: center; padding: 10px; }}
.fc-n .n {{ width: 100%; height: auto; }}
.fc-small {{ display: grid; gap: 6px; }}
.sm-light, .sm-dark {{ display: flex; align-items: center; padding: 10px 12px; }}
.sm-light {{ background: var(--linen); }} .sm-dark {{ background: var(--navy); }}
.wm-s {{ width: 120px; height: auto; display: block; }}
.fc p, .sc p {{ margin: 0; font-size: 14px; color: var(--muted); }}
.grid-s {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }}
.sc-pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
.sp {{ aspect-ratio: 1; max-width: 100%; display: grid; place-items: center; }}
.sp.light {{ background: var(--linen); }} .sp.dark {{ background: var(--navy); }}
.sp .big {{ width: 88%; height: auto; }}
.tests {{ display: flex; gap: 10px; }}
.tests figure {{ margin: 0; text-align: center; }}
.tb {{ width: 72px; height: 72px; display: grid; place-items: center; background: var(--linen); }}
.tests figcaption {{ font-size: 12px; color: var(--muted); margin-top: 4px; }}
.combo {{ margin-top: 64px; background: var(--navy); }}
.combo .wrap {{ padding-block: 60px; }}
.combo h2 {{ color: var(--linen); }}
.combo .intro {{ color: rgba(245,242,236,.86); }}
.boards {{ display: grid; grid-template-columns: 1.5fr 1fr; gap: 16px; }}
.board {{ display: grid; place-items: center; padding: 48px 32px; min-height: 260px; min-width: 0; }}
.board.light {{ background: var(--linen); }} .board.dark {{ background: var(--navy); border: 1px solid rgba(245,242,236,.22); }}
.lh {{ display: flex; align-items: center; gap: 4%; width: 100%; max-width: 460px; }}
.lh-i {{ width: 27%; height: auto; flex: none; }}
.lh-w {{ flex: 1; min-width: 0; height: auto; }}
.lv {{ display: flex; flex-direction: column; align-items: center; gap: 6px; width: 100%; max-width: 260px; }}
.lv-i {{ width: 64%; height: auto; }}
.lv-w {{ width: 100%; height: auto; }}
.minis {{ display: flex; flex-wrap: wrap; gap: 16px; margin-top: 16px; align-items: center; }}
.avatar {{ width: 120px; height: 120px; border-radius: 50%; background: var(--linen); display: grid; place-items: center; }}
.avatar svg {{ width: 74%; height: auto; }}
.minis .lab {{ color: rgba(245,242,236,.75); font-size: 13px; }}
.decide .wrap {{ padding-block: 60px 72px; }}
.qs {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 24px; }}
.q {{ background: var(--paper); border: 1px solid var(--line); padding: 22px; min-width: 0; }}
.q h3 {{ margin-bottom: 8px; }}
.q p, .q li {{ font-size: 15px; margin: 0; }}
.q ul {{ margin: 10px 0 0; padding-left: 18px; display: grid; gap: 4px; }}
.q code {{ font: 600 12px/1 var(--text); letter-spacing: .12em; color: var(--navy); }}
@media (max-width: 760px) {{
  .why, .boards, .qs {{ grid-template-columns: 1fr; }}
  .why .bigN {{ max-width: 160px; }}
  .grid-f, .grid-s {{ grid-template-columns: 1fr; }}
}}
</style>

<header class="top"><div class="wrap">
  <p class="eyebrow">Identidade visual · estudo 2 · 04/11/2026</p>
  <h1>Fonte e símbolo</h1>
  <p class="lead">Dois ajustes pedidos: o N que parece apagado e um símbolo que fale da casa toda, não só do sofá. Abaixo, as opções de cada um e a combinação que recomendo.</p>
</div></header>

<main>
<div class="wrap">
  <section class="s" aria-labelledby="h-f">
    <p class="eyebrow">1 · Fonte do nome</p>
    <h2 id="h-f">Por que o N some</h2>
    <div class="why" style="margin-top:24px">
      {word_svg("atual", NAVY, "bigN", "N", 0)}
      <div><p class="cur-l">Versão atual · Bodoni Moda 500</p><div class="cur">{word_svg("atual", NAVY, "wm-s")}<span class="cur-d">{word_svg("atual", LINEN, "wm-s")}</span></div>
      <p>Nas Didone, como a Bodoni, a diagonal do N é grossa e as duas hastes verticais são finíssimas. Em tamanho grande isso é elegante. Em etiqueta, no perfil do Instagram ou sobre marinho, as hastes somem e o N vira uma barra inclinada. A correção é escolher um corte com traços finos mais robustos, sem perder o contraste que dá o ar sofisticado.</p></div>
    </div>
    <div class="grid-f">{fonts_html}</div>
  </section>

  <section class="s" aria-labelledby="h-s">
    <p class="eyebrow">2 · Símbolo</p>
    <h2 id="h-s">Do sofá para a casa toda</h2>
    <p class="intro">O sofá continua sendo o centro, com o desenho da Planta refinada. Em cada opção ele ganha uma peça que amplia a leitura para a casa. Os testes de 32 e 24 px usam a versão de redução.</p>
    <div class="grid-s">{syms_html}</div>
  </section>
</div>

<section class="combo" aria-labelledby="h-c"><div class="wrap">
  <p class="eyebrow">Combinação recomendada</p>
  <h2 id="h-c">Prata com sofá e pendente</h2>
  <p class="intro">O pendente mantém o símbolo simétrico e equilibrado no quadrado do perfil. A Prata segura o N em qualquer tamanho. Juntos, ficam mais firmes que a versão anterior sem perder a calma.</p>
  <div class="boards">
    <div class="board light">{lock_h("prata", "pendente", NAVY)}</div>
    <div class="board dark">{lock_v("prata", "pendente", LINEN)}</div>
  </div>
  <div class="minis">
    <div class="avatar">{sym("pendente", NAVY, None, False, 3.2)}</div>
    <span class="lab">Perfil @nobreliving</span>
  </div>
</div></section>

<section class="decide" aria-labelledby="h-d"><div class="wrap">
  <p class="eyebrow">Para decidir</p>
  <h2 id="h-d">Quatro respostas e eu fecho a marca</h2>
  <div class="qs">
    <div class="q"><h3>1. Fonte</h3><p>Prata (recomendada), Bodoni Moda 600, Playfair Display ou Gilda Display. Os títulos do material podem continuar em Bodoni Moda.</p></div>
    <div class="q"><h3>2. Símbolo</h3><p>Pendente (recomendado), luminária de piso, mesa lateral com abajur ou luminária de arco.</p></div>
    <div class="q"><h3>3. Linha de categoria</h3><p>Hoje é <code>MÓVEIS E ESTOFADOS · BRASÍLIA</code>. Com a casa toda, sugiro:</p>
      <ul><li><code>MÓVEIS PARA A CASA · BRASÍLIA</code></li><li><code>CASA, MÓVEIS E ESTOFADOS · BRASÍLIA</code></li><li>Manter a atual</li></ul></div>
    <div class="q"><h3>4. Iluminação</h3><p>A Nobre Living vende luminárias, ou a luminária no símbolo é só para sugerir ambiente? Isso muda o que o post e o catálogo podem mostrar.</p></div>
  </div>
</div></section>
</main>
'''
open(sys.argv[2], "w").write(html)
print("ok", len(html))
