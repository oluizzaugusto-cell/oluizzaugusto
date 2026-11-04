"""Símbolo da Nobre Living: direção Planta refinada (grade 96 × 96).
Herda do logo de 2025: encosto em três módulos, braços arredondados à frente
do encosto, pés palito inclinados. Traço único, uma cor, sem preenchimento.
Caixa do sofá: x 6–90, y 30–71 (84 × 41, proporção ~2:1).
"""
X0, X1 = 6, 90          # extremos dos braços
XI0, XI1 = 17, 79       # face interna dos braços
Y_BACK, Y_ARM, Y_SEAT, Y_BASE, Y_FOOT = 30, 42, 51, 64, 71
R = 3                   # raio dos cantos
D1 = XI0 + (XI1 - XI0) / 3
D2 = XI0 + 2 * (XI1 - XI0) / 3

def sil(r=R):
    return (f"M{X0} {Y_BASE}V{Y_ARM+r}A{r} {r} 0 0 1 {X0+r} {Y_ARM}H{XI0-r}A{r} {r} 0 0 1 {XI0} {Y_ARM+r}"
            f"V{Y_BACK+r}A{r} {r} 0 0 1 {XI0+r} {Y_BACK}H{XI1-r}A{r} {r} 0 0 1 {XI1} {Y_BACK+r}"
            f"V{Y_ARM+r}A{r} {r} 0 0 1 {XI1+r} {Y_ARM}H{X1-r}A{r} {r} 0 0 1 {X1} {Y_ARM+r}V{Y_BASE}Z")

LEGS = [f"M{X0+6} {Y_BASE}L{X0+4.6} {Y_FOOT}", f"M{X1-6} {Y_BASE}L{X1-4.6} {Y_FOOT}"]
ARMS_IN = [f"M{XI0} {Y_ARM+R}V{Y_BASE}", f"M{XI1} {Y_ARM+R}V{Y_BASE}"]
SEAT = f"M{XI0} {Y_SEAT}H{XI1}"
MODS = [f"M{D1:.3f} {Y_BACK}V{Y_SEAT-2.4}", f"M{D2:.3f} {Y_BACK}V{Y_SEAT-2.4}"]

FULL = [sil()] + ARMS_IN + [SEAT] + MODS + LEGS
# Alternativa "estofada": almofadas de assento com leve abaulado (mais próxima de 2025)
def _cush(y, c):
    return (f"M{XI0} {y}Q{(XI0+D1)/2:.2f} {c} {D1:.3f} {y}Q{(D1+D2)/2:.2f} {c} {D2:.3f} {y}"
            f"Q{(D2+XI1)/2:.2f} {c} {XI1} {y}")
ESTOFADA = [sil()] + ARMS_IN + [_cush(Y_SEAT, Y_SEAT-4), f"M{XI0} {Y_SEAT+6}H{XI1}",
            f"M{D1:.3f} {Y_SEAT}V{Y_SEAT+6}", f"M{D2:.3f} {Y_SEAT}V{Y_SEAT+6}",
            f"M{D1:.3f} {Y_BACK}V{Y_SEAT-4}", f"M{D2:.3f} {Y_BACK}V{Y_SEAT-4}"] + LEGS
# Redução (≤ 40 px): sem módulos, raio maior, traço grosso
REDUCAO = [sil(4)] + [f"M{XI0} {Y_ARM+4}V{Y_BASE}", f"M{XI1} {Y_ARM+4}V{Y_BASE}", SEAT,
           f"M{X0+6} {Y_BASE}L{X0+4.6} {Y_FOOT+1}", f"M{X1-6} {Y_BASE}L{X1-4.6} {Y_FOOT+1}"]

DROP = "M48 9C46.3 12 44.4 14.2 44.4 16.6A3.6 3.6 0 0 0 51.6 16.6C51.6 14.2 49.7 12 48 9Z"

# Espessura do traço por tamanho de uso (unidades da grade 96)
STROKES = {"fino": 1.6, "medio": 2.6, "reducao": 5.0}

def body(var="full", dashed_seat=False, drop=False):
    ps = {"full": FULL, "estofada": ESTOFADA, "reducao": REDUCAO}[var]
    out = ""
    for d in ps:
        if dashed_seat and d == SEAT:
            out += f'<path d="M{XI0+1.5} {Y_SEAT}H{XI1-1.5}" stroke-dasharray="3 2.6" stroke-linecap="butt"/>'
        else:
            out += f'<path d="{d}"/>'
    if drop:
        out += f'<path d="{DROP}"/>'
    return out

def group(color, sw, var="full", x=0, y=0, s=1.0, **kw):
    return (f'<g transform="translate({x:.3f} {y:.3f}) scale({s:.5f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body(var, **kw)}</g>')

def square(color, px=None, var="full", sw=None, bg=None, cls="", **kw):
    """Ícone quadrado (versão C). Centro ótico: sofá 30–71 → desloca -2,5."""
    if sw is None:
        sw = STROKES["reducao"] if var == "reducao" else STROKES["medio"]
    rect = f'<rect width="96" height="96" fill="{bg}"/>' if bg else ""
    size = f' width="{px}" height="{px}"' if px else ""
    c = f' class="{cls}"' if cls else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg"{c} viewBox="0 0 96 96"{size}>{rect}'
            f'{group(color, sw, var, 0, -2.5, 1, **kw)}</svg>')
