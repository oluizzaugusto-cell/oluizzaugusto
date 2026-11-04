"""Manual da marca Nobre Living (HTML → PDF A4 paisagem).
Uso: python3 kit_manual.py <pasta-fontes> <pasta-kit>"""
import sys, os, re
F, KIT = sys.argv[1], sys.argv[2]
sys.argv = [sys.argv[0], F]
import final as fs
from kit_templates import hl_icon

SVG = os.path.join(KIT, "svg"); PREV = os.path.join(KIT, "modelos", "previa")
NAVY, LINEN, GRAF, GOLD = "#14263D", "#F5F2EC", "#252525", "#B49A68"

def L(name, cls="", style=""):
    s = open(os.path.join(SVG, f"nobre-living-{name}.svg")).read()
    s = re.sub(r"<title>.*?</title>", "", s)
    return re.sub(r'<svg([^>]*?) width="[^"]*" height="[^"]*"', rf'<svg\1 class="{cls}" style="{style}"', s, count=1) \
        if ' width="' in s.split(">")[0] else s.replace("<svg ", f'<svg class="{cls}" style="{style}" ', 1)

def prev(name): return f'<img src="file://{PREV}/{name}.png" alt="">'

def page(content, cls="", num=None, sec=""):
    foot = f'<footer><span>Nobre Living · Manual da marca</span><span>{sec}</span><span>{num:02d}</span></footer>' if num else ""
    return f'<section class="pg {cls}">{content}{foot}</section>'

def head(eyebrow, title, lead=""):
    return f'<p class="eb">{eyebrow}</p><h2>{title}</h2>' + (f'<p class="lead">{lead}</p>' if lead else "")

pages = []
n = 0
def add(content, cls="", sec=""):
    global n; n += 1
    pages.append(page(content, cls, n if n > 1 else None, sec))

# 1 · Capa
add(f'''<div class="cover">{L("a-vertical-offwhite", "cv-logo")}
<div class="cv-meta"><p class="eb">Manual da marca</p><p>Versão 1.0 · novembro de 2026</p><p>Identidade visual do relançamento</p></div></div>''', "navy")

# 2 · Essência
add(head("01 · Essência", "Curadoria de móveis e estofados em Brasília")
 + '''<div class="cols3">
 <div><h3>Promessa</h3><p class="quote">A escolha certa, do móvel novo ao que já é seu.</p></div>
 <div><h3>Propósito</h3><p>Deixar a casa pronta para receber, do móvel que já existe ao que ainda vai ser feito.</p>
 <h3>Missão</h3><p>Escolher com critério o móvel certo para cada casa, e dizer preço, prazo e condição antes, não depois.</p></div>
 <div><h3>Personalidade</h3><p>Elegante, segura, consultiva, calma, calorosa, precisa e discreta. Nunca esnobe, insistente ou burocrática.</p>
 <h3>Tom de voz</h3><p>Frase curta. Número no lugar do adjetivo: “30 dias”, não “rapidinho”. Trata por “você”. Zero urgência artificial.</p></div>
 </div>
 <div class="valores"><span>Palavra cumprida</span><span>Transparência de preço e condição</span><span>Critério, não catálogo</span><span>Respeito pelo tempo e pela casa</span><span>Consertar o erro</span></div>''', sec="Essência")

# 3 · Símbolo
add(head("02 · Símbolo", "Portal", "Um arco de porta enquadra a sala pronta. É o propósito da marca desenhado: a casa pronta para receber.")
 + f'''<div class="sym">
 <div class="sym-big">{L("c-icone-marinho", "s-big")}</div>
 <ul class="parts">
  <li><b>Arco</b> A porta da casa. Dá ao símbolo uma silhueta própria, sem círculo nem escudo.</li>
  <li><b>Pendente</b> A luz que desce do alto do arco: a sala acesa, à espera de quem chega.</li>
  <li><b>Sofá</b> Herdado do logo de 2025: três módulos, braços arredondados e pés palito inclinados.</li>
  <li><b>Vaso com galhos secos</b> O objeto de afeto que torna a sala vivida. Galhos, nunca folhas.</li>
  <li><b>Piso</b> A linha que atravessa o vão e dá chão à cena.</li>
 </ul></div>''', sec="Símbolo")

