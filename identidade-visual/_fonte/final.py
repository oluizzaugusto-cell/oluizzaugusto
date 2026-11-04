"""Símbolo final da Nobre Living: Portal com pendente e vaso (grade 96 × 96).
Três níveis de detalhe:
  completo  ≥ 64 px  · galhos do vaso, módulos do sofá
  reducao   24–63 px · vaso com uma haste, sofá sem módulos, traço grosso
  micro     ≤ 20 px  · arco, pendente, sofá e vaso em silhueta simples
"""
import math
import simbolo as sb

FLOOR, AX0, AX1, ATOP = 84, 18, 78, 10
R = (AX1 - AX0) / 2
CY = ATOP + R
DY = 1  # centro ótico no quadrado

def arch_y(x):
    return CY - math.sqrt(max(R * R - (x - 48) ** 2, 0))

def sofa(s, x, sw, var):
    tx = x - sb.X0 * s; ty = FLOOR - sb.Y_FOOT * s
    return f'<g transform="translate({tx:.3f} {ty:.3f}) scale({s})" stroke-width="{sw/s:.3f}">{sb.body(var)}</g>'

def arch():
    return (f'<path d="M{AX0} {FLOOR}V{CY}A{R} {R} 0 0 1 {AX1} {CY}V{FLOOR}"/>'
            f'<path d="M8 {FLOOR}H88"/>')

def pendente(level, cx=40):
    y0 = round(arch_y(cx), 2)
    if level == "completo":
        return f'<path d="M{cx} {y0}V27"/><path d="M{cx-6.5} 32.5A6.5 5.5 0 0 1 {cx+6.5} 32.5Z"/>'
    return f'<path d="M{cx} {y0}V25"/><path d="M{cx-8} 32A8 7 0 0 1 {cx+8} 32Z"/>'

def vaso(level, x=69):
    F = FLOOR
    body = (f'<path d="M{x-3} {F}C{x-7} {F-4} {x-7} {F-10} {x-2.6} {F-13}V{F-16}'
            f'H{x+2.6}V{F-13}C{x+7} {F-10} {x+7} {F-4} {x+3} {F}Z"/>')
    if level == "completo":
        return body + (f'<path d="M{x-0.5} {F-16}C{x-1} {F-25} {x-3} {F-31} {x-6} {F-36}"/>'
                       f'<path d="M{x+0.5} {F-16}C{x+1} {F-24} {x+3} {F-29} {x+5.5} {F-33}"/>'
                       f'<path d="M{x-2} {F-28}L{x+1.5} {F-32}"/>')
    if level == "reducao":
        return body + f'<path d="M{x} {F-16}V{F-27}"/>'
    return body

def inner(level, sw):
    var = "full" if level == "completo" else "reducao"
    return arch() + pendente(level) + sofa(0.44, 21.5, sw, var) + vaso(level)

STROKE = {"completo": 2.2, "reducao": 4.4, "micro": 6.0}

def level_for(px):
    if px is None or px >= 64: return "completo"
    return "reducao" if px > 20 else "micro"

def group(color, sw=None, level="completo", x=0, y=0, s=1.0):
    sw = sw or STROKE[level]
    return (f'<g transform="translate({x:.3f} {y + DY * s:.3f}) scale({s:.5f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{inner(level, sw)}</g>')

def square(color, px=None, level=None, sw=None, bg=None, cls="", pad=0):
    level = level or level_for(px)
    rect = f'<rect x="{-pad}" y="{-pad}" width="{96+2*pad}" height="{96+2*pad}" fill="{bg}"/>' if bg else ""
    size = f' width="{px}" height="{px}"' if px else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg"{c} viewBox="{-pad} {-pad} {96+2*pad} {96+2*pad}"{size} '
            f'role="img" aria-label="Nobre Living">{rect}{group(color, sw, level)}</svg>')

# caixa útil do desenho (para composições)
BOX = (8, ATOP, 80, FLOOR - ATOP)   # x, y, w, h
