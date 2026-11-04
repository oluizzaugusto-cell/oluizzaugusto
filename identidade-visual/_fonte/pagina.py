"""Monta a página de apresentação das direções (HTML com SVG embutido)."""
import sys
sys.argv = [sys.argv[0]] + sys.argv[1:]
import gerar as g

NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD

def icon(key, color, px, variant=None, cls=""):
    v = variant or ("small" if px <= 32 else "full")
    return (f'<svg class="{cls}" viewBox="0 0 48 48" width="{px}" height="{px}" role="img" '
            f'aria-label="Símbolo {key}">{g.icon_group(key, color, v)}</svg>')

def sec(key, which, color, px):
    return f'<svg viewBox="0 0 48 48" width="{px}" height="{px}">{g.secondary_group(key, which, color)}</svg>'

def lock(fn, key, color, cls, tag=None):
    W, H, b = fn(key, color, GOLD, tag) if tag else fn(key, color, GOLD)
    return f'<svg class="{cls}" viewBox="0 0 {W:.1f} {H:.1f}" role="img" aria-label="Nobre Living">{b}</svg>'

DIRS = [
 dict(key="fio", n="1", nome="Fio", lema="A peça já na sala",
  ideia="Uma linha de chão sobe, desenha o sofá e volta ao chão. A marca mostra o móvel no lugar dele: dentro da casa, pronta para receber.",
  logica=[("Forma", "Sofá baixo e largo, com o assento marcado. A linha de chão é o traço que só esta direção tem."),
          ("Para ela", "Fala com quem pensa na sala inteira, não na peça solta. Traduz o propósito: casa pronta para receber."),
          ("Personalidade", "Puxa o lado Amante do arquétipo. É a mais calorosa e a mais contemporânea das três.")],
  riscos="A linha de chão pode ser lida como sublinhado quando o logo fica pequeno. Por isso a versão de redução encurta o chão. No horizontal, o chão pede respiro dos dois lados."),
 dict(key="planta", n="2", nome="Planta", lema="O desenho de quem mede antes",
  ideia="O sofá desenhado como numa prancha de projeto: contorno fechado, braços, assento e pés, tudo num módulo de 4 unidades.",
  logica=[("Forma", "Elevação frontal, simétrica e completa. É a leitura mais imediata de sofá entre as três."),
          ("Para ela", "Responde ao medo número um: gastar R$ 5 mil e a peça não caber. Desenho técnico sugere medida certa, projeto e sob medida."),
          ("Personalidade", "Curador preciso. O fio dourado entre o nome e a assinatura é o único ornamento.")],
  riscos="É a mais convencional. A sofisticação depende da wordmark Didone e do espaço em branco. Tem mais linhas, então a versão de redução tira o assento e os pés."),
 dict(key="vao", n="3", nome="Vão", lema="O lugar de quem senta",
  ideia="Só o essencial: encosto e braços numa linha aberta, e o assento solto no meio. O espaço vazio entre eles é o lugar da pessoa.",
  logica=[("Forma", "Aberta embaixo, encosto alto, assento flutuando. Pede espaço em volta e entreletra bem aberta."),
          ("Para ela", "Tem cara de revista de decoração. Funciona muito bem no Instagram e em capa de destaque."),
          ("Personalidade", "Curador discreto. É a mais silenciosa e a que mais lembra ateliê.")],
  riscos="É a mais abstrata: em 16 px o assento solto perde força. A entreletra muito aberta pede corpo maior. Se a fotografia não for calorosa, a marca pode parecer distante."),
]

CRIT = [
 ("Reconhecível a 24 px", ["sim", "sim", "parcial"], "Vão: o assento solto perde força abaixo de 24 px."),
 ("Funciona em uma cor", ["sim", "sim", "sim"], "Os três símbolos são de traço único, sem preenchimento."),
 ("Legível em fundo claro e escuro", ["sim", "sim", "sim"], "Marinho sobre off-white e o inverso, 13,4:1."),
 ("Não se parece com marca conhecida", ["verificar", "verificar", "verificar"], "Depende de busca de anterioridade no INPI, ainda não feita."),
 ("Sem clichê", ["sim", "parcial", "sim"], "Planta: sofá frontal é a forma mais próxima do ícone genérico. A Didone e o módulo diferenciam."),
 ("Parece caro sem parecer caro demais", ["sim", "sim", "parcial"], "Vão pode soar distante sem foto calorosa."),
 ("Sugere móveis e serviço", ["parcial", "sim", "parcial"], "Planta remete a projeto e sob medida."),
 ("Atual em 5 anos", ["sim", "sim", "parcial"], "Minimalismo extremo envelhece junto com a moda."),
]
MARK = {"sim": ("●", "Atende"), "parcial": ("◐", "Atende em parte"), "verificar": ("○", "A verificar")}