# 4 · Níveis de detalhe
lv = "".join(f'<figure><div class="lvbox">{L(f"c-icone{suf}-marinho", "lv")}</div><figcaption><b>{t}</b>{d}</figcaption></figure>'
             for suf, t, d in [("", "Completo", "64 px ou mais · 20 mm ou mais. Todos os detalhes."),
                               ("-reducao", "Redução", "De 24 a 63 px. Sofá sem módulos, vaso com uma haste, traço grosso."),
                               ("-micro", "Micro", "Até 20 px (favicon). Só as silhuetas.")])
add(head("03 · Símbolo", "Três níveis de detalhe", "O símbolo muda de detalhe conforme o tamanho, para continuar legível do perfil ao favicon. Use sempre o arquivo do nível certo; nunca reduza o completo.")
 + f'<div class="levels">{lv}</div>', sec="Símbolo")

# 5 · Versões
add(head("04 · Logo", "Versões A a E")
 + f'''<div class="vers">
 <figure class="v1"><div class="vb light">{L("a-vertical-marinho", "lg-v")}</div><figcaption><b>A · Vertical</b> Avatar, capa, etiqueta</figcaption></figure>
 <figure class="v3"><div class="vb navy">{L("c-icone-offwhite", "lg-c")}</div><figcaption><b>C · Ícone</b> Perfil, favicon, marca d’água</figcaption></figure>
 <figure class="v4"><div class="vb white">{L("d-monocromatica-horizontal-grafite", "lg-h")}</div><figcaption><b>D · Monocromática</b> Gravação, bordado, carimbo</figcaption></figure>
 <figure class="v2"><div class="vb light">{L("b-horizontal-marinho", "lg-h")}</div><figcaption><b>B · Horizontal</b> Cabeçalho, orçamento, contrato, e-mail</figcaption></figure>
 <figure class="v5"><div class="vb navy">{L("e-assinatura-offwhite", "lg-h")}</div><figcaption><b>E · Assinatura completa</b> Peça institucional. A linha curta “Móveis · Brasília” não substitui a completa.</figcaption></figure>
 </div>''', sec="Logo")

# 6 · Proteção e mínimos
add(head("05 · Logo", "Área de proteção e tamanhos mínimos", "Margem livre igual à altura do arco em todos os lados. Nada entra nessa área: texto, foto recortada, borda de página.")
 + f'''<div class="prot">
 <div class="pbox"><div class="pzone">{L("b-horizontal-marinho", "lg-p")}</div><span class="pl">x = altura do arco</span></div>
 <table class="mins"><thead><tr><th>Versão</th><th>Tela</th><th>Impressão</th></tr></thead><tbody>
 <tr><td>C · Ícone</td><td>24 px</td><td>8 mm</td></tr>
 <tr><td>B · Horizontal</td><td>120 px</td><td>30 mm</td></tr>
 <tr><td>A · Vertical</td><td>96 px de largura</td><td>24 mm</td></tr>
 <tr><td>E · Assinatura</td><td>200 px</td><td>50 mm</td></tr>
 </tbody></table></div>''', sec="Logo")

# 7 · Cores
sw = "".join(f'<div class="sw"><div class="chip" style="background:{h};{"border:1px solid #ddd" if h==LINEN else ""}"></div><p class="sn">{nm}</p><p>HEX {h}<br>RGB {r}<br>{u}</p></div>'
   for nm, h, r, u in [("Marinho Nobre", NAVY, "20 38 61", "Primária · 60%"), ("Off-white Linho", LINEN, "245 242 236", "Clara · 30%"),
                       ("Grafite", GRAF, "37 37 37", "Texto · 8%"), ("Dourado Antigo", GOLD, "180 154 104", "Acento · até 5%")])
add(head("06 · Cores", "Paleta")
 + f'''<div class="sws">{sw}</div>
 <div class="cols2 small">
 <div><h3>Contraste</h3><p>Marinho sobre off-white: 13,4:1. Off-white sobre marinho: o mesmo. Ambos AAA. O dourado é só acento: fio, detalhe, nunca texto corrido.</p></div>
 <div><h3>Proibido</h3><p>Preto puro como fundo de marca. Cores saturadas. Degradê marinho–dourado. Mais de 4 cores na mesma peça.</p>
 <h3>Impressão</h3><p>O CMYK não está definido: a gráfica faz a conversão com o perfil da máquina, a partir do HEX, e aprova prova de cor antes da tiragem.</p></div></div>''', sec="Cores")

