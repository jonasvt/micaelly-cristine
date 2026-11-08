# Sistema de design

Princípio: **o trabalho é o protagonista, e o site tem a cara da Mica.** Pouco texto, números grandes, imagens grandes. A identidade vem da ilustração dela (cabelo ruivo, óculos, prendedores de estrela, casaco creme, fundo rosa) e não de um template.

O Jonas rejeitou o "visual padrão de site feito por IA": Geist/Inter, rótulos em fonte mono e caixa-alta, palavra em itálico serifado no título, monograma "MC". **Não voltar com isso.**

## Cores (tokens em `src/static/css/site.css`, bloco `:root`)

| Token | Página principal | Página de vídeo (`.theme-dark`) | Uso |
|---|---|---|---|
| `--bg` | `#fbf6ef` creme | `#121010` | fundo |
| `--surface` | `#fffdf9` | `#1c1817` | cartões |
| `--ink` | `#211a17` marrom-tinta (contorno da ilustração) | `#f7efe6` | texto |
| `--ink-2` / `--ink-3` | `#5b514b` / `#74695f` | `#c4b8ad` / `#998d82` | secundário (contraste AA) |
| `--accent` | `#b33d0e` cobre (cabelo) | `#f08a52` | destaque: ✦, fim do título, e-mail |
| `--blush` | `#f8d9dd` rosa (fundo da ilustração) | `#3a2328` | painel do retrato |

## Tipografia (self-hosted em `src/static/fonts/`)
- **Fraunces** (variável) — títulos e números. Eixos: `SOFT 100` (cantos macios) e `WONK 1` (letras levemente tortas) nos títulos grandes; `WONK 0` nos títulos de projeto. Peso ~560.
- **Figtree** — todo o resto (texto, botões, chips, rótulos). Rótulos em peso 600, caixa normal.
- Monoespaçada do sistema **só** dentro do terminal do projeto Kāsper.

## Marcas pessoais
- **✦** (estrelinha dos prendedores de cabelo) antes do nome no topo, nos rótulos de seção e no favicon.
- **Retrato ilustrado** no topo da página principal, em painel rosa levemente girado (−2°).
- Sem logo, sem monograma.

## Forma e espaço
- Raio 8 / 14 / 22 / 28 px; botões e chips em pílula.
- Largura máxima 1160 px; margem lateral `clamp(20px, 5vw, 48px)`; espaço entre seções `clamp(88px, 10vw, 152px)`.

## Componentes
- **Números (proof)**: valor grande em Fraunces + rótulo curto.
- **Case**: visual (citação, terminal ou pipeline) + título de 1 linha + chips + links.
- **Experiência**: data · cargo · empresa · uma linha de resultado.
- **Player**: pôster + botão "Assistir"; o vídeo só baixa ao clicar; um toca por vez. Página de vídeo abre com o nome dela em Fraunces bem grande e um **leque animado** de 5 pôsteres (`.fan`, lógica em `site.js → initFan`): as cartas são "distribuídas" ao abrir, flutuam de leve, giram uma posição a cada 3,2 s e a carta do centro toca uma prévia muda de 4 s (`<slug>-preview.mp4`). Pausa com o mouse em cima, fora da tela ou com a aba oculta; parado com `prefers-reduced-motion`; sem prévias com "economia de dados". O comercial vem depois dos dramas.
- **Parede de ferramentas**: categorias com nomes em pílulas.

## Movimento
- Fade + 14 px ao entrar na tela (`.reveal`); topo com animação CSS curta (`.intro`).
- Tudo desligado com `prefers-reduced-motion`. Autoplay mudo só no comercial (seção Cinematográfico), quando visível e sem "economia de dados".

## Não fazer
Gradientes coloridos, glassmorphism, 3D, cards em excesso, parágrafos longos, mais de uma cor de destaque, monograma, rótulos em mono/caixa-alta, Geist/Inter/Instrument Serif.
