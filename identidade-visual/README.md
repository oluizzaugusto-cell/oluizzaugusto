# Identidade visual · Nobre Living

Etapa atual: **escolha de direção** (3 propostas).

- `apresentacao.html`: página de apresentação das direções Fio, Planta e Vão.
- `direcoes/<direcao>/`: SVGs de cada direção (ícone, ícone de redução, vertical, horizontal, assinatura), em marinho e off-white. Texto em curvas.
- `_fonte/gerar.py` e `_fonte/pagina.py`: scripts que geram os SVGs e a página.

Para regenerar (precisa de `fonttools` e das fontes Bodoni Moda opsz 28 / Inter em TTF estático):

```bash
cd identidade-visual/_fonte
python3 gerar.py <pasta-das-fontes> ../direcoes
python3 pagina.py <pasta-das-fontes> ../apresentacao.html
```
