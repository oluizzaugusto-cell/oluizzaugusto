"""Gera os SVGs das direções de identidade visual da Nobre Living.
Texto convertido em curvas a partir de Bodoni Moda (opsz 28, 500) e Inter 500.
Uso: python3 gerar.py <pasta-de-fontes> <pasta-de-saida>
"""
import sys, os, json
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

FONTS = sys.argv[1] if len(sys.argv) > 1 else "fonts"
OUT = sys.argv[2] if len(sys.argv) > 2 else "../direcoes"
NAVY, LINEN, GRAF, GOLD = "#14263D", "#F5F2EC", "#252525", "#B49A68"

class Txt:
    def __init__(self, path):
        self.f = TTFont(path); self.gs = self.f.getGlyphSet()
        self.cmap = self.f.getBestCmap(); self.upm = self.f["head"].unitsPerEm
        self.cap = self.f["OS/2"].sCapHeight
    def path(self, text, size, track_em=0.0, x=0.0, y=0.0):
        """Retorna (d, largura). y = linha de base."""
        s = size / self.upm; pen = SVGPathPen(self.gs); cx = x
        n = len(text)
        for i, ch in enumerate(text):
            g = self.cmap[ord(ch)]
            tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
            self.gs[g].draw(tp)
            cx += self.gs[g].width * s + (track_em * size if i < n - 1 else 0)
        return pen.getCommands(), cx - x
    def cap_h(self, size): return self.cap * size / self.upm

bodoni = Txt(f"{FONTS}/bodoni-28-500.ttf")
inter = Txt(f"{FONTS}/inter-500.ttf")

# ---------- Símbolos (grade 48 × 48, traço monolinear, cantos vivos) ----------
ICONS = {
  # D1 Fio: a linha do chão sobe e vira sofá — a peça já na sala. Baixo e largo.
  "fio": {
    "full":  ["M3 34H8V22H13V28H35V22H40V34H45", "M13 22V15H35V22"],
    "small": ["M2 35H7V22H13V28H35V22H41V35H46", "M13 22V14H35V22"],
  },
  # D2 Planta: elevação técnica — contorno fechado, braços, assento, pés.
  "planta": {
    "full":  ["M7 34V23H12V15H36V23H41V34Z", "M12 23V34", "M36 23V34", "M12 28H36", "M9.5 34V37.5", "M38.5 34V37.5"],
    "small": ["M6 35V23H13V14H35V23H42V35Z", "M13 23V35", "M35 23V35"],
  },
  # D3 Vão: silhueta aberta embaixo + assento solto; o vazio é o lugar de quem senta.
  "vao": {
    "full":  ["M9 36V23H14V13H34V23H39V36", "M17 29H31"],
    "small": ["M8 37V23H14V12H34V23H40V37", "M18 30H30"],
  },
}
STROKE = {"full": 1.5, "small": 3.0}

DROP = "M24 2.5C22.6 4.9 21 6.7 21 8.6A3 3 0 0 0 27 8.6C27 6.7 25.4 4.9 24 2.5Z"
# Sistema: reforma = assento costurado (tracejado); impermeabilização = gota sobre o encosto.
SECONDARY = {
  "fio": {
    "reforma": [("M3 34H8V22H13V28", 0), ("M13 28H35", 1), ("M35 28V22H40V34H45", 0), ("M13 22V15H35V22", 0)],
  },
  "planta": {
    "reforma": [("M7 34V23H12V15H36V23H41V34Z", 0), ("M12 23V34", 0), ("M36 23V34", 0), ("M13.5 28H35", 1), ("M9.5 34V37.5", 0), ("M38.5 34V37.5", 0)],
  },
  "vao": {
    "reforma": [("M9 36V23H14V13H34V23H39V36", 0), ("M17 29H31", 1)],
  },
}
for k in SECONDARY:
    base = [(d, 0) for d in ICONS[k]["full"]]
    if k == "vao":
        base = [("M9 36V23H14V15H34V23H39V36", 0), ("M17 29H31", 0)]
    SECONDARY[k]["impermeabilizacao"] = base + [(DROP, 0)]

def secondary_group(key, which, color, x=0, y=0, scale=1.0, sw=1.5):
    out = ""
    for d, dashed in SECONDARY[key][which]:
        da = ' stroke-dasharray="2.2 1.6" stroke-linecap="butt"' if dashed else ""
        out += f'<path d="{d}"{da}/>'
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="square" stroke-linejoin="miter">{out}</g>')

def icon_group(key, color, variant="full", x=0, y=0, scale=1.0):
    sw = STROKE[variant]
    paths = "".join(f'<path d="{d}"/>' for d in ICONS[key][variant])
    return (f'<g transform="translate({x:.2f} {y:.2f}) scale({scale:.4f})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="square" stroke-linejoin="miter">{paths}</g>')

