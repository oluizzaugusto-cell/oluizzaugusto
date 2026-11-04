"""Estudos de símbolo 'casa toda': sofá + iluminação/apoio (grade 96 × 96).
O sofá é o da Planta refinada (simbolo.py), escalado e reposicionado."""
import simbolo as sb

FLOOR = 72

def sofa(s, x, sw, var="full"):
    """Sofá escalado por s, com o pé tocando o chão (FLOOR) e o braço esquerdo em x."""
    tx = x - sb.X0 * s
    ty = FLOOR - sb.Y_FOOT * s
    return (f'<g transform="translate({tx:.3f} {ty:.3f}) scale({s})" stroke-width="{sw/s:.3f}">'
            f'{sb.body(var)}</g>'), (lambda X, Y: (tx + X * s, ty + Y * s))

def arm_top(s, x):
    return FLOOR - (sb.Y_FOOT - sb.Y_ARM) * s

STUDIES = {}

def study(key, title, desc, dy=10):
    def deco(fn):
        STUDIES[key] = dict(title=title, desc=desc, fn=fn, dy=dy); return fn
    return deco

@study("piso", "Sofá + luminária de piso", "Luminária de haste reta com cúpula ao lado do braço. A leitura mais direta de sala completa.", dy=1)
def piso(sw, small=False):
    s = 0.70
    g, P = sofa(s, 4, sw, "reducao" if small else "full")
    lx = 82
    lamp = (f'<path d="M{lx} {FLOOR}V33"/>'
            f'<path d="M{lx-6.5} 33L{lx-3.5} 22H{lx+3.5}L{lx+6.5} 33Z"/>'
            f'<path d="M{lx-5} {FLOOR}H{lx+5}"/>')
    return g + lamp

@study("pendente", "Sofá + pendente", "Luminária pendente centrada sobre o sofá. Mantém a simetria do briefing e dá altura ao símbolo.")
def pendente(sw, small=False):
    s = 0.86
    w = (sb.X1 - sb.X0) * s
    g, P = sofa(s, (96 - w) / 2, sw, "reducao" if small else "full")
    top = FLOOR - (sb.Y_FOOT - sb.Y_BACK) * s
    cy = top - 8
    lamp = (f'<path d="M48 4V{cy-9}"/>' if not small else f'<path d="M48 8V{cy-9}"/>')
    lamp += f'<path d="M38 {cy}A10 9 0 0 1 58 {cy}Z"/>'
    return g + lamp

@study("abajur", "Sofá + mesa lateral com abajur", "Mesa de apoio na altura do braço, com abajur. Mostra móvel, apoio e luz numa cena só.", dy=-6)
def abajur(sw, small=False):
    s = 0.66
    g, P = sofa(s, 3, sw, "reducao" if small else "full")
    ty = round(arm_top(s, 3) + 1, 2)
    x0, x1 = 66, 92
    tb = (f'<path d="M{x0} {ty}H{x1}"/>'
          f'<path d="M{x0+3} {ty}V{FLOOR}"/><path d="M{x1-3} {ty}V{FLOOR}"/>')
    cx = (x0 + x1) / 2
    lamp = (f'<path d="M{cx} {ty}V{ty-9}"/><path d="M{cx-4} {ty}H{cx+4}"/>'
            f'<path d="M{cx-7} {ty-9}L{cx-4.5} {ty-18}H{cx+4.5}L{cx+7} {ty-9}Z"/>')
    return g + tb + lamp

@study("arco", "Sofá + luminária de arco", "Uma linha nasce no chão, faz um arco sobre o sofá e acende sobre o assento. Gesto único, mais autoral.", dy=8)
def arco(sw, small=False):
    s = 0.74
    g, P = sofa(s, 3, sw, "reducao" if small else "full")
    bx = 88
    arc = (f'<path d="M{bx} {FLOOR}V30C{bx} 12 70 8 52 12C46 13.4 42 16 40 20"/>'
           f'<path d="M{bx-5} {FLOOR}H{bx+5}"/>'
           f'<path d="M33 27A7.2 6.4 0 0 1 47 27Z" transform="rotate(14 40 25)"/>')
    return g + arc

def svg(key, color, px=None, sw=2.6, small=False, bg=None):
    rect = f'<rect width="96" height="96" fill="{bg}"/>' if bg else ""
    size = f' width="{px}" height="{px}"' if px else ""
    inner = STUDIES[key]["fn"](sw, small)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"{size}>{rect}'
            f'<g transform="translate(0 {STUDIES[key]["dy"]})" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{inner}</g></svg>')
