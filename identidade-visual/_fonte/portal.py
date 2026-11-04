"""Variações do símbolo Portal (grade 96 × 96): arco de porta + sala.
Elementos combináveis: pendente, quadro, vaso, tapete."""
import simbolo as sb

FLOOR = 84
AX0, AX1, ATOP = 18, 78, 10          # arco: laterais e topo
R = (AX1 - AX0) / 2

def sofa(s, x, sw, var="full"):
    tx = x - sb.X0 * s; ty = FLOOR - sb.Y_FOOT * s
    return f'<g transform="translate({tx:.3f} {ty:.3f}) scale({s})" stroke-width="{sw/s:.3f}">{sb.body(var)}</g>'

def arch(floor_ext=(8, 88)):
    cy = ATOP + R
    return (f'<path d="M{AX0} {FLOOR}V{cy}A{R} {R} 0 0 1 {AX1} {cy}V{FLOOR}"/>'
            f'<path d="M{floor_ext[0]} {FLOOR}H{floor_ext[1]}"/>')

def _arch_y(x):
    import math
    return ATOP + R - math.sqrt(max(R * R - (x - 48) ** 2, 0))

def pendente(small, cx=48):
    y0 = round(_arch_y(cx), 2)
    if small:
        return f'<path d="M{cx} {y0}V25"/><path d="M{cx-8} 32A8 7 0 0 1 {cx+8} 32Z"/>'
    return f'<path d="M{cx} {y0}V27"/><path d="M{cx-6.5} 32.5A6.5 5.5 0 0 1 {cx+6.5} 32.5Z"/>'

def quadro(small, cx=48, y=30, w=22, h=16):
    o = f'<path d="M{cx-w/2} {y}H{cx+w/2}V{y+h}H{cx-w/2}Z"/>'
    if not small:
        o += f'<path d="M{cx-w/2+4} {y+4}H{cx+w/2-4}V{y+h-4}H{cx-w/2+4}Z" stroke-width="1.1"/>'
    return o

def vaso(small, x=70):
    # ânfora baixa com dois galhos secos (sem folhas)
    body = (f'<path d="M{x-3} {FLOOR}C{x-7} {FLOOR-4} {x-7} {FLOOR-10} {x-2.6} {FLOOR-13}V{FLOOR-16}'
            f'H{x+2.6}V{FLOOR-13}C{x+7} {FLOOR-10} {x+7} {FLOOR-4} {x+3} {FLOOR}Z"/>')
    if small:
        return body + f'<path d="M{x} {FLOOR-16}V{FLOOR-27}"/>'
    return body + (f'<path d="M{x-0.5} {FLOOR-16}C{x-1} {FLOOR-25} {x-3} {FLOOR-31} {x-6} {FLOOR-36}"/>'
                   f'<path d="M{x+0.5} {FLOOR-16}C{x+1} {FLOOR-24} {x+3} {FLOOR-29} {x+5.5} {FLOOR-33}"/>'
                   f'<path d="M{x-2} {FLOOR-28}L{x+1.5} {FLOOR-32}"/>')

def tapete(small, x0=26, x1=70, depth=6, spread=7):
    o = f'<path d="M{x0} {FLOOR}L{x0-spread} {FLOOR+depth}H{x1+spread}L{x1} {FLOOR}"/>'
    if not small:
        n = 9
        for i in range(n):
            fx = x0 - spread + 4 + i * ((x1 - x0 + 2 * spread - 8) / (n - 1))
            o += f'<path d="M{fx:.2f} {FLOOR+depth+1.6}V{FLOOR+depth+3.4}" stroke-width="1.1"/>'
    return o

V = {}
def variant(key, title, desc, dy=0):
    def d(fn): V[key] = dict(fn=fn, title=title, desc=desc, dy=dy); return fn
    return d

@variant("pendente", "Pendente", "A versão do estudo 3: luz que desce do alto do arco.", dy=1)
def v_pendente(sw, small):
    return arch() + pendente(small) + sofa(0.58, 23.6, sw, "reducao" if small else "full")

@variant("quadro", "Quadro", "Um quadro na parede no lugar da luz. Mais galeria, mais curadoria.", dy=1)
def v_quadro(sw, small):
    return arch() + quadro(small) + sofa(0.58, 23.6, sw, "reducao" if small else "full")

@variant("pendente-tapete", "Pendente + tapete", "O tapete em perspectiva dá profundidade: a sala ganha chão de verdade.", dy=-3)
def v_pt(sw, small):
    return arch() + pendente(small) + tapete(small) + sofa(0.58, 23.6, sw, "reducao" if small else "full")

@variant("quadro-tapete", "Quadro + tapete", "Galeria com profundidade. O quadro e a franja do tapete conversam.", dy=-3)
def v_qt(sw, small):
    return arch() + quadro(small) + tapete(small) + sofa(0.58, 23.6, sw, "reducao" if small else "full")

@variant("vaso", "Pendente + vaso", "O sofá vai para a esquerda e um vaso com galhos secos ocupa o canto. Assimétrico, mais vivido.", dy=1)
def v_vaso(sw, small):
    return arch() + pendente(small, 40) + sofa(0.44, 21.5, sw, "reducao" if small else "full") + vaso(small, 69)

@variant("completo", "Quadro + vaso + tapete", "A sala completa: parede, chão e um objeto de afeto. A mais rica, a mais difícil em tamanho pequeno.", dy=-3)
def v_completo(sw, small):
    return (arch() + quadro(small, 40, 32, 18, 13) + tapete(small, 22, 60, 6, 6)
            + sofa(0.44, 21.5, sw, "reducao" if small else "full") + vaso(small, 69))

def svg(key, color, px=None, sw=2.6, small=False, bg=None, cls=""):
    rect = f'<rect width="96" height="96" fill="{bg}"/>' if bg else ""
    size = f' width="{px}" height="{px}"' if px else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg"{c} viewBox="0 0 96 96"{size} role="img" aria-label="Símbolo Portal">{rect}'
            f'<g transform="translate(0 {V[key]["dy"]})" fill="none" stroke="{color}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round">{V[key]["fn"](sw, small)}</g></svg>')
