"""Estudo 3: conceitos criativos de símbolo (grade 96 × 96)."""
import simbolo as sb

def sofa_g(s, x, floor, sw, var="full"):
    tx = x - sb.X0 * s; ty = floor - sb.Y_FOOT * s
    return f'<g transform="translate({tx:.3f} {ty:.3f}) scale({s})" stroke-width="{sw/s:.3f}">{sb.body(var)}</g>'

C = {}
def concept(key, **meta):
    def d(fn): C[key] = dict(fn=fn, **meta); return fn
    return d

# 1 · ALVORADA — o sofá pousa sobre as curvas das colunas do Palácio da Alvorada
@concept("alvorada", title="Alvorada", lema="Brasília no desenho",
  ideia="O sofá pousa sobre a curva das colunas do Palácio da Alvorada. É o único símbolo de móveis que só poderia ser de Brasília.")
def alvorada(sw, small=False):
    o = ""
    top, arm, seat, base = 24, 35, 44, 54
    r = 4
    sil = (f"M8 {base}V{arm+r}A{r} {r} 0 0 1 {8+r} {arm}H{19-r}A{r} {r} 0 0 1 19 {arm+r}V{top+r}A{r} {r} 0 0 1 {19+r} {top}"
           f"H{77-r}A{r} {r} 0 0 1 77 {top+r}V{arm+r}A{r} {r} 0 0 1 {77+r} {arm}H{88-r}A{r} {r} 0 0 1 88 {arm+r}V{base}Z")
    o += f'<path d="{sil}"/>'
    o += f'<path d="M19 {arm+r}V{base}"/><path d="M77 {arm+r}V{base}"/><path d="M19 {seat}H77"/>'
    if not small:
        o += f'<path d="M38.67 {top}V{seat-2.4}"/><path d="M57.33 {top}V{seat-2.4}"/>'
    # colunata: cada pé é uma coluna do Alvorada (lados côncavos que afinam até tocar o chão);
    # entre duas colunas vizinhas o vão forma um arco.
    fl = 80
    for x, w in ((18, 10), (48, 12), (78, 10)):
        o += f'<path d="M{x-w} {base}C{x-2} {base+2} {x-0.6} {base+12} {x} {fl}C{x+0.6} {base+12} {x+2} {base+2} {x+w} {base}"/>'
    return o

# 2 · DIDONE — o sofá escrito com a mesma pena do nome: verticais grossas, horizontais finas
@concept("didone", title="Didone", lema="O sofá escrito com a pena do nome",
  ideia="O sofá ganha o contraste da fonte: verticais grossas, horizontais finíssimas, pés em cunha. Símbolo e nome passam a ser uma coisa só.")
def didone(sw, small=False):
    k = 1.0 if not small else 1.35
    thick, thin = 5.2 * k, (1.1 if not small else 2.4)
    o = ""
    # finos
    o += f'<g stroke-width="{thin}">'
    o += '<path d="M19 42V33A3 3 0 0 1 22 30H74A3 3 0 0 1 77 33V42"/>'      # encosto
    o += '<path d="M10.6 42H19"/><path d="M77 42H85.4"/>'                    # topo dos braços
    o += '<path d="M19 51H77"/><path d="M8 64H88"/>'                         # assento, base
    o += '<path d="M19 42V64"/><path d="M77 42V64"/>'                         # face interna dos braços
    if not small:
        o += '<path d="M39.67 30V48.6"/><path d="M56.33 30V48.6"/>'
    o += '</g>'
    # grossos (verticais dos braços), com remate de serifa fina no topo
    o += f'<g stroke-width="{thick}" stroke-linecap="butt"><path d="M10.6 44.5V64"/><path d="M85.4 44.5V64"/></g>'
    o += f'<g stroke-width="{thin}"><path d="M8 42.6Q10.6 42 13.2 42.6" /><path d="M82.8 42.6Q85.4 42 88 42.6"/></g>'
    # pés em cunha (preenchidos)
    o += f'<path d="M13 64.5H19.5L14.6 74.5H13.2Z" fill="currentColor" stroke="none"/>'
    o += f'<path d="M83 64.5H76.5L81.4 74.5H82.8Z" fill="currentColor" stroke="none"/>'
    return o

# 3 · PORTAL — a porta em arco que se abre para a sala pronta
@concept("portal", title="Portal", lema="A casa pronta para receber",
  ideia="Um arco de porta enquadra a sala: o sofá, o pendente que desce do alto do arco e o piso que passa pelo vão. É o propósito da marca desenhado.")
def portal(sw, small=False):
    o = '<path d="M18 84V40A30 30 0 0 1 78 40V84"/>'
    o += '<path d="M8 84H88"/>'
    if not small:
        o += '<path d="M48 10V27"/><path d="M41.5 32.5A6.5 5.5 0 0 1 54.5 32.5Z"/>'
    else:
        o += '<path d="M48 10V25"/><path d="M40 32A8 7 0 0 1 56 32Z"/>'
    o += sofa_g(0.58, 23.6, 84, sw, "reducao" if small else "full")
    return o

# 4 · PLANTA BAIXA — a sala vista de cima, como no projeto
@concept("plantabaixa", title="Planta baixa", lema="A sala vista do projeto",
  ideia="A sala desenhada de cima, como numa planta de arquiteto: sofá com três assentos, mesa de centro redonda, tapete e mesa lateral com luminária. Fala de medida e de casa inteira.")
def plantabaixa(sw, small=False):
    o = ""
    o += '<path d="M16 18H80V44H16Z"/>'                       # sofá (vista de cima)
    o += '<path d="M23 25H73"/><path d="M23 25V44"/><path d="M73 25V44"/>'  # encosto e braços
    if not small:
        o += '<path d="M39.67 25V44"/><path d="M56.33 25V44"/>'
        o += '<path d="M14 50H82V82H14Z" stroke-dasharray="0.1 3.2"/>'   # tapete pontilhado
    else:
        o += '<path d="M14 52H82"/>'
    o += '<circle cx="48" cy="66" r="10"/>'                    # mesa de centro
    o += '<path d="M84 18H92V26H84Z"/><circle cx="88" cy="22" r="1.6"/>' if not small else ''
    return o

def svg(key, color, px=None, sw=2.6, small=False, bg=None, cls=""):
    rect = f'<rect width="96" height="96" fill="{bg}"/>' if bg else ""
    size = f' width="{px}" height="{px}"' if px else ""
    c = f' class="{cls}"' if cls else ""
    dy = {"alvorada": 2, "didone": -2, "portal": 0, "plantabaixa": 0}[key]
    return (f'<svg xmlns="http://www.w3.org/2000/svg"{c} viewBox="0 0 96 96"{size} style="color:{color}">{rect}'
            f'<g transform="translate(0 {dy})" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{C[key]["fn"](sw, small)}</g></svg>')
