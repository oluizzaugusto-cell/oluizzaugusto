# Identidade visual · Nobre Living

Etapa atual: **estudo 4: variações do Portal** (`estudo-portal.html`). Rodadas anteriores: `estudo-simbolos-autorais.html`, `estudo-fonte-simbolo.html`, `refinamento.html` e `apresentacao.html`.

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
