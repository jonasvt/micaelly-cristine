# Portfólio — Micaelly Cristine

Site pessoal da Micaelly Cristine: **Cientista de Dados & Engenheira de IA**, com uma página separada de **AI Video Creator**.

- `/` e `/pt/` — portfólio principal (inglês e português)
- `/ai-video-creator/` e `/pt/ai-video-creator/` — vitrine de vídeo com IA. Independente: nenhuma página menciona ou linka a outra, e ela tem `noindex`. É para enviar o link direto a clientes e recrutadores.

Regra de ouro: **vídeo e resultados, quase nenhum texto.** Ver `docs/PORTFOLIO_STRATEGY.md`.

## Stack
HTML + CSS + um pouco de JavaScript, gerados por um script Python (`build.py`) com Jinja2. Sem Node, sem framework. Os textos ficam em arquivos JSON (`content/`), em inglês e português lado a lado.

```
content/            textos do site (EN + PT) — é aqui que se edita conteúdo
  site.json         nome, e-mail, links, URL do site, selo "disponível"
  home.json         página principal
  ai-video.json     página AI Video Creator
  ui.json           palavrinhas de interface (menu, botões)
src/templates/      HTML (Jinja2): base, home, ai-video, macros, 404
src/static/         CSS, JS, fontes, favicon, imagens Open Graph e mídia
  media/video/      <slug>.mp4 + <slug>.webp (pôster)
  media/img/        ilustração
tools/
  prepare_media.py      gera vídeos/pôsteres/capas web a partir dos originais
  make_brand_assets.py  gera favicon e imagens de compartilhamento
source-materials/   originais (zips, MP4, PDF do LinkedIn) — NÃO vai para o Git
docs/               estratégia, fatos verificados, design, textos longos
dist/               site gerado (não editar à mão)
```

## Rodar no computador
Precisa de Python 3.10+ (e ffmpeg só para gerar mídia).

```bash
pip install -r requirements.txt
```

```bash
python build.py --serve
```

Abra http://127.0.0.1:8000. Depois de editar algo, pare (Ctrl+C) e rode de novo.

## Publicar (GitHub Pages)
1. Crie um repositório no GitHub (ou use o `portfolio` atual dela) e envie esta pasta (o `.gitignore` já deixa de fora `source-materials/` e `dist/`).
2. No GitHub: **Settings → Pages → Source: GitHub Actions**.
3. Cada `git push` na branch `main` roda `.github/workflows/deploy.yml`, que gera o site e publica.
4. Ajuste `site_url` em `content/site.json` para o endereço final (ex.: `https://micaelly2222.github.io/portfolio/`). Domínio próprio: preencha `custom_domain` e configure o DNS.

Funciona também em Netlify/Vercel/Cloudflare Pages: comando de build `pip install -r requirements.txt && python build.py`, pasta de saída `dist`.

## Tarefas comuns

**Mudar um texto** → edite o JSON em `content/` (cada texto tem `"en"` e `"pt"`), rode `python build.py`.

**Mudar e-mail, links ou o selo "aberta a oportunidades"** → `content/site.json` (`available: true/false`).

**Adicionar/editar um projeto** → `content/home.json → work.projects`. Cada projeto tem `kicker`, `title` (uma linha!), `stack` (chips) e `links`. O campo `visual` escolhe o desenho: `citation`, `terminal` ou `pipeline` (ver `src/templates/home.html`). Projetos menores vão em `work.more`.

**Adicionar uma experiência** → `content/home.json → experience.items` (uma linha de resultado em `result`).

**Adicionar um vídeo na página AI Video Creator**
1. Coloque o original em `source-materials/` (ex.: `source-materials/novo/meu-video.mp4`).
2. Em `tools/prepare_media.py`, adicione em `VIDEOS`: `slug`, `source`, `kind` (`vertical` ou `landscape`) e `poster_at` (segundo do pôster).
3. Rode `python tools/prepare_media.py` (gera `src/static/media/video/<slug>.mp4`, o pôster `.webp` e, para vídeos verticais, a prévia muda de 4 s `<slug>-preview.mp4`).
4. Em `content/ai-video.json → series.items`, adicione `{"slug", "title", "tag", "alt"}`. As cartas do leque animado do topo ficam em `hero.fan` (5 slugs). O comercial da seção Cinematográfico é `featured.slug`.
5. `python build.py`.

**Trocar a ilustração** (retrato do topo da página principal) → substitua `src/static/media/img/mica-illustration.webp` (proporção 4:5).

**Ferramentas de IA** → `content/ai-video.json → toolkit.groups` (categorias com lista de nomes). Mantenha só ferramentas que a Mica realmente usou.

**Imagem de compartilhamento (WhatsApp/LinkedIn)** → edite `TEXT` em `tools/make_brand_assets.py` e rode o script.

## Documentação
- `CLAUDE.md` — contexto completo para qualquer sessão do Claude Code.
- `CONTENT.md` — todos os textos atuais, bio curta e longa.
- `docs/FACTS.md` — fatos verificados, fontes e **pendências para confirmar**.
- `docs/PORTFOLIO_STRATEGY.md` — posicionamento, decisões e revisão como recrutador.
- `docs/DESIGN.md` — cores, fontes, componentes.
- `docs/_long-copy-*.json` — versões longas dos textos (para currículo e propostas).
