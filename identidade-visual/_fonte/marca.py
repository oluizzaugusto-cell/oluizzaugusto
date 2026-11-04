"""Composições oficiais (versões A–E) da Planta refinada, em curvas."""
import sys, os
import gerar as g
import simbolo as sb

NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
WORD, TAG, TAG_S = g.WORD, g.TAG_FULL, g.TAG_SHORT
TRACK = 0.14
SOFA_W = sb.X1 - sb.X0

def wm(color, size, x, y):
    d, w = g.bodoni.path(WORD, size, TRACK, x, y)
    return f'<path fill="{color}" d="{d}"/>', w

def tg(text, color, size, x, y, track=0.2):
    d, w = g.inter.path(text, size, track, x, y)
    return f'<path fill="{color}" d="{d}"/>', w

def svg(W, H, b, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg"{c} viewBox="0 0 {W:.2f} {H:.2f}" '
            f'width="{W:.0f}" height="{H:.0f}" role="img" aria-label="Nobre Living">{b}</svg>')

def vertical(color, tag=None, accent=GOLD, pad=24):
    """A: ícone sobre a wordmark. Sofá ≈ 68% da largura do nome."""
    size = 40.0
    cap = g.bodoni.cap_h(size)
    _, ww = g.bodoni.path(WORD, size, TRACK)
    sofa_px = ww * 0.68
    s = sofa_px / SOFA_W
    sw = cap * 0.075 / s
    W = ww + 2 * pad
    ix = (W - sofa_px) / 2 - sb.X0 * s
    iy = pad - sb.Y_BACK * s
    b = sb.group(color, sw, "full", ix, iy, s)
    foot = pad + (sb.Y_FOOT - sb.Y_BACK) * s
    base = foot + cap * 1.05 + cap
    p, _ = wm(color, size, pad, base); b += p
    H = base + pad
    if tag:
        b += f'<rect x="{W/2-18:.2f}" y="{base + cap*0.55:.2f}" width="36" height="1" fill="{accent}"/>'
        ts = cap * 0.34
        _, tw = g.inter.path(tag, ts, 0.2)
        ty = base + cap * 0.55 + 1 + cap * 0.5 + g.inter.cap_h(ts)
        p, _ = tg(tag, color, ts, (W - tw) / 2, ty); b += p
        H = ty + pad
    return W, H, b

def horizontal(color, tag=None, accent=GOLD, pad=16):
    """B: ícone à esquerda; linha de base do nome = base do sofá; altura de versal = braço→base."""
    size = 40.0
    cap = g.bodoni.cap_h(size)
    s = cap / (sb.Y_BASE - sb.Y_ARM)
    sw = cap * 0.075 / s
    ix = pad - sb.X0 * s
    top = pad
    iy = top - sb.Y_BACK * s
    b = sb.group(color, sw, "full", ix, iy, s)
    base = iy + sb.Y_BASE * s
    tx = pad + SOFA_W * s + cap * 0.9
    p, ww = wm(color, size, tx, base); b += p
    W = tx + ww + pad
    H = iy + sb.Y_FOOT * s + pad
    if tag:
        ry = base + cap * 0.42
        b += f'<rect x="{tx:.2f}" y="{ry:.2f}" width="{ww:.2f}" height="0.9" fill="{accent}"/>'
        ts = cap * 0.30
        # entreletra calculada para a assinatura ocupar a largura do nome
        _, t0 = g.inter.path(tag, ts, 0)
        tr = (ww - t0) / (len(tag) - 1) / ts
        ty = ry + 0.9 + cap * 0.42 + g.inter.cap_h(ts)
        p, _ = tg(tag, color, ts, tx, ty, tr); b += p
        H = max(H, ty + pad)
    return W, H, b

def icone(color, var="full"):
    return sb.square(color, None, var, sb.STROKES["medio"] if var != "reducao" else None)

def write_all(out):
    os.makedirs(out, exist_ok=True)
    cores = {"marinho": NAVY, "offwhite": LINEN, "grafite": GRAF}
    n = 0
    for cname, col in cores.items():
        files = {
            f"vertical-{cname}": svg(*vertical(col)),
            f"horizontal-{cname}": svg(*horizontal(col)),
            f"icone-{cname}": icone(col),
            f"icone-reducao-{cname}": icone(col, "reducao"),
            f"assinatura-{cname}": svg(*horizontal(col, TAG, GOLD if cname != "grafite" else col)),
            f"vertical-assinatura-{cname}": svg(*vertical(col, TAG_S, GOLD if cname != "grafite" else col)),
        }
        for k, v in files.items():
            open(os.path.join(out, f"nobre-living-{k}.svg"), "w").write(v); n += 1
    print("marca ok", n, "arquivos")

if __name__ == "__main__":
    write_all(sys.argv[2] if len(sys.argv) > 2 else "../marca/svg")