# 8 · Tipografia
add(head("07 · Tipografia", "Prata e Inter", "Duas fontes gratuitas do Google Fonts. Prata para o nome e os títulos; Inter para todo o resto.")
 + '''<div class="type">
 <div class="tp"><p class="tp-n prata">Prata</p><p class="abc prata">Aa Bb Cc Ãã Çç 0123</p><p>Nome da marca (em curvas no logo) e títulos. Peso único 400. Escolhida porque mantém o N firme em tamanho pequeno.</p></div>
 <div class="tp"><p class="tp-n inter">Inter</p><p class="abc inter">Aa Bb Cc Ãã Çç 0123</p><p>Texto, preço, legenda e etiqueta. Pesos 300, 400 e 600.</p></div>
 <table class="hier"><tbody>
 <tr><td class="prata" style="font-size:22pt">Título 1</td><td>Prata 48–64 px</td></tr>
 <tr><td class="prata" style="font-size:16pt">Título 2</td><td>Prata 32–40 px</td></tr>
 <tr><td class="inter" style="font-weight:600;font-size:12pt">Título 3</td><td>Inter 600 · 20–24 px</td></tr>
 <tr><td class="inter" style="font-size:10pt">Corpo do texto</td><td>Inter 400 · 16–18 px</td></tr>
 <tr><td class="inter" style="font-weight:600;font-size:13pt">Sob consulta</td><td>Preço: Inter 600 · 24–32 px</td></tr>
 <tr><td class="inter" style="font-weight:500;font-size:7pt;letter-spacing:.12em">ETIQUETA</td><td>Inter 500 · 10–12 px · +0,12 em · caixa alta</td></tr>
 </tbody></table></div>
 <p class="rules">Máximo 2 pesos por peça · nunca esticar, condensar ou contornar · caixa alta só em etiqueta curta · nunca justificar texto digital · preço sempre em Inter</p>''', sec="Tipografia")

# 9 · Fundos
bgs = [("Marinho", NAVY, "c-icone-offwhite", ""), ("Off-white", "#F5F2EC", "c-icone-marinho", ""),
       ("Foto escura + véu 30%", "linear-gradient(rgba(20,38,61,.30),rgba(20,38,61,.30)),#4a4440", "c-icone-offwhite", "Off-white"),
       ("Foto clara + véu 40%", "linear-gradient(rgba(245,242,236,.40),rgba(245,242,236,.40)),#cfc6b8", "c-icone-marinho", "Marinho")]
fb = "".join(f'<figure><div class="bgb" style="background:{b}">{L(lg, "lg-bg")}</div><figcaption>{t}</figcaption></figure>' for t, b, lg, _ in bgs)
add(head("08 · Aplicação", "Fundos permitidos", "Marinho pede off-white; off-white pede marinho. Sobre foto, use véu. Preto só em peça antiga ainda em circulação.")
 + f'<div class="bgs">{fb}</div>', sec="Aplicação")

# 10 · Usos incorretos
wrong = [("Esticar ou achatar", 'transform:scaleX(1.5)'), ("Rotacionar ou inclinar", 'transform:rotate(-12deg)'),
         ("Sombra, brilho ou relevo", 'filter:drop-shadow(3px 4px 3px rgba(0,0,0,.5))'), ("Trocar as cores", 'filter:hue-rotate(140deg) saturate(4)'),
         ("Dentro de círculo ou escudo", 'border:3px solid #14263D;border-radius:50%;padding:12px'), ("Baixo contraste sem véu", 'opacity:.25')]
wr = "".join(f'<figure><div class="wb"><div style="{st}">{L("c-icone-marinho", "lg-w")}</div><span class="x">×</span></div><figcaption>{t}</figcaption></figure>' for t, st in wrong)
add(head("09 · Aplicação", "Usos incorretos", "Também não: redesenhar o sofá com outro traço, usar a wordmark sozinha em corpo pequeno, aplicar degradê.")
 + f'<div class="wrong">{wr}</div>', sec="Aplicação")

# 11 · Ícones de apoio
ic = "".join(f'<figure><svg viewBox="0 0 96 96" class="hl">{hl_icon(k, NAVY, 2.6)}</svg><figcaption>{t}</figcaption></figure>'
             for k, t in [("colecao", "Coleção"), ("entrega", "Entrega"), ("sobmedida", "Sob medida"), ("cuidados", "Cuidados")])
