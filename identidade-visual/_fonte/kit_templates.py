"""Modelos editáveis das aplicações (SVG). Textos ficam como texto (Prata e Inter,
ambas no Google Fonts, Figma e Canva); o logo entra em curvas.
Uso: python3 kit_templates.py <pasta-kit>"""
import sys, os, re
KIT = sys.argv[1]
SVG = os.path.join(KIT, "svg"); OUT = os.path.join(KIT, "modelos"); os.makedirs(OUT, exist_ok=True)
NAVY, LINEN, GRAF, GOLD = "#14263D", "#F5F2EC", "#252525", "#B49A68"
MUTED = "#5E6470"
TEL, MAIL, IG = "(61) 99604-4750", "nobrelivingg@gmail.com", "@nobreliving"
GARANTIA = "Garantia de 12 meses: estrutura, tecido e mão de obra."
P, I = "Prata, Georgia, 'Times New Roman', serif", "Inter, system-ui, 'Segoe UI', sans-serif"

def logo(name, x, y, w=None, h=None):
    s = open(os.path.join(SVG, f"nobre-living-{name}.svg")).read()
    vb = list(map(float, re.search(r'viewBox="([^"]+)"', s).group(1).split()))
    if w is None: w = h * vb[2] / vb[3]
    if h is None: h = w * vb[3] / vb[2]
    inner = s[s.index(">") + 1: s.rindex("</svg>")]
    inner = re.sub(r"<title>.*?</title>", "", inner)
    return f'<svg x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" viewBox="{" ".join(map(str, vb))}">{inner}</svg>', w, h

def doc(w, h, body, unit="", title=""):
    size = f'width="{w}{unit}" height="{h}{unit}"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" {size}>'
            f'<title>{title}</title>{body}</svg>')

def t(x, y, s, txt, font=I, weight=400, fill=GRAF, anchor="start", ls=0, extra=""):
    lsp = f' letter-spacing="{ls}"' if ls else ""
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{s}" font-weight="{weight}" fill="{fill}" '
            f'text-anchor="{anchor}"{lsp}{extra}>{txt}</text>')

def placeholder(x, y, w, h, label, fill="#E4DED4", col=MUTED, fs=24):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"/>'
            + t(x + w / 2, y + h / 2, fs, label, fill=col, anchor="middle", ls=fs * 0.08))

def write(name, svg):
    open(os.path.join(OUT, name), "w").write(svg)

# Ícones de destaque, no mesmo traço do símbolo (grade 96)
def hl_icon(kind, color, sw=3.2):
    import simbolo as sb
    sofa = lambda s, x, y: f'<g transform="translate({x - sb.X0*s} {y - sb.Y_BACK*s}) scale({s})" stroke-width="{sw/s:.3f}">{sb.body("full")}</g>'
    if kind == "colecao":
        o = sofa(0.9, 10, 34) + '<path d="M48 8V22"/><path d="M41 27A7 6 0 0 1 55 27Z"/>'
    elif kind == "entrega":   # caixa em perspectiva + 48 h implícito no título
        o = ('<path d="M48 18L80 32V66L48 80L16 66V32Z"/><path d="M16 32L48 46L80 32"/><path d="M48 46V80"/>'
             '<path d="M32 25L64 39V50"/>')
    elif kind == "sobmedida": # sofá com cota de medida acima
        o = sofa(0.84, 13, 40) + '<path d="M13 26H83"/><path d="M13 22V30"/><path d="M83 22V30"/>'
    else:                     # cuidados: gota
        o = '<path d="M48 14C40 28 30 40 30 54A18 18 0 0 0 66 54C66 40 56 28 48 14Z"/><path d="M40 56A8 8 0 0 0 48 64"/>'
    return f'<g fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{o}</g>'

