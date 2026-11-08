# CLAUDE.md — Portfólio da Micaelly Cristine

Leia isto antes de qualquer mudança. Responda ao usuário em **português do Brasil**, de forma simples.

## O projeto
Site pessoal da **Micaelly Cristine** ("Mica"), feito pelo Jonas (parceiro dela). Dois objetivos:
1. Conseguir entrevistas como **Data Scientist / AI Engineer / Data Engineer** (profissão principal).
2. Conseguir trabalhos como **AI Video Creator** (segunda frente) via uma página própria enviada por link.

## Quem é a Mica (resumo — detalhes e fontes em `docs/FACTS.md`)
- Cientista de Dados na **Prysmo** desde jan/2026 (LLMs, RAG, Databricks, Airflow, Flask).
- Antes: Risk3 (Python/scraping), Tech6 Group (engenharia de dados para banco com ~8M de cooperados), SOFTEX, EBAC, Seno, SEPLAG-MT, Frexco. 4+ anos em dados desde jun/2022.
- MBA Data Science & Analytics (USP/Esalq), ADS (UniFCV), Economia (UFMT). Artigo publicado sobre LRF com Random Forest.
- Vídeo com IA: **121 episódios / 27 séries para a AnimePocky** (estúdio de Londres, 2026) + um **comercial de jogo da Steam não anunciado**. As 40 capas da AnimePocky **não são dela** — não mostrar.
- Parede de ferramentas de IA: lista ampla pedida pelo Jonas (versatilidade), não comprovada nos arquivos; a Mica deve revisar.
- Local no site: só **"Brasil"** (nunca a cidade). E-mail público: micaellycristine01@gmail.com. Nunca publicar o telefone.

## Regras de conteúdo (obrigatórias)
1. **Nunca inventar** empresa, cargo, número, cliente, ferramenta, resultado, depoimento. Se não está em `docs/FACTS.md`, pergunte antes. Ao confirmar algo novo, registre lá com a fonte.
2. **Pouquíssimo texto.** A Mica odeia ler demais. Site = vídeo, imagens, números e títulos de uma linha. Nada de parágrafos explicativos, loglines ou "sobre mim" longo. Textos longos ficam em `docs/_long-copy-*.json`.
3. Os episódios da AnimePocky são **adaptações em anime de dramas live-action** (áudio/diálogo originais). Não dizer que ela escreveu as histórias nem que fez as vozes.
4. O nome do jogo do comercial **não aparece** (não anunciado).
5. Não mostrar o repo `projeto-machine-learning-ia` (README promete mais que o código entrega).
7. **As duas páginas são independentes:** a página principal nunca menciona vídeo/IA criativa e a `/ai-video-creator/` nunca menciona o portfólio de dados (nem link, nem texto, nem o nome do topo).
8. **Escrita sem cara de IA:** nada de travessão (— ou –) em texto do site; use ponto, vírgula, dois-pontos ou "·". Datas com hífen simples (2024-2025) ou "Since/Desde 2026". Evitar frases de efeito, trios de palavras ("Built, shipped, published."), trocadilhos e palavras de marketing (seamless, passionate, leverage, cutting-edge, elevate, unlock, journey). Frases curtas e diretas, como uma pessoa escreveria.
6. Inglês é o idioma padrão e o site **sempre abre em inglês** (`/`); português só em `/pt/`, pelo botão PT. Nunca redirecionar pelo idioma do navegador. Toda mudança de texto precisa das duas línguas, com tradução natural.

## Arquitetura
- `build.py` (Python + Jinja2) gera `dist/` a partir de `content/*.json` + `src/templates/*.html` + `src/static/`.
- Páginas: `home` → `/` e `/pt/`; `ai` → `/ai-video-creator/` e `/pt/ai-video-creator/`; `404.html`.
- Links internos são **relativos** (o site pode morar em subpasta, ex. GitHub Pages `/portfolio/`). Use `{{ root }}` para estáticos e `link('home'|'ai')` para páginas.
- Textos bilíngues: `{"en": "...", "pt": "..."}` + filtro `| t` no template. Cuidado: chaves chamadas `items` devem ser lidas como `x["items"]` no Jinja.
- `/ai-video-creator/` fica **fora de qualquer menu e sem link a partir da home**, com `noindex` (`site.json → ai_page_indexable: false`). Só é acessada pelo link enviado diretamente.
- Vídeos: `src/static/media/video/<slug>.mp4` (+ `.webp` pôster). Não baixam até o clique (`data-src`, `preload="none"`). O vídeo de abertura toca mudo em loop só quando visível e sem reduced-motion/save-data.
- Mídia é gerada por `tools/prepare_media.py` a partir de `source-materials/` (zips originais; fora do Git). Requer ffmpeg.
- Favicon e imagens Open Graph: `tools/make_brand_assets.py`.

## Comandos
```bash
pip install -r requirements.txt
python build.py              # gera dist/
python build.py --serve      # gera e serve em http://127.0.0.1:8000
python tools/prepare_media.py [--only videos|covers|images] [--force]
python tools/make_brand_assets.py
```
Pré-visualização no app: `.claude/launch.json` → configuração "portfolio" (porta 8000).

Deploy: push na `main` → GitHub Actions (`.github/workflows/deploy.yml`) → GitHub Pages (Source: GitHub Actions). `site_url` em `content/site.json` deve ser o endereço final.

## Design (detalhes em `docs/DESIGN.md`)
- Principal: creme `#fbf6ef`, tinta `#211a17`, destaque cobre `#b33d0e` (cabelo dela), rosa `#f8d9dd` (fundo da ilustração). Retrato ilustrado no topo.
- Vídeo: escuro `#121010`, destaque `#f08a52`. Ordem fixa: cabeçalho dela (nome grande + leque de pôsteres dos dramas) → números → dramas → comercial cinematográfico → ferramentas → contato. O comercial **não** abre a página. O leque (`hero.fan`) e a grade (`series.items`) nunca repetem a mesma série.
- Fontes self-hosted: **Fraunces** nos títulos (eixos SOFT 100 / WONK 1: macia e um pouco torta) + **Figtree** no texto. Nada de fonte mono em rótulos nem palavra em itálico serifado: é o "visual padrão de IA" que o Jonas rejeitou.
- Marcador ✦ (estrelinha dos prendedores de cabelo da ilustração) no lugar de números de seção. **Sem logo/monograma "MC".**
- Inspiração aprovada pelo Jonas: https://minimalio.org/video-portfolio-website-8-minimalist-examples/
- Proibido: gradientes coloridos, glassmorphism, 3D, excesso de cards, várias cores de destaque, monograma "MC", rótulos em mono/caixa-alta, Geist/Inter/Instrument Serif.

## SEO e acessibilidade (manter)
- `title`, `description`, canonical, `hreflang` EN/PT, Open Graph + Twitter card, JSON-LD `Person` na home, `sitemap.xml`, `robots.txt`.
- HTML semântico, um `h1` por página, `alt` em todas as imagens, skip link, foco visível, alvos de toque ≥ 44px, contraste AA, `prefers-reduced-motion` respeitado.

## Checklist antes de dizer "pronto"
1. `python build.py` sem erro.
2. `python tools/check_site.py` sem problemas (links, âncoras, h1, alt).
3. Ver no navegador em 1366px e 375px (sem rolagem horizontal).
4. Conferir EN e PT.
5. Nenhum fato novo sem fonte em `docs/FACTS.md`.

## Pendências abertas
Ver `docs/FACTS.md → Pendências` (vínculo/permissão AnimePocky, ferramenta de vídeo, revista do artigo, autoria da ilustração, domínio final).
