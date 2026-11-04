# Identidade visual · Nobre Living

Etapa atual: **kit final v1.0** em `kit/` (símbolo Portal com pendente e vaso, fonte Prata). Comece por `kit/LEIA-ME.md` e `kit/manual/nobre-living-manual-da-marca.pdf`.

- `refinamento.html`: página da Planta refinada (construção, versões A–E, testes, aplicações).
- `marca/svg/`: versões oficiais em SVG, texto em curvas, nas cores marinho, off-white e grafite.
  `nobre-living-[vertical|horizontal|icone|icone-reducao|assinatura|vertical-assinatura]-[cor].svg`
- `apresentacao.html` e `direcoes/`: rodada anterior com as três direções (Fio, Planta, Vão).
- `referencia/logo-2025-raster.jpg`: logo antigo, só raster.
- `_fonte/`: scripts que geram tudo (`simbolo.py`, `marca.py`, `refinamento.py`, `gerar.py`, `pagina.py`).

Para regenerar (precisa de `fonttools` e das fontes Bodoni Moda opsz 28 e Inter em TTF estático):

```bash
cd identidade-visual/_fonte
python3 marca.py <pasta-das-fontes> ../marca/svg
python3 refinamento.py <pasta-das-fontes> ../refinamento.html <miniatura-do-logo-antigo.jpg>
```

## Kit final

```bash
cd identidade-visual/_fonte
python3 kit_logos.py <pasta-das-fontes> ../kit        # SVGs A–E
node kit_png.js ../kit                                # PNGs, favicon, marca d'água
python3 kit_templates.py ../kit                       # modelos
node kit_previa.js <pasta-das-fontes> ../kit          # prévias dos modelos
python3 kit_manual.py <pasta-das-fontes> ../kit       # manual (HTML) → exportar PDF com o Chromium
```

Fontes usadas: Prata 400 e Inter 300–600 (TTF estático do Google Fonts).