add(head("10 · Sistema", "Ícones de apoio", "Mesmo traço do símbolo. Usados nas capas de destaque e em listas de serviço. Ficam sempre subordinados ao logo, nunca no lugar dele.")
 + f'<div class="icons">{ic}</div>', sec="Sistema")

# 12-13 · Aplicações
add(head("11 · Aplicações", "Digital")
 + f'''<div class="apps-d">
 <figure>{prev("01-perfil-512")}<figcaption>Perfil · 512 × 512</figcaption></figure>
 <figure>{prev("02-destaque-colecao-1080x1920")}<figcaption>Destaque · 1080 × 1920</figcaption></figure>
 <figure>{prev("03-post-peca-1080x1350")}<figcaption>Post de peça · 1080 × 1350</figcaption></figure>
 <figure>{prev("04-story-disponibilidade-1080x1920")}<figcaption>Story · 1080 × 1920</figcaption></figure>
 </div><p class="note">Feed e story: margem 72 px, área útil 936 px, 12 colunas de 58 px, calha 20 px, base 8 px. No story, zona segura de 250 px no topo e 340 px na base.</p>''', sec="Aplicações")
add(head("12 · Aplicações", "Impressos")
 + f'''<div class="apps-p">
 <figure class="a4">{prev("05-orcamento-a4")}<figcaption>Orçamento · A4</figcaption></figure>
 <figure class="a4">{prev("06-ficha-pedido-a4")}<figcaption>Ficha do pedido · A4</figcaption></figure>
 <div class="small-p">
  <figure>{prev("07-etiqueta-90x50mm")}<figcaption>Etiqueta · 90 × 50 mm</figcaption></figure>
  <figure>{prev("08-cartao-pos-entrega-frente-90x50mm")}<figcaption>Cartão pós-entrega · frente</figcaption></figure>
  <figure>{prev("08-cartao-pos-entrega-verso-90x50mm")}<figcaption>Cartão pós-entrega · verso</figcaption></figure>
 </div></div><p class="note">A4: margem 20 mm, logo horizontal com 52 mm, fio dourado de 0,5 pt, rodapé em Inter 8 pt. Sem preço confirmado, escrever “sob consulta”. Garantia: 12 meses para estrutura, tecido e mão de obra; nunca “garantia total”.</p>''', sec="Aplicações")

# 14 · Fotografia
add(head("13 · Fotografia", "A peça na casa de verdade")
 + '''<div class="cols2">
 <div><h3>Como fotografar</h3><ul class="li">
 <li>Luz natural lateral, sem flash.</li><li>Câmera na altura do assento, levemente abaixo.</li>
 <li>Sala real, com objetos de uso.</li><li>Cor do tecido preservada, sem filtro quente.</li></ul>
 <h3>Kit por peça</h3><p>Frontal no ambiente · macro do tecido · detalhe da estrutura · escala humana.</p></div>
 <div><h3>Reforma</h3><p>O par antes e depois é o ativo mais forte: mesmo ângulo, mesma luz, mesmo enquadramento.</p>
 <h3>Proibido</h3><ul class="li"><li>Banco de imagem como acervo próprio.</li><li>Ambiente ou cliente de terceiro sem autorização escrita.</li>
 <li>Peça que a marca não vende.</li><li>Marca de concorrente visível.</li></ul></div></div>''', sec="Fotografia")

# 15 · Arquivos
add(head("14 · Arquivos", "O que está no kit", "Nome dos arquivos: nobre-living-[versão]-[cor]. Cores: marinho, offwhite (negativo) e grafite. Todo texto do logo está em curvas.")
 + '''<table class="files"><tbody>
 <tr><td>svg/</td><td>Versões A–E em vetor. Use para impressão (a gráfica converte para PDF vetorial) e para editar no Figma ou Canva.</td></tr>
 <tr><td>png/@1x, @2x, @3x</td><td>As mesmas versões com fundo transparente, para redes, site e documentos.</td></tr>
 <tr><td>favicon/</td><td>16, 32, 48, 64, 192 e 512 px, ícone para iPhone (180 px) e favicon.svg.</td></tr>
 <tr><td>marca-dagua/</td><td>Logo horizontal translúcido, em off-white e marinho, para fotos.</td></tr>
 <tr><td>modelos/</td><td>Perfil, destaques, post, story, orçamento, ficha do pedido, etiqueta, cartão e assinatura de e-mail. Textos editáveis; instale Prata e Inter.</td></tr>
 </tbody></table>
 <div class="changes"><h3>Decisões desta versão em relação ao briefing 1.1</h3><ul class="li">
 <li>Fonte do nome: Prata no lugar da Bodoni Moda, porque o N da Bodoni some em tamanho pequeno.</li>
 <li>Símbolo: cena Portal (arco, pendente, sofá, vaso e piso) no lugar do sofá isolado. A marca passou a vender para a casa toda.</li>
 <li>Cantos arredondados e composição assimétrica, para manter a essência do logo de 2025.</li>
 <li>Linha de categoria mantida: Móveis e estofados · Brasília.</li></ul></div>''', sec="Arquivos")