def direction(d):
    k = d["key"]
    tests = "".join(f'<figure class="t"><div class="tbox">{icon(k, NAVY, s)}</div><figcaption>{s} px</figcaption></figure>' for s in (48, 32, 24, 16))
    tests_dark = "".join(f'<figure class="t"><div class="tbox dark">{icon(k, LINEN, s)}</div><figcaption>{s} px</figcaption></figure>' for s in (48, 32, 24, 16))
    mono = f'<figure class="t"><div class="tbox">{icon(k, GRAF, 48)}</div><figcaption>Grafite</figcaption></figure>'
    logica = "".join(f'<div class="lg"><dt>{a}</dt><dd>{b}</dd></div>' for a, b in d["logica"])
    return f'''
<section class="dir" id="{k}" aria-labelledby="h-{k}">
  <header class="dir-h">
    <p class="eyebrow">Direção {d["n"]} de 3</p>
    <h2 id="h-{k}">{d["nome"]}</h2>
    <p class="lema">{d["lema"]}</p>
  </header>
  <div class="hero-pair">
    <div class="panel light">{lock(g.lockup_horizontal, k, NAVY, "lk-h")}</div>
    <div class="panel navy">{lock(g.lockup_horizontal, k, LINEN, "lk-h", g.TAG_FULL)}</div>
  </div>
  <div class="cols">
    <div class="col-text">
      <p class="ideia">{d["ideia"]}</p>
      <dl class="logica">{logica}</dl>
      <p class="risco"><strong>Pontos de atenção.</strong> {d["riscos"]}</p>
    </div>
    <div class="col-side">
      <div class="panel light vert">{lock(g.lockup_vertical, k, NAVY, "lk-v", g.TAG_SHORT)}</div>
    </div>
  </div>
  <h3>Testes de redução</h3>
  <p class="note">De 32 px para baixo entra a versão de redução: traço mais grosso e menos detalhe. É o que garante leitura a 24 px.</p>
  <div class="tests">{tests}{mono}</div>
  <div class="tests">{tests_dark}</div>
  <h3>Sistema de símbolos</h3>
  <div class="system">
    <figure>{icon(k, NAVY, 72)}<figcaption>Principal · sofá</figcaption></figure>
    <figure>{sec(k, "reforma", NAVY, 72)}<figcaption>Reforma · assento costurado</figcaption></figure>
    <figure>{sec(k, "impermeabilizacao", NAVY, 72)}<figcaption>Impermeabilização · gota</figcaption></figure>
  </div>
  <h3>Aplicações</h3>
  <div class="apps">
    <figure class="app">
      <div class="avatar">{icon(k, LINEN, 64, "full")}</div>
      <figcaption>Perfil Instagram e WhatsApp<br><span>512 × 512, recorte circular da plataforma</span></figcaption>
    </figure>
    <figure class="app">
      <div class="post">
        <div class="photo"><span>Foto própria da peça<br>luz natural lateral</span></div>
        <div class="post-body">
          <p class="p-name">Sofá três lugares</p>
          <p class="p-meta">Pronta entrega · 48 h</p>
          <p class="p-price">Sob consulta</p>
          <div class="p-logo">{lock(g.lockup_horizontal, k, NAVY, "lk-post")}</div>
        </div>
      </div>
      <figcaption>Post de peça<br><span>1080 × 1350, texto de exemplo</span></figcaption>
    </figure>
    <figure class="app">
      <div class="tag">
        <div class="tag-logo">{lock(g.lockup_horizontal, k, NAVY, "lk-tag")}</div>
        <div class="tag-rule"></div>
        <div class="tag-fields"><span>Peça</span><i></i><span>Tecido</span><i></i><span>Pedido nº</span><i></i></div>
        <p class="tag-foot">Garantia de 12 meses: estrutura, tecido e mão de obra.</p>
      </div>
      <figcaption>Etiqueta de peça<br><span>90 × 50 mm, logo horizontal a 30 mm</span></figcaption>
    </figure>
  </div>
</section>'''

rows = ""
for label, marks, note in CRIT:
    cells = "".join(f'<td><span class="mk {m}" title="{MARK[m][1]}">{MARK[m][0]}</span> <span class="mk-t">{MARK[m][1]}</span></td>' for m in marks)
    rows += f"<tr><th scope=row>{label}</th>{cells}<td class='cn'>{note}</td></tr>"