def svg(w, h, body, bg=None):
    rect = f'<rect width="100%" height="100%" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.2f} {h:.2f}" '
            f'width="{w:.0f}" height="{h:.0f}">{rect}{body}</svg>')

WORD = "NOBRE LIVING"
TAG_FULL = "MÓVEIS E ESTOFADOS · BRASÍLIA"
TAG_SHORT = "MÓVEIS · BRASÍLIA"

# Parâmetros de composição por direção
STYLE = {
  "fio":    {"track": 0.16, "rule": False, "floor_ext": True},
  "planta": {"track": 0.20, "rule": True,  "floor_ext": False},
  "vao":    {"track": 0.30, "rule": False, "floor_ext": False},
}

def wordmark(key, color, size, x, y):
    d, w = bodoni.path(WORD, size, STYLE[key]["track"], x, y)
    return f'<path fill="{color}" d="{d}"/>', w

def tagline(text, color, size, x, y, track=0.16):
    d, w = inter.path(text, size, track, x, y)
    return f'<path fill="{color}" d="{d}"/>', w

def lockup_vertical(key, color, accent=None, tag=None):
    # ícone 120 de largura, wordmark centralizada embaixo
    size = 30; cap = bodoni.cap_h(size)
    _, ww = bodoni.path(WORD, size, STYLE[key]["track"])
    W = max(ww, 120) + 2 * 40
    icon_s = 120 / 48 * 1.15
    ix = (W - 48 * icon_s) / 2
    body = icon_group(key, color, "full", ix, 10, icon_s)
    by = 10 + 48 * icon_s + 6 + cap
    p, _ = wordmark(key, color, size, (W - ww) / 2, by)
    body += p; H = by + 30
    if tag:
        ts = 9.5; _, tw = inter.path(tag, ts, 0.16)
        ty = by + 30
        if STYLE[key]["rule"]:
            body += f'<rect x="{(W-40)/2:.2f}" y="{by+13:.2f}" width="40" height="0.75" fill="{accent or color}"/>'
            ty = by + 34
        p, _ = tagline(tag, color, ts, (W - tw) / 2, ty); body += p; H = ty + 22
    return W, H, body

def lockup_horizontal(key, color, accent=None, tag=None):
    size = 30; cap = bodoni.cap_h(size)
    icon_h = 48 * 1.9  # escala do ícone
    s = 1.9
    pad = 12
    body = icon_group(key, color, "full", pad, 0, s)
    tx = pad + 48 * s + 18
    _, ww = bodoni.path(WORD, size, STYLE[key]["track"])
    if tag:
        base = icon_h / 2 + cap / 2 - 6
    else:
        base = icon_h / 2 + cap / 2 + 1
    # alinhamento ótico: base da wordmark na linha do assento quando há chão
    if key == "fio": base = 34 * s - 2 if not tag else 34 * s - 16
    p, _ = wordmark(key, color, size, tx, base); body += p
    W = tx + ww + pad
    if tag:
        ts = 8.6; ty = base + 20
        if STYLE[key]["rule"]:
            body += f'<rect x="{tx:.2f}" y="{base+9:.2f}" width="{ww:.2f}" height="0.75" fill="{accent or color}"/>'
            ty = base + 23
        p, tw = tagline(tag, color, ts, tx, ty, 0.16 if key != "vao" else 0.3); body += p
        W = max(W, tx + tw + pad)
    if key == "fio" and STYLE[key]["floor_ext"] and not tag:
        pass
    return W, icon_h + 4, body

def main():
  os.makedirs(OUT, exist_ok=True)
  manifest = {}
  for key in ICONS:
      d = os.path.join(OUT, key); os.makedirs(d, exist_ok=True); m = {}
      for cname, col, bg in [("marinho", NAVY, None), ("offwhite", LINEN, None)]:
          acc = GOLD
          files = {
            f"icone-{cname}": svg(48, 48, icon_group(key, col, "full")),
            f"icone-reducao-{cname}": svg(48, 48, icon_group(key, col, "small")),
          }
          W, H, b = lockup_vertical(key, col, acc); files[f"vertical-{cname}"] = svg(W, H, b)
          W, H, b = lockup_horizontal(key, col, acc); files[f"horizontal-{cname}"] = svg(W, H, b)
          W, H, b = lockup_horizontal(key, col, acc, TAG_FULL); files[f"assinatura-{cname}"] = svg(W, H, b)
          W, H, b = lockup_vertical(key, col, acc, TAG_SHORT); files[f"vertical-assinatura-{cname}"] = svg(W, H, b)
          for n, content in files.items():
              fn = f"nobre-living-{key}-{n}.svg"
              open(os.path.join(d, fn), "w").write(content); m[n] = fn
      manifest[key] = m
  json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w"), indent=1)
  print("ok", sum(len(v) for v in manifest.values()), "arquivos")


if __name__ == "__main__":
    main()