def main():
    # 1 · Perfil Instagram / WhatsApp 512
    l, w, h = logo("c-icone-offwhite", 96, 96, 320)
    write("01-perfil-512.svg", doc(512, 512, f'<rect width="512" height="512" fill="{NAVY}"/>{l}', title="Perfil 512"))

    # 2 · Capas de destaque 1080×1920 (o círculo visível fica no centro)
    for kind, label in [("colecao", "Coleção"), ("entrega", "Entrega"), ("sobmedida", "Sob medida"), ("cuidados", "Cuidados")]:
        body = (f'<rect width="1080" height="1920" fill="{NAVY}"/>'
                f'<g transform="translate(300 720) scale(5)">{hl_icon(kind, LINEN, 2.6)}</g>'
                + t(540, 1330, 44, label.upper(), fill=LINEN, anchor="middle", ls=6, weight=500))
        write(f"02-destaque-{kind}-1080x1920.svg", doc(1080, 1920, body, title=f"Destaque {label}"))

    # 3 · Post de peça 1080×1350 (margem 72, base 8)
    l, lw, lh = logo("b-horizontal-marinho", 0, 0, 300)
    l, lw, lh = logo("b-horizontal-marinho", 1008 - 300, 1350 - 72 - lh, 300)
    body = (f'<rect width="1080" height="1350" fill="{LINEN}"/>'
            + placeholder(72, 72, 936, 960, "FOTO DA PEÇA · LUZ NATURAL LATERAL")
            + t(72, 1124, 60, "Nome da peça", font=P, fill=NAVY)
            + t(72, 1176, 22, "PRONTA ENTREGA · 48 H", weight=600, ls=2.6, fill=GRAF)
            + t(72, 1248, 40, "Sob consulta", weight=600, fill=NAVY)
            + f'<rect x="72" y="1200" width="96" height="1.5" fill="{GOLD}"/>' + l)
    write("03-post-peca-1080x1350.svg", doc(1080, 1350, body, title="Post de peça"))

    # 4 · Story de disponibilidade 1080×1920 (zona segura 250 topo, 340 base)
    l, lw, lh = logo("a-vertical-offwhite", 0, 0, 220)
    l, lw, lh = logo("a-vertical-offwhite", (1080 - 220) / 2, 1920 - 340 - lh, 220)
    body = (f'<rect width="1080" height="1920" fill="{NAVY}"/>'
            + placeholder(72, 250, 936, 760, "FOTO DA PEÇA", fill="#22344B", col="#AEB6C2")
            + t(72, 1096, 24, "DISPONÍVEL", weight=600, ls=3.4, fill=GOLD)
            + t(72, 1172, 72, "Nome da peça", font=P, fill=LINEN)
            + t(72, 1228, 28, "Pronta entrega em 48 h · Sob consulta", fill=LINEN, weight=300)
            + t(72, 1274, 28, f"WhatsApp {TEL}", fill=LINEN, weight=600) + l)
    write("04-story-disponibilidade-1080x1920.svg", doc(1080, 1920, body, title="Story de disponibilidade"))

    # 5 · Orçamento A4 (mm). Margem 20, logo horizontal 50 mm, fio dourado 0,5 pt, rodapé Inter 8 pt
    pt = 0.3528
    def a4_header(titulo, campos):
        l, lw, lh = logo("b-horizontal-marinho", 20, 16, 52)
        o = f'<rect width="210" height="297" fill="#FFFFFF"/>' + l
        o += t(190, 24, 4.2, titulo, weight=600, fill=NAVY, anchor="end", ls=0.7)
        for i, c in enumerate(campos):
            o += t(190, 30.5 + i * 5, 3.0, c, fill=GRAF, anchor="end")
        o += f'<rect x="20" y="{16 + lh + 6:.2f}" width="170" height="{0.5*pt:.3f}" fill="{GOLD}"/>'
        return o, 16 + lh + 6
    def footer():
        return (f'<rect x="20" y="279" width="170" height="{0.5*pt:.3f}" fill="{GOLD}"/>'
                + t(20, 284, 8 * pt, f"Nobre Living · Móveis e estofados · Brasília/DF", fill=GRAF)
                + t(190, 284, 8 * pt, f"{TEL} · {MAIL} · {IG}", fill=GRAF, anchor="end"))
    def label(x, y, s): return t(x, y, 2.5, s.upper(), weight=600, fill=NAVY, ls=0.35)
    def line(x, y, w): return f'<rect x="{x}" y="{y}" width="{w}" height="0.2" fill="#C9CCD2"/>'

    o, y0 = a4_header("ORÇAMENTO", ["Nº ______", "Data: __/__/____", "Válido até: __/__/____"])
    y = y0 + 12
    o += label(20, y, "Cliente") + line(20, y + 6, 105) + label(132, y, "Telefone") + line(132, y + 6, 58)
    y += 14
    o += label(20, y, "Endereço de entrega") + line(20, y + 6, 170)
    y += 16
    cols = [(20, "Item"), (32, "Descrição"), (128, "Qtd"), (142, "Prazo"), (166, "Valor")]
    o += f'<rect x="20" y="{y-5}" width="170" height="8" fill="{LINEN}"/>'
    for x, c in cols: o += label(x + 2, y, c)
    for r in range(8):
        yy = y + 4 + (r + 1) * 9
        o += line(20, yy, 170)
    y = y + 4 + 9 * 8 + 10
    o += label(128, y, "Total") + line(142, y + 1, 48)
    y += 14
    o += label(20, y, "Condições")
    cond = ["Pagamento: ____________________________________________",
            "Prazo de entrega: confirmado item a item, contado a partir de ____________",
            GARANTIA,
            "Itens sem preço confirmado aparecem como “sob consulta”."]
    for i, c in enumerate(cond): o += t(20, y + 7 + i * 6, 3.0, c, fill=GRAF)
    y += 7 + len(cond) * 6 + 14
    o += line(20, y + 14, 75) + t(20, y + 19, 2.6, "Nobre Living", fill=MUTED) + line(115, y + 14, 75) + t(115, y + 19, 2.6, "Cliente", fill=MUTED)
    o += footer()
    write("05-orcamento-a4.svg", doc(210, 297, o, "mm", "Orçamento A4"))

    # 6 · Ficha do pedido / contrato A4
    o, y0 = a4_header("FICHA DO PEDIDO", ["Pedido nº ______", "Data: __/__/____"])
    y = y0 + 12
    rows = [("Cliente", 105, "CPF", 58), ("Telefone", 60, "E-mail", 103), ("Endereço de entrega", 170, None, 0)]
    for a, wa, b, wb in rows:
        o += label(20, y, a) + line(20, y + 6, wa)
        if b: o += label(20 + wa + 7, y, b) + line(20 + wa + 7, y + 6, wb)
        y += 14
    y += 2
    o += label(20, y, "Serviço")
    for i, s in enumerate(["Pronta entrega", "Sob medida", "Reforma", "Impermeabilização"]):
        x = 20 + i * 43
        o += f'<rect x="{x}" y="{y+3}" width="3.6" height="3.6" fill="none" stroke="{NAVY}" stroke-width="0.25"/>' + t(x + 5.5, y + 6.2, 3.0, s)
    y += 16
    for a, wa, b, wb in [("Peça", 105, "Quantidade", 58), ("Medidas (L × P × A, cm)", 105, "Tecido / cor", 58), ("Prazo combinado", 80, "Valor", 83)]:
        o += label(20, y, a) + line(20, y + 6, wa) + label(20 + wa + 7, y, b) + line(20 + wa + 7, y + 6, wb)
        y += 14
    o += label(20, y, "Forma de pagamento") + line(20, y + 6, 170); y += 14
    o += label(20, y, "Observações")
    for i in range(4): o += line(20, y + 6 + i * 7, 170)
    y += 6 + 4 * 7 + 10
    o += label(20, y, "Condições do contrato")
    o += t(20, y + 7, 3.0, GARANTIA)
    o += t(20, y + 13, 3.0, "[Inserir aqui o texto contratual revisado. Não usar “garantia total”.]", fill=MUTED)
    y += 40
    o += line(20, y, 75) + t(20, y + 5, 2.6, "Nobre Living", fill=MUTED) + line(115, y, 75) + t(115, y + 5, 2.6, "Cliente", fill=MUTED)
    o += footer()
    write("06-ficha-pedido-a4.svg", doc(210, 297, o, "mm", "Ficha do pedido A4"))

    # 7 · Etiqueta de peça 90×50 mm (logo horizontal a 32 mm)
    l, lw, lh = logo("b-horizontal-marinho", 6, 5, 34)
    o = f'<rect width="90" height="50" fill="#FFFFFF"/>' + l
    o += f'<rect x="6" y="{5+lh+2.5:.2f}" width="78" height="0.18" fill="{GOLD}"/>'
    yy = 5 + lh + 8
    for i, c in enumerate(["PEÇA", "TECIDO", "PEDIDO Nº"]):
        o += t(6, yy + i * 6, 2.3, c, weight=600, fill=NAVY, ls=0.3) + f'<rect x="24" y="{yy + i*6 + 0.4:.2f}" width="60" height="0.15" fill="#C9CCD2"/>'
    o += t(6, 46, 2.2, GARANTIA)
    write("07-etiqueta-90x50mm.svg", doc(90, 50, o, "mm", "Etiqueta de peça"))

    # 8 · Cartão de pós-entrega 90×50 mm (frente e verso)
    l, lw, lh = logo("a-vertical-offwhite", 0, 0, None, 30)
    l, lw, lh = logo("a-vertical-offwhite", (90 - lw) / 2, 10, None, 30)
    write("08-cartao-pos-entrega-frente-90x50mm.svg", doc(90, 50, f'<rect width="90" height="50" fill="{NAVY}"/>' + l, "mm", "Cartão frente"))
    o = f'<rect width="90" height="50" fill="{LINEN}"/>'
    o += t(7, 13, 5.2, "Sua peça está em casa.", font=P, fill=NAVY)
    o += t(7, 21, 2.7, "Garantia de 12 meses para estrutura, tecido", fill=GRAF)
    o += t(7, 25, 2.7, "e mão de obra. Qualquer ajuste, fale com a gente.", fill=GRAF)
    o += f'<rect x="7" y="33" width="12" height="0.18" fill="{GOLD}"/>'
    o += t(7, 39, 2.5, TEL, weight=600, fill=NAVY, ls=0.2) + t(7, 43.5, 2.5, IG.upper(), weight=600, fill=NAVY, ls=0.3)
    l, lw, lh = logo("c-icone-reducao-marinho", 72, 31, 12)
    write("08-cartao-pos-entrega-verso-90x50mm.svg", doc(90, 50, o + l, "mm", "Cartão verso"))

    # 9 · Assinatura de e-mail (HTML; a imagem precisa estar hospedada em um link público)
    write("09-assinatura-email.html", f'''<!-- Assinatura de e-mail Nobre Living.
Troque SEU NOME e o endereço da imagem (src) por um link público do arquivo
png/@2x/nobre-living-c-icone-marinho@2x.png (Google Drive público, site etc.). -->
<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;color:{GRAF};border-top:1px solid {GOLD};padding-top:12px">
  <tr>
    <td style="padding:12px 16px 0 0;vertical-align:middle">
      <img src="https://SEU-LINK/nobre-living-c-icone-marinho@2x.png" width="64" height="64" alt="Nobre Living" style="display:block">
    </td>
    <td style="padding-top:12px;vertical-align:middle;font-size:13px;line-height:1.55">
      <div style="font-weight:bold;color:{NAVY}">SEU NOME</div>
      <div style="font-size:10px;letter-spacing:1.4px;color:{NAVY}">NOBRE LIVING · MÓVEIS E ESTOFADOS · BRASÍLIA</div>
      <div style="color:{MUTED}">{TEL} · <a href="mailto:{MAIL}" style="color:{MUTED};text-decoration:none">{MAIL}</a> · <a href="https://instagram.com/nobreliving" style="color:{MUTED};text-decoration:none">{IG}</a></div>
    </td>
  </tr>
</table>
''')
    print("modelos ok", len(os.listdir(OUT)))

if __name__ == "__main__":
    main()