swatches = "".join(f'<div class="sw"><div class="chip" style="background:{h}"></div><p><b>{n}</b><br><code>{h}</code> · {r}</p></div>'
    for n, h, r in [("Marinho Nobre", NAVY, "60%"), ("Off-white Linho", LINEN, "30%"), ("Grafite", GRAF, "8%"), ("Dourado Antigo", GOLD, "até 5%")])

nav = "".join(f'<a href="#{d["key"]}"><span class="nav-ic">{icon(d["key"], NAVY, 40, "full")}</span>{d["nome"]}</a>' for d in DIRS)

html = f'''<title>Nobre Living · Direções de Marca</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=Inter:wght@300;400;600&display=swap">
<style>
/* Layout: prancha de apresentação; faixa marinho de abertura, depois uma seção por direção sobre linho. Tema único, de marca. */
:root {{
  --navy: {NAVY}; --linen: {LINEN}; --graphite: {GRAF}; --gold: {GOLD};
  --paper: #FBFAF7; --muted: #5E6470; --line: rgba(20,38,61,.14); --photo: #E4DED4;
  --display: "Bodoni Moda", Georgia, "Times New Roman", serif;
  --text: "Inter", system-ui, "Segoe UI", sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--linen); color: var(--graphite); font: 400 16px/1.6 var(--text); }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1, h2 {{ font-family: var(--display); font-weight: 400; text-wrap: balance; color: var(--navy); margin: 0; }}
h3 {{ font: 600 13px/1.3 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); margin: 48px 0 12px; }}
.eyebrow {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 0 0 14px; }}
.top {{ background: var(--navy); color: var(--linen); }}
.top .wrap {{ padding-block: 64px 56px; }}
.top h1 {{ color: var(--linen); font-size: clamp(36px, 6vw, 60px); line-height: 1.08; }}
.top .lead {{ max-width: 62ch; font-weight: 300; font-size: 18px; color: rgba(245,242,236,.86); margin: 20px 0 0; }}
.nav {{ display: flex; flex-wrap: wrap; gap: 12px; margin-top: 36px; }}
.nav a {{ display: inline-flex; align-items: center; gap: 10px; padding: 8px 18px 8px 8px; background: var(--linen); color: var(--navy); text-decoration: none; font-weight: 600; font-size: 14px; letter-spacing: .04em; }}
.nav a:hover, .nav a:focus-visible {{ outline: 1px solid var(--gold); outline-offset: 2px; }}
.nav-ic svg {{ display: block; }}
.fixed {{ padding-block: 48px 8px; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}
.fixed p.lbl {{ font: 600 12px/1 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--muted); margin: 0 0 16px; }}
.sws {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }}
.sw .chip {{ aspect-ratio: 1; max-width: 100%; border: 1px solid var(--line); }}
.sw p {{ font-size: 12px; line-height: 1.45; margin: 8px 0 0; }}
.sw code {{ font: 12px var(--text); color: var(--muted); }}
.type-d {{ font: 400 40px/1.1 var(--display); color: var(--navy); margin: 0; }}
.type-t {{ font: 300 16px/1.5 var(--text); margin: 6px 0 0; }}
.type-t b {{ font-weight: 600; }}
.dir {{ padding-block: 72px 24px; border-top: 1px solid var(--line); margin-top: 48px; }}
.dir-h h2 {{ font-size: clamp(40px, 7vw, 64px); line-height: 1; }}
.lema {{ font: 300 20px/1.4 var(--text); color: var(--muted); margin: 10px 0 32px; }}
.hero-pair {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
.panel {{ display: flex; align-items: center; justify-content: center; padding: 48px 32px; min-height: 200px; }}
.panel.light {{ background: var(--paper); border: 1px solid var(--line); }}
.panel.navy {{ background: var(--navy); }}
.lk-h {{ width: 100%; max-width: 400px; height: auto; }}
.cols {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 40px; margin-top: 40px; align-items: start; }}
.col-text {{ min-width: 0; }}
.ideia {{ font: 400 24px/1.4 var(--display); color: var(--navy); margin: 0 0 24px; max-width: 30ch; text-wrap: pretty; }}
.logica {{ margin: 0; display: grid; gap: 14px; }}
.lg {{ display: grid; grid-template-columns: 120px 1fr; gap: 16px; padding-top: 14px; border-top: 1px solid var(--line); }}
.lg dt {{ font: 600 12px/1.6 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); }}
.lg dd {{ margin: 0; max-width: 60ch; }}
.risco {{ margin: 24px 0 0; padding: 16px 18px; background: var(--paper); border-left: 2px solid var(--gold); max-width: 66ch; font-size: 15px; }}
.risco strong {{ color: var(--navy); }}
.vert {{ min-height: 300px; }}
.lk-v {{ width: 100%; max-width: 260px; height: auto; }}
.note {{ margin: 0 0 16px; color: var(--muted); font-size: 14px; max-width: 70ch; }}
.tests {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 12px; }}
.t {{ margin: 0; text-align: center; }}
.tbox {{ width: 88px; height: 88px; display: grid; place-items: center; background: var(--paper); border: 1px solid var(--line); }}
.tbox.dark {{ background: var(--navy); border-color: var(--navy); }}
.t figcaption {{ font-size: 12px; color: var(--muted); margin-top: 6px; font-variant-numeric: tabular-nums; }}
.system {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.system figure {{ margin: 0; flex: 1 1 180px; display: flex; flex-direction: column; align-items: center; gap: 10px; padding: 24px 12px; background: var(--paper); border: 1px solid var(--line); }}
.system figcaption {{ font-size: 13px; color: var(--muted); text-align: center; }}
.apps {{ display: grid; grid-template-columns: 160px minmax(0, 300px) minmax(0, 1fr); gap: 32px; align-items: start; }}
.app {{ margin: 0; min-width: 0; }}
.app figcaption {{ font-size: 13px; font-weight: 600; color: var(--navy); margin-top: 12px; }}
.app figcaption span {{ font-weight: 400; color: var(--muted); }}
.avatar {{ width: 140px; height: 140px; border-radius: 50%; background: var(--navy); display: grid; place-items: center; }}
.post {{ width: 100%; max-width: 300px; aspect-ratio: 4 / 5; background: var(--linen); border: 1px solid var(--line); display: flex; flex-direction: column; box-shadow: 0 10px 30px -18px rgba(20,38,61,.45); }}
.photo {{ flex: 1; margin: 18px 18px 0; background: var(--photo); display: grid; place-items: center; text-align: center; font-size: 11px; color: var(--muted); letter-spacing: .04em; }}
.post-body {{ padding: 14px 18px 16px; position: relative; }}
.p-name {{ font: 400 22px/1.1 var(--display); color: var(--navy); margin: 0; }}
.p-meta {{ font: 600 9px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--graphite); margin: 8px 0 0; }}
.p-price {{ font: 600 16px/1 var(--text); color: var(--navy); margin: 10px 0 0; }}
.p-logo {{ position: absolute; right: 18px; bottom: 14px; width: 92px; }}
.lk-post, .lk-tag {{ display: block; width: 100%; height: auto; }}
.tag {{ width: 100%; max-width: 360px; aspect-ratio: 90 / 50; background: var(--paper); border: 1px solid var(--line); padding: 6% 6.5%; display: flex; flex-direction: column; box-shadow: 0 10px 30px -18px rgba(20,38,61,.45); }}
.tag-logo {{ width: 36%; }}
.tag-rule {{ height: 1px; background: var(--gold); margin: 5% 0 4%; }}
.tag-fields {{ display: grid; grid-template-columns: auto 1fr; column-gap: 10px; row-gap: 6px; align-items: end; font: 600 9px/1 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); }}
.tag-fields i {{ border-bottom: 1px solid var(--line); height: 9px; }}
.tag-foot {{ margin: auto 0 0; font-size: 9px; line-height: 1.3; color: var(--graphite); }}
.compare {{ padding-block: 72px 24px; border-top: 1px solid var(--line); margin-top: 48px; }}
.compare h2, .rec h2 {{ font-size: clamp(32px, 5vw, 44px); }}
.tbl {{ overflow-x: auto; margin-top: 24px; }}
table {{ border-collapse: collapse; width: 100%; min-width: 720px; font-size: 14px; }}
th, td {{ text-align: left; padding: 12px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }}
thead th {{ font: 600 12px/1.2 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); }}
tbody th {{ font-weight: 600; color: var(--navy); width: 24%; }}
.mk {{ color: var(--navy); font-size: 15px; }}
.mk.verificar {{ color: var(--gold); }}
.mk-t {{ color: var(--muted); font-size: 13px; }}
.cn {{ color: var(--muted); font-size: 13px; }}
.rec {{ margin-top: 48px; background: var(--navy); color: var(--linen); }}
.rec .wrap {{ padding-block: 64px; display: grid; grid-template-columns: 1fr 1.3fr; gap: 48px; }}
.rec h2 {{ color: var(--linen); }}
.rec p, .rec li {{ color: rgba(245,242,236,.88); max-width: 62ch; }}
.rec .eyebrow {{ color: var(--gold); }}
.rec ol {{ padding-left: 20px; margin: 0; display: grid; gap: 10px; }}
.rec h4 {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 28px 0 12px; }}
.foot {{ padding-block: 32px 48px; font-size: 13px; color: var(--muted); }}
@media (max-width: 860px) {{
  .fixed, .hero-pair, .cols, .rec .wrap {{ grid-template-columns: 1fr; }}
  .apps {{ grid-template-columns: 1fr 1fr; }}
  .apps .app:last-child {{ grid-column: 1 / -1; }}
}}
@media (max-width: 480px) {{
  .sws {{ grid-template-columns: repeat(2, 1fr); }}
  .apps {{ grid-template-columns: 1fr; }}
  .lg {{ grid-template-columns: 1fr; gap: 4px; }}
  .panel {{ padding: 32px 20px; min-height: 150px; }}
}}
</style>

<header class="top">
  <div class="wrap">
    <p class="eyebrow">Identidade visual · direções para escolha · 04/11/2026</p>
    <h1>Nobre Living<br>três direções de marca</h1>
    <p class="lead">Paleta, tipografia e o sofá em traço fino já estavam aprovados no briefing. O que muda entre as direções é como o sofá é desenhado, o espaço em volta do nome e o tom que isso dá à marca. Cada uma traz a lógica, os testes de redução e três aplicações.</p>
    <nav class="nav" aria-label="Direções">{nav}</nav>
  </div>
</header>

<main>
<div class="wrap">
  <section class="fixed" aria-label="O que é comum às três">
    <div>
      <p class="lbl">Paleta aprovada · comum às três</p>
      <div class="sws">{swatches}</div>
    </div>
    <div>
      <p class="lbl">Tipografia aprovada · comum às três</p>
      <p class="type-d">Bodoni Moda</p>
      <p class="type-t">Display, pesos 400 e 500. A wordmark usa o tamanho ótico 28, que mantém os traços finos visíveis em logo pequeno.</p>
      <p class="type-d" style="font-family: var(--text); font-weight: 300; font-size: 34px; margin-top: 24px;">Inter</p>
      <p class="type-t">Texto, pesos 300, 400 e 600. Preço sempre em Inter: <b>Sob consulta</b>.</p>
    </div>
  </section>
  {"".join(direction(d) for d in DIRS)}
  <section class="compare" aria-labelledby="h-cmp">
    <p class="eyebrow">Critérios do briefing, seção 10</p>
    <h2 id="h-cmp">Comparativo</h2>
    <div class="tbl"><table>
      <thead><tr><th scope="col">Critério</th><th scope="col">Fio</th><th scope="col">Planta</th><th scope="col">Vão</th><th scope="col">Observação</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
  </section>
</div>
<section class="rec" aria-labelledby="h-rec">
  <div class="wrap">
    <div>
      <p class="eyebrow">Recomendação</p>
      <h2 id="h-rec">Planta, com o calor vindo da fotografia</h2>
    </div>
    <div>
      <p>O inimigo da marca é a dúvida depois da compra. Planta é a direção que diz, sem palavra nenhuma, que a peça foi medida antes. É também a que lê melhor a 24 px e a que fica mais à vontade em orçamento, contrato e etiqueta, onde a promessa de preço e prazo é cumprida.</p>
      <p>O risco dela é parecer comum. A resposta está na Didone com entreletra ampla, no fio dourado usado com parcimônia e na fotografia de luz natural, que traz o lado caloroso. Se a preferência for por mais calor no próprio símbolo, Fio é a segunda opção.</p>
      <h4>Para decidir</h4>
      <ol>
        <li>Qual direção segue, ou se quer combinar elementos de duas.</li>
        <li>Se o nome já passou por busca de anterioridade no INPI. Sem isso, o critério 4 fica em aberto.</li>
        <li>Para as próximas aplicações: o @ do Instagram, o WhatsApp e o e-mail que vão no cartão e na assinatura. Não usei nenhum dado de contato inventado.</li>
      </ol>
      <h4>Depois da escolha</h4>
      <p>Ajuste ótico do símbolo, traços convertidos em contorno, as versões A a E em SVG e PNG @1x, @2x e @3x, favicon de 32 e 64 px, os modelos das dez aplicações e o manual em PDF.</p>
    </div>
  </div>
</section>
<div class="wrap foot">
  <p>Wordmark e assinaturas convertidas em curvas a partir de Bodoni Moda e Inter (licença OFL). Textos dos exemplos são ilustrativos. Preço aparece como "Sob consulta", conforme o briefing.</p>
</div>
</main>
'''
open(sys.argv[2] if len(sys.argv) > 2 else "../apresentacao.html", "w").write(html)
print("pagina ok", len(html))