face = lambda fam, f, w: f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{F}/{f}')}}"
fonts = face("Prata", "prata-400.ttf", 400) + "".join(face("Inter", f"inter-{w}.ttf", w) for w in (300, 400, 500, 600))

css = fonts + f'''
@page {{ size: 297mm 210mm; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 400 9.5pt/1.5 Inter, sans-serif; color: {GRAF}; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
.pg {{ width: 297mm; height: 210mm; padding: 16mm 18mm 18mm; position: relative; overflow: hidden; page-break-after: always; background: {LINEN}; }}
.pg.navy {{ background: {NAVY}; color: {LINEN}; }}
footer {{ position: absolute; left: 18mm; right: 18mm; bottom: 9mm; display: flex; justify-content: space-between; font-size: 7pt; color: #5E6470; letter-spacing: .06em; }}
h2 {{ font: 400 26pt/1.1 Prata, serif; color: {NAVY}; margin: 0 0 4mm; }}
h3 {{ font: 600 8pt/1.3 Inter; letter-spacing: .12em; text-transform: uppercase; color: {NAVY}; margin: 5mm 0 2mm; }}
.eb {{ font: 600 7.5pt/1 Inter; letter-spacing: .16em; text-transform: uppercase; color: {GOLD}; margin: 0 0 3mm; }}
.lead {{ max-width: 150mm; font-weight: 300; font-size: 11pt; margin: 0 0 8mm; }}
p {{ margin: 0 0 2mm; }}
.cover {{ height: 100%; display: grid; grid-template-columns: 1.2fr 1fr; align-items: center; }}
.cv-logo {{ width: 120mm; height: auto; justify-self: center; }}
.cv-meta p {{ color: rgba(245,242,236,.85); font-size: 11pt; }}
.cv-meta .eb {{ font-size: 9pt; }}
.cols3 {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10mm; margin-top: 6mm; }}
.cols2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12mm; margin-top: 4mm; }}
.quote {{ font: 400 20pt/1.25 Prata, serif; color: {NAVY}; }}
.valores {{ display: flex; flex-wrap: wrap; gap: 3mm; margin-top: 10mm; }}
.valores span {{ border: 0.3mm solid {GOLD}; padding: 2mm 4mm; font-size: 8.5pt; color: {NAVY}; }}
.sym {{ display: grid; grid-template-columns: 105mm 1fr; gap: 14mm; align-items: center; }}
.sym-big {{ background: #FBFAF7; padding: 6mm; }}
.s-big {{ width: 100%; height: auto; display: block; }}
.parts {{ list-style: none; padding: 0; margin: 0; }}
.parts li {{ padding: 3mm 0; border-top: 0.2mm solid rgba(20,38,61,.18); }}
.parts b {{ display: block; color: {NAVY}; font-weight: 600; }}
.levels {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; }}
.levels figure, .vers figure, .bgs figure, .wrong figure, .icons figure, .apps-d figure, .apps-p figure {{ margin: 0; }}
.lvbox {{ background: #FBFAF7; aspect-ratio: 1; display: grid; place-items: center; }}
.lv {{ width: 70%; height: auto; }}
figcaption {{ font-size: 8pt; color: #5E6470; margin-top: 2mm; }}
figcaption b {{ display: block; color: {NAVY}; font-weight: 600; font-size: 9pt; }}
.vers {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 5mm; }}
.v1, .v3, .v4 {{ grid-column: span 2; }} .v2, .v5 {{ grid-column: span 3; }}
.vb {{ height: 40mm; display: grid; place-items: center; padding: 6mm; }}
.vb.light {{ background: #FBFAF7; }} .vb.white {{ background: #fff; }} .vb.navy {{ background: {NAVY}; }}
.lg-v {{ height: 31mm; width: auto; }} .lg-h {{ width: 84%; max-height: 30mm; height: auto; }} .lg-c {{ height: 31mm; width: auto; }}
.prot {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 12mm; align-items: center; }}
.pbox {{ background: #FBFAF7; padding: 8mm; position: relative; }}
.pzone {{ outline: 0.3mm dashed {GOLD}; padding: 14mm; }}
.lg-p {{ width: 100%; height: auto; display: block; outline: 0.2mm solid rgba(20,38,61,.25); }}
.pl {{ position: absolute; top: 2.5mm; left: 8mm; font-size: 7pt; color: {GOLD}; }}
table {{ border-collapse: collapse; width: 100%; }}
td, th {{ text-align: left; padding: 2.4mm 2mm; border-bottom: 0.2mm solid rgba(20,38,61,.18); vertical-align: top; }}
th {{ font: 600 7.5pt Inter; letter-spacing: .12em; text-transform: uppercase; color: {NAVY}; }}
.sws {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 6mm; }}
.chip {{ height: 38mm; }}
.sn {{ font-weight: 600; color: {NAVY}; margin-top: 3mm; }}
.small p {{ font-size: 9pt; }}
.type {{ display: grid; grid-template-columns: 1fr 1fr 1.2fr; gap: 8mm; }}
.prata {{ font-family: Prata, serif; }} .inter {{ font-family: Inter, sans-serif; }}
.tp-n {{ font-size: 34pt; line-height: 1; color: {NAVY}; }}
.abc {{ font-size: 15pt; color: {NAVY}; }}
.hier td:first-child {{ color: {NAVY}; white-space: nowrap; }}
.hier td:last-child {{ font-size: 8pt; color: #5E6470; }}
.rules {{ margin-top: 8mm; font-size: 8.5pt; color: {NAVY}; border-top: 0.3mm solid {GOLD}; padding-top: 3mm; }}
.bgs {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 6mm; }}
.bgb {{ aspect-ratio: 1; display: grid; place-items: center; outline: 0.2mm solid rgba(20,38,61,.18); }}
.lg-bg {{ width: 62%; height: auto; }}
.wrong {{ display: grid; grid-template-columns: repeat(6, 1fr); gap: 5mm; }}
.wb {{ aspect-ratio: 1; background: #FBFAF7; display: grid; place-items: center; position: relative; overflow: hidden; }}
.lg-w {{ width: 26mm; height: auto; display: block; }}
.x {{ position: absolute; top: 1mm; right: 2.5mm; font: 600 14pt Inter; color: #9B2C2C; }}
.icons {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8mm; }}
.hl {{ width: 100%; height: auto; background: #FBFAF7; padding: 8mm; display: block; }}
.icons figcaption {{ text-align: center; font-size: 9pt; color: {NAVY}; }}
.apps-d {{ display: grid; grid-template-columns: 0.9fr 0.62fr 0.95fr 0.62fr; gap: 6mm; align-items: end; }}
.apps-d img {{ width: 100%; display: block; box-shadow: 0 1.5mm 4mm rgba(20,38,61,.18); }}
.apps-d figure:nth-child(2) img, .apps-d figure:nth-child(4) img {{ height: 104mm; width: auto; }}
.apps-p {{ display: grid; grid-template-columns: 74mm 74mm 1fr; gap: 6mm; align-items: start; }}
.apps-p img {{ width: 100%; display: block; box-shadow: 0 1.5mm 4mm rgba(20,38,61,.18); }}
.a4 img {{ height: 104mm; width: auto; }}
.small-p {{ display: grid; gap: 4mm; }}
.small-p img {{ width: 62mm; }}
.note {{ margin-top: 5mm; font-size: 8.5pt; color: #5E6470; max-width: 230mm; }}
.li {{ padding-left: 4mm; margin: 0; }} .li li {{ margin-bottom: 1.4mm; }}
.files td:first-child {{ font-weight: 600; color: {NAVY}; width: 46mm; }}
.changes {{ margin-top: 6mm; background: #FBFAF7; padding: 4mm 6mm; }}
.changes h3 {{ margin-top: 0; }}
'''
html = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><title>Nobre Living · Manual da marca</title><style>{css}</style></head><body>{''.join(pages)}</body></html>"
out = os.path.join(KIT, "manual"); os.makedirs(out, exist_ok=True)
open(os.path.join(out, "manual.html"), "w").write(html)
print("manual html ok", len(pages), "páginas")
