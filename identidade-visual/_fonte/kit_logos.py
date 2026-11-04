"""Kit final: versões A–E (SVG, texto em curvas) da Nobre Living.
Uso: python3 kit_logos.py <pasta-das-fontes> <pasta-kit>"""
import sys, os, json
FONTS = sys.argv[1]; KIT = sys.argv[2]
sys.argv = [sys.argv[0], FONTS]
import gerar as g
import final as fs

NAVY, LINEN, GRAF, GOLD = g.NAVY, g.LINEN, g.GRAF, g.GOLD
prata = g.Txt(f"{FONTS}/prata-400.ttf")
inter = g.Txt(f"{FONTS}/inter-500.ttf")
WORD, TAG, TAG_S = "NOBRE LIVING", "MÓVEIS E ESTOFADOS · BRASÍLIA", "MÓVEIS · BRASÍLIA"
TRACK = 0.14
BX, BY, BW, BH = fs.BOX

def wm(color, size, x, y):
    d, w = prata.path(WORD, size, TRACK, x, y); return f'<path fill="{color}" d="{d}"/>', w

def tg(text, color, size, x, y, tr):
    d, w = inter.path(text, size, tr, x, y); return f'<path fill="{color}" d="{d}"/>', w

def svg(W, H, b, title="Nobre Living"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.2f} {H:.2f}" width="{W:.0f}" height="{H:.0f}" '
            f'role="img" aria-label="{title}"><title>{title}</title>{b}</svg>')

def icon_at(color, x, y, h, cap):
    """Desenha o símbolo com altura h (caixa útil), canto superior esquerdo em x,y."""
    s = h / BH
    sw = max(cap * 0.08 / s, fs.STROKE["completo"] * 0.7)
    return fs.group(color, sw, "completo", x - BX * s, y - BY * s - fs.DY * s, s), BW * s

def vertical(color, tag=None, accent=GOLD, pad=24):
    size = 40.0; cap = prata.cap_h(size)
    _, ww = prata.path(WORD, size, TRACK)
    ih = ww * 0.62
    W = ww + 2 * pad
    iw = BW * ih / BH
    b, _ = icon_at(color, (W - iw) / 2, pad, ih, cap)
    base = pad + ih + cap * 1.0 + cap
    p, _ = wm(color, size, pad, base); b += p; H = base + pad
    if tag:
        ry = base + cap * 0.6
        b += f'<rect x="{W/2-20:.2f}" y="{ry:.2f}" width="40" height="1" fill="{accent}"/>'
        ts = cap * 0.36; _, tw = inter.path(tag, ts, 0.22)
        ty = ry + 1 + cap * 0.55 + inter.cap_h(ts)
        p, _ = tg(tag, color, ts, (W - tw) / 2, ty, 0.22); b += p; H = ty + pad
    return W, H, b

def horizontal(color, tag=None, accent=GOLD, pad=16):
    size = 40.0; cap = prata.cap_h(size)
    ih = cap * 3.1
    b, iw = icon_at(color, pad, pad, ih, cap)
    tx = pad + iw + cap * 0.75
    _, ww = prata.path(WORD, size, TRACK)
    H = ih + 2 * pad
    if not tag:
        base = pad + ih * 0.62 + cap / 2
        p, _ = wm(color, size, tx, base); b += p
    else:
        ts = cap * 0.30
        block = cap + cap * 0.42 + 1 + cap * 0.42 + inter.cap_h(ts)
        top = pad + ih * 0.6 - block / 2
        base = top + cap
        p, _ = wm(color, size, tx, base); b += p
        ry = base + cap * 0.42
        b += f'<rect x="{tx:.2f}" y="{ry:.2f}" width="{ww:.2f}" height="0.9" fill="{accent}"/>'
        _, t0 = inter.path(tag, ts, 0); tr = (ww - t0) / (len(tag) - 1) / ts
        ty = ry + 0.9 + cap * 0.42 + inter.cap_h(ts)
        p, _ = tg(tag, color, ts, tx, ty, tr); b += p
    return tx + ww + pad, H, b

def icone(color, level="completo", bg=None):
    return fs.square(color, None, level, bg=bg).replace(
        'role="img" aria-label="Nobre Living">', 'role="img" aria-label="Nobre Living"><title>Nobre Living</title>')

CORES = {"marinho": NAVY, "offwhite": LINEN, "grafite": GRAF}

def build():
    out = os.path.join(KIT, "svg"); os.makedirs(out, exist_ok=True)
    files = {}
    for cn, c in CORES.items():
        acc = GOLD if cn != "grafite" else GRAF
        files[f"a-vertical-{cn}"] = svg(*vertical(c))
        files[f"a-vertical-assinatura-{cn}"] = svg(*vertical(c, TAG_S, acc))
        files[f"b-horizontal-{cn}"] = svg(*horizontal(c))
        files[f"c-icone-{cn}"] = icone(c)
        files[f"c-icone-reducao-{cn}"] = icone(c, "reducao")
        files[f"c-icone-micro-{cn}"] = icone(c, "micro")
        files[f"e-assinatura-{cn}"] = svg(*horizontal(c, TAG, acc))
    # D · monocromática: uma cor só, inclusive a linha de categoria (gravação, bordado, carimbo)
    for cn, c in CORES.items():
        files[f"d-monocromatica-vertical-{cn}"] = svg(*vertical(c, TAG_S, c))
        files[f"d-monocromatica-horizontal-{cn}"] = svg(*horizontal(c, TAG, c))
    for k, v in files.items():
        open(os.path.join(out, f"nobre-living-{k}.svg"), "w").write(v)
    json.dump(sorted(files), open(os.path.join(out, "_lista.json"), "w"), indent=1)
    print("svg", len(files))

if __name__ == "__main__":
    build()
