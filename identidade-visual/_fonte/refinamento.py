"""Página de apresentação da Planta refinada."""
import sys, base64
import gerar as g, simbolo as sb, marca as mk

NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
OLD = base64.b64encode(open(sys.argv[3], "rb").read()).decode()

def inline(W, H, b, cls):
    return f'<svg class="{cls}" viewBox="0 0 {W:.2f} {H:.2f}" role="img" aria-label="Nobre Living">{b}</svg>'

V = lambda c, cls, tag=None: inline(*mk.vertical(c, tag), cls)
H = lambda c, cls, tag=None: inline(*mk.horizontal(c, tag), cls)
I = lambda c, px, var="full", **kw: sb.square(c, px, var, **kw)

# grade de construção
grid = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="96"/>' for x in range(0, 97, 4))
grid += "".join(f'<line x1="0" y1="{y}" x2="96" y2="{y}"/>' for y in range(0, 97, 4))
guides = "".join(f'<line x1="0" y1="{y-2.5}" x2="118" y2="{y-2.5}"/>' for y in (sb.Y_BACK, sb.Y_ARM, sb.Y_SEAT, sb.Y_BASE, sb.Y_FOOT))
labels = "".join(f'<text x="119" y="{y-3.3}" text-anchor="end">{t}</text>' for y, t in
                 [(sb.Y_BACK, "encosto"), (sb.Y_ARM, "braço"), (sb.Y_SEAT, "assento"), (sb.Y_BASE, "base"), (sb.Y_FOOT, "pé")])
construcao = (f'<svg class="constr" viewBox="0 0 120 96" role="img" aria-label="Grade de construção do símbolo">'
              f'<g stroke="var(--grid)" stroke-width=".15">{grid}</g>'
              f'<g stroke="var(--gold)" stroke-width=".3" stroke-dasharray="1 1">{guides}</g>'
              f'<g class="lbl">{labels}</g>{sb.group(NAVY, sb.STROKES["medio"], "full", 0, -2.5)}</svg>')

tests = "".join(f'<figure class="t"><div class="tbox">{I(NAVY, px, "reducao" if px <= 40 else "full", sw=None if px <= 40 else sb.STROKES["medio"])}</div><figcaption>{px} px</figcaption></figure>' for px in (96, 48, 32, 24, 16))
tests_d = "".join(f'<figure class="t"><div class="tbox dark">{I(LINEN, px, "reducao" if px <= 40 else "full", sw=None if px <= 40 else sb.STROKES["medio"])}</div><figcaption>{px} px</figcaption></figure>' for px in (96, 48, 32, 24, 16))

versoes = f'''
<figure class="v v-a"><div class="panel light">{V(NAVY, "lk-v")}</div><figcaption><b>A · Vertical</b> Avatar, capa, etiqueta</figcaption></figure>
<figure class="v v-c"><div class="panel navy">{I(LINEN, 120)}</div><figcaption><b>C · Ícone</b> Perfil, favicon, marca d'água</figcaption></figure>
<figure class="v v-d"><div class="panel white">{V(GRAF, "lk-v")}</div><figcaption><b>D · Uma cor</b> Gravação, bordado, carimbo</figcaption></figure>
<figure class="v v-b"><div class="panel light">{H(NAVY, "lk-h")}</div><figcaption><b>B · Horizontal</b> Cabeçalho, orçamento, contrato, e-mail</figcaption></figure>
<figure class="v v-e"><div class="panel navy">{H(LINEN, "lk-h", g.TAG_FULL)}</div><figcaption><b>E · Assinatura completa</b> Peça institucional</figcaption></figure>
'''

html = f'''<title>Nobre Living · Planta Refinada</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400;6..96,500&family=Inter:wght@300;400;600&display=swap">
<style>
/* Layout: abertura marinho com antes/depois; seções sobre linho; aplicações em escala real relativa. Tema único, de marca. */
:root {{
  --navy: {NAVY}; --linen: {LINEN}; --graphite: {GRAF}; --gold: {GOLD};
  --paper: #FBFAF7; --muted: #5E6470; --line: rgba(20,38,61,.14); --grid: rgba(20,38,61,.16); --photo: #E4DED4;
  --display: "Bodoni Moda", Georgia, "Times New Roman", serif;
  --text: "Inter", system-ui, "Segoe UI", sans-serif;
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ background: var(--linen); color: var(--graphite); font: 400 16px/1.6 var(--text); }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
h1, h2 {{ font-family: var(--display); font-weight: 400; color: var(--navy); margin: 0; text-wrap: balance; }}
h2 {{ font-size: clamp(32px, 5vw, 46px); line-height: 1.08; }}
h3 {{ font: 600 13px/1.3 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); margin: 40px 0 14px; }}
.eyebrow {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 0 0 14px; }}
.lead {{ max-width: 62ch; font-weight: 300; font-size: 18px; }}
.top {{ background: var(--navy); color: var(--linen); }}
.top .wrap {{ padding-block: 60px 64px; }}
.top h1 {{ color: var(--linen); font-size: clamp(36px, 6vw, 60px); line-height: 1.06; }}
.top .lead {{ color: rgba(245,242,236,.86); margin: 18px 0 40px; }}
.ba {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
.ba figure {{ margin: 0; }}
.ba .frame {{ aspect-ratio: 1; max-width: 100%; display: grid; place-items: center; }}
.ba .old {{ background: #000; }}
.ba .old img {{ width: 100%; height: 100%; object-fit: contain; display: block; }}
.ba .new {{ background: var(--linen); padding: 14%; }}
.ba figcaption {{ font-size: 13px; margin-top: 10px; color: rgba(245,242,236,.75); }}
.ba figcaption b {{ color: var(--linen); font-weight: 600; }}
.lk-v {{ width: 100%; height: auto; display: block; }}
.lk-h {{ width: 100%; height: auto; display: block; }}
section.s {{ padding-block: 64px 8px; }}
section.s + section.s {{ border-top: 1px solid var(--line); margin-top: 56px; }}
.two {{ display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start; margin-top: 28px; }}
.two > * {{ min-width: 0; }}
.kept, .changed {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 0; }}
.kept li, .changed li {{ padding: 12px 0; border-top: 1px solid var(--line); }}
.kept li b, .changed li b {{ color: var(--navy); font-weight: 600; }}
.constr {{ width: 100%; max-width: 520px; height: auto; background: var(--paper); border: 1px solid var(--line); display: block; }}
.constr .lbl text {{ font: 2.6px var(--text); fill: var(--muted); letter-spacing: .05em; }}
.note {{ color: var(--muted); font-size: 14px; max-width: 68ch; margin: 0 0 16px; }}
.versoes {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; margin-top: 28px; }}
.v {{ margin: 0; min-width: 0; }}
.v-a, .v-d {{ grid-column: span 2; }}
.v-c {{ grid-column: span 2; }}
.v-b, .v-e {{ grid-column: span 3; }}
.panel {{ display: grid; place-items: center; padding: 40px 28px; height: 240px; }}
.panel.light {{ background: var(--paper); border: 1px solid var(--line); }}
.panel.white {{ background: #fff; border: 1px solid var(--line); }}
.panel.navy {{ background: var(--navy); }}
.v-a .lk-v, .v-d .lk-v {{ max-width: 230px; }}
.v-b .lk-h, .v-e .lk-h {{ max-width: 400px; }}
.v figcaption {{ font-size: 13px; color: var(--muted); margin-top: 10px; }}
.v figcaption b {{ display: block; color: var(--navy); font-weight: 600; }}
.tests {{ display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 12px; }}
.t {{ margin: 0; text-align: center; }}
.tbox {{ width: 112px; height: 112px; display: grid; place-items: center; background: var(--paper); border: 1px solid var(--line); }}
.tbox.dark {{ background: var(--navy); border-color: var(--navy); }}
.t figcaption {{ font-size: 12px; color: var(--muted); margin-top: 6px; font-variant-numeric: tabular-nums; }}
.alt {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }}
.alt svg, .sys svg {{ max-width: 100%; height: auto; }}
.alt figure, .sys figure {{ min-width: 0; }}
.alt figure, .sys figure {{ margin: 0; background: var(--paper); border: 1px solid var(--line); padding: 20px 16px 16px; display: flex; flex-direction: column; align-items: center; gap: 8px; }}
.alt figcaption, .sys figcaption {{ font-size: 13px; color: var(--muted); text-align: center; max-width: 34ch; }}
.alt figcaption b, .sys figcaption b {{ display: block; color: var(--navy); font-weight: 600; }}
.sys {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
.apps {{ display: grid; grid-template-columns: repeat(12, 1fr); gap: 28px 24px; margin-top: 28px; align-items: start; }}
.app {{ margin: 0; min-width: 0; }}
.app figcaption {{ font-size: 13px; font-weight: 600; color: var(--navy); margin-top: 12px; }}
.app figcaption span {{ display: block; font-weight: 400; color: var(--muted); }}
.a-avatar {{ grid-column: span 3; }} .a-post {{ grid-column: span 4; }} .a-tag {{ grid-column: span 5; }}
.a-card {{ grid-column: span 5; }} .a-mail {{ grid-column: span 7; }}
.avatar {{ width: 100%; max-width: 180px; aspect-ratio: 1; border-radius: 50%; background: var(--navy); display: grid; place-items: center; }}
.avatar svg {{ width: 68%; height: auto; }}
.shadow {{ box-shadow: 0 12px 32px -20px rgba(20,38,61,.5); }}
.post {{ width: 100%; max-width: 320px; aspect-ratio: 4 / 5; background: var(--linen); border: 1px solid var(--line); display: flex; flex-direction: column; }}
.photo {{ flex: 1; margin: 6.7% 6.7% 0; background: var(--photo); display: grid; place-items: center; text-align: center; font-size: 11px; color: var(--muted); }}
.post-body {{ padding: 5% 6.7% 6%; display: flex; justify-content: space-between; align-items: end; gap: 12px; }}
.p-name {{ font: 400 22px/1.1 var(--display); color: var(--navy); margin: 0; }}
.p-meta {{ font: 600 9px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; margin: 8px 0 0; }}
.p-price {{ font: 600 16px/1 var(--text); color: var(--navy); margin: 10px 0 0; }}
.p-logo {{ width: 34%; flex: none; }}
.card90 {{ width: 100%; max-width: 400px; aspect-ratio: 90 / 50; padding: 6% 6.5%; display: flex; flex-direction: column; }}
.tag {{ background: var(--paper); border: 1px solid var(--line); }}
.tag-logo {{ width: 40%; }}
.rule {{ height: 1px; background: var(--gold); margin: 5% 0 4%; }}
.fields {{ display: grid; grid-template-columns: auto 1fr; column-gap: 10px; row-gap: 7px; align-items: end; font: 600 8.5px/1 var(--text); letter-spacing: .12em; text-transform: uppercase; color: var(--navy); }}
.fields i {{ border-bottom: 1px solid var(--line); height: 9px; }}
.foot9 {{ margin: auto 0 0; font-size: 9px; line-height: 1.35; }}
.card {{ background: var(--navy); color: var(--linen); justify-content: space-between; }}
.card .c-h {{ font: 400 20px/1.15 var(--display); margin: 0; color: var(--linen); }}
.card .c-t {{ font: 300 10.5px/1.5 var(--text); margin: 0; color: rgba(245,242,236,.9); }}
.card .c-f {{ display: flex; justify-content: space-between; align-items: end; gap: 12px; font: 600 9px/1.4 var(--text); letter-spacing: .1em; text-transform: uppercase; }}
.card .c-f svg {{ width: 36px; height: auto; flex: none; }}
.mail {{ background: #fff; border: 1px solid var(--line); padding: 22px 24px; max-width: 560px; font: 400 14px/1.5 var(--text); }}
.mail .m-txt {{ color: var(--graphite); margin: 0 0 18px; }}
.sig {{ display: flex; gap: 18px; align-items: center; padding-top: 16px; border-top: 1px solid var(--gold); }}
.sig .sig-ic {{ width: 64px; flex: none; }}
.sig p {{ margin: 0; font-size: 13px; line-height: 1.55; }}
.sig .sig-n {{ font-weight: 600; color: var(--navy); }}
.sig .sig-b {{ font: 500 10px/1.6 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--navy); }}
.sig .sig-c {{ color: var(--muted); font-variant-numeric: tabular-nums; }}
.decide {{ margin-top: 64px; background: var(--navy); color: var(--linen); }}
.decide .wrap {{ padding-block: 60px; display: grid; grid-template-columns: 1fr 1.3fr; gap: 48px; }}
.decide h2 {{ color: var(--linen); }}
.decide ol {{ margin: 0; padding-left: 20px; display: grid; gap: 12px; color: rgba(245,242,236,.9); }}
.decide ol b {{ color: var(--linen); }}
.decide p {{ color: rgba(245,242,236,.88); max-width: 62ch; }}
.decide h4 {{ font: 600 12px/1 var(--text); letter-spacing: .14em; text-transform: uppercase; color: var(--gold); margin: 28px 0 12px; }}
.foot {{ padding-block: 28px 48px; font-size: 13px; color: var(--muted); }}
@media (max-width: 900px) {{
  .two, .decide .wrap {{ grid-template-columns: 1fr; }}
  .versoes {{ grid-template-columns: 1fr 1fr; }}
  .v-a, .v-c, .v-d {{ grid-column: span 1; }} .v-b, .v-e {{ grid-column: 1 / -1; }}
  .v-c {{ grid-column: 1 / -1; }}
  .apps {{ grid-template-columns: 1fr 1fr; }}
  .a-avatar, .a-post {{ grid-column: span 1; }} .a-tag, .a-card, .a-mail {{ grid-column: 1 / -1; }}
}}
@media (max-width: 520px) {{
  .ba, .alt, .sys, .versoes, .apps {{ grid-template-columns: 1fr; }}
  .v-a, .v-b, .v-c, .v-d, .v-e, .a-avatar, .a-post {{ grid-column: 1 / -1; }}
  .panel {{ height: 200px; }}
  .tbox {{ width: 84px; height: 84px; }}
}}
</style>

<header class="top">
  <div class="wrap">
    <p class="eyebrow">Identidade visual · rodada de refinamento · 04/11/2026</p>
    <h1>Planta refinada</h1>
    <p class="lead">A base é a direção Planta, com a essência do logo de 2025: o encosto em três módulos, os braços arredondados à frente do encosto e os pés palito inclinados. O desenho foi limpo para ganhar presença e funcionar do perfil do Instagram à etiqueta de 90 mm.</p>
    <div class="ba">
      <figure><div class="frame old"><img src="data:image/jpeg;base64,{OLD}" alt="Logo de 2025: sofá de três lugares em linha branca sobre fundo preto, com o nome em serifa"></div><figcaption><b>2025</b> Raster, fundo preto</figcaption></figure>
      <figure><div class="frame new">{V(NAVY, "lk-v")}</div><figcaption><b>2026</b> Vetor, texto em curvas, marinho sobre linho</figcaption></figure>
    </div>
  </div>
</header>

<main>
<div class="wrap">
  <section class="s" aria-labelledby="h-o">
    <p class="eyebrow">O que mudou</p>
    <h2 id="h-o">Mesma alma, desenho mais preciso</h2>
    <div class="two">
      <div>
        <h3>Herdado de 2025</h3>
        <ul class="kept">
          <li><b>Sofá de três lugares em linha.</b> É o que a cliente já reconhece.</li>
          <li><b>Encosto em três módulos.</b> Agora como divisões soltas que param antes do assento, com respiro.</li>
          <li><b>Braços arredondados à frente do encosto.</b> Raio único em todos os cantos.</li>
          <li><b>Pés palito inclinados.</b> Dão o traço contemporâneo.</li>
          <li><b>Nome em serifa, caixa alta.</b></li>
        </ul>
      </div>
      <div>
        <h3>Refinado em 2026</h3>
        <ul class="changed">
          <li><b>Menos linhas.</b> Saíram as almofadas de assento e a faixa de base. O sofá lê como sofá a 24 px.</li>
          <li><b>Proporção 2:1 numa grade de 4 unidades.</b> Mais largo e baixo, como o original.</li>
          <li><b>Espessura do traço por tamanho.</b> Fino no logo grande, médio no ícone e grosso na redução.</li>
          <li><b>Bodoni Moda com entreletra ampla.</b> No horizontal, a linha de base do nome coincide com a base do sofá.</li>
          <li><b>Marinho e linho no lugar do preto.</b> O preto fica só para peça antiga, como pede o briefing.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="s" aria-labelledby="h-c">
    <p class="eyebrow">Construção</p>
    <h2 id="h-c">Cinco alturas, um raio, um traço</h2>
    <div class="two">
      <div>{construcao}</div>
      <div>
        <p class="note">Encosto, braço, assento, base e pé ficam em alturas fixas da grade de 96 unidades. O sofá ocupa 84 × 41, com braços de 11 unidades e três módulos iguais de 20,7.</p>
        <h3>Duas leituras do mesmo sofá</h3>
        <div class="alt">
          <figure>{I(NAVY, 150)}<figcaption><b>Mínima · recomendada</b> Lê melhor pequena e é a mais refinada.</figcaption></figure>
          <figure>{I(NAVY, 150, "estofada")}<figcaption><b>Estofada</b> Almofadas abauladas, mais próxima de 2025. Perde nitidez abaixo de 48 px.</figcaption></figure>
        </div>
      </div>
    </div>
  </section>

  <section class="s" aria-labelledby="h-v">
    <p class="eyebrow">Versões obrigatórias</p>
    <h2 id="h-v">De A a E</h2>
    <div class="versoes">{versoes}</div>
    <p class="note" style="margin-top:20px">Área de proteção: margem igual à altura do ícone em todos os lados. Mínimos: ícone 24 px ou 8 mm, horizontal 120 px ou 30 mm.</p>
  </section>

  <section class="s" aria-labelledby="h-t">
    <p class="eyebrow">Critérios 1, 2 e 3 do briefing</p>
    <h2 id="h-t">Testes de redução</h2>
    <p class="note" style="margin-top:16px">Até 40 px entra a versão de redução: sem os módulos, com raio maior e traço grosso. Acima disso, o símbolo completo.</p>
    <div class="tests">{tests}</div>
    <div class="tests">{tests_d}</div>
  </section>

  <section class="s" aria-labelledby="h-y">
    <p class="eyebrow">Sistema</p>
    <h2 id="h-y">Ícones de serviço</h2>
    <p class="note" style="margin-top:16px">Mesmo traço e mesma grade do símbolo. Ficam sempre subordinados ao logo, nunca no lugar dele.</p>
    <div class="sys">
      <figure>{I(NAVY, 110)}<figcaption><b>Móveis</b> Pronta entrega e sob medida</figcaption></figure>
      <figure>{I(NAVY, 110, dashed_seat=True)}<figcaption><b>Reforma</b> Assento em costura, o que já é seu</figcaption></figure>
      <figure>{I(NAVY, 110, drop=True)}<figcaption><b>Impermeabilização</b> Gota sobre o encosto</figcaption></figure>
    </div>
  </section>

  <section class="s" aria-labelledby="h-a">
    <p class="eyebrow">Aplicações com os dados reais</p>
    <h2 id="h-a">Como a marca aparece</h2>
    <div class="apps">
      <figure class="app a-avatar"><div class="avatar">{I(LINEN, None)}</div><figcaption>Perfil @nobreliving<span>Instagram e WhatsApp, 512 × 512</span></figcaption></figure>
      <figure class="app a-post"><div class="post shadow">
        <div class="photo"><span>Foto própria da peça<br>luz natural lateral</span></div>
        <div class="post-body"><div><p class="p-name">Sofá três lugares</p><p class="p-meta">Pronta entrega · 48 h</p><p class="p-price">Sob consulta</p></div><div class="p-logo">{V(NAVY, "lk-v")}</div></div>
      </div><figcaption>Post de peça<span>1080 × 1350, texto de exemplo</span></figcaption></figure>
      <figure class="app a-tag"><div class="card90 tag shadow">
        <div class="tag-logo">{H(NAVY, "lk-h")}</div><div class="rule"></div>
        <div class="fields"><span>Peça</span><i></i><span>Tecido</span><i></i><span>Pedido nº</span><i></i></div>
        <p class="foot9">Garantia de 12 meses: estrutura, tecido e mão de obra.</p>
      </div><figcaption>Etiqueta de peça<span>90 × 50 mm</span></figcaption></figure>
      <figure class="app a-card"><div class="card90 card shadow">
        <p class="c-h">Sua peça está em casa.</p>
        <p class="c-t">Garantia de 12 meses para estrutura, tecido e mão de obra. Qualquer ajuste, fale com a gente.</p>
        <div class="c-f"><span>(61) 99604-4750<br>@nobreliving</span>{I(LINEN, None)}</div>
      </div><figcaption>Cartão de pós-entrega<span>90 × 50 mm, verso</span></figcaption></figure>
      <figure class="app a-mail"><div class="mail shadow">
        <p class="m-txt">Segue o orçamento com preço, prazo e condições. Qualquer dúvida, é só responder.</p>
        <div class="sig">
          <div class="sig-ic">{I(NAVY, None)}</div>
          <div><p class="sig-n">Seu nome</p><p class="sig-b">Nobre Living · Móveis e estofados · Brasília</p>
          <p class="sig-c">(61) 99604-4750 · nobrelivingg@gmail.com · @nobreliving</p></div>
        </div>
      </div><figcaption>Assinatura de e-mail<span>O nome de quem assina fica a definir</span></figcaption></figure>
    </div>
  </section>
</div>

<section class="decide" aria-labelledby="h-d">
  <div class="wrap">
    <div><p class="eyebrow">Para fechar</p><h2 id="h-d">Três confirmações antes do kit final</h2></div>
    <div>
      <ol>
        <li><b>Leitura mínima ou estofada?</b> Recomendo a mínima.</li>
        <li><b>Cantos arredondados.</b> O briefing pedia cantos vivos e nenhuma almofada. Para manter a essência de 2025, arredondei os cantos. Se aprovar, atualizo o briefing.</li>
        <li><b>Nome na assinatura de e-mail.</b> Quem assina: o nome do dono ou só "Nobre Living"?</li>
      </ol>
      <h4>Depois da aprovação</h4>
      <p>PNG transparente @1x, @2x e @3x de todas as versões, favicon de 32 e 64 px, modelos das dez aplicações, orçamento e contrato em A4, e o manual da marca em PDF.</p>
    </div>
  </div>
</section>
<div class="wrap foot"><p>Logos em vetor com texto convertido em curvas (Bodoni Moda e Inter, licença OFL). Preço aparece como "Sob consulta", conforme o briefing.</p></div>
</main>
'''
open(sys.argv[2], "w").write(html)
print("ok", len(html))
