# Estratégia do portfólio

## Diagnóstico (auditoria de 08/11/2026)

**A. Quem é a Mica profissionalmente.** Cientista de Dados e Engenheira de IA com 4+ anos em dados: hoje coloca aplicações com LLM/RAG em produção (Prysmo); antes, engenharia de dados para um banco com ~8M de cooperados, setor público (SEPLAG-MT), scraping para crédito e back-end em Flask. Veio da economia (UFMT) e tem MBA na USP com artigo publicado.

**B. Competências principais.** Python, SQL, PySpark, Databricks, Airflow, LLMs/RAG, ML clássico (Random Forest), APIs Flask/FastAPI, Docker. Segunda frente: produção de vídeo com IA (Seedream, Photoshop, CapCut).

**C. Projetos mais fortes.** (1) Vídeo com IA: volume real (121 episódios, 40 capas) + comercial fotorrealista; (2) pesquisa publicada com dataset aberto; (3) Kāsper Production Gate (código recente, testado, com análise de custo de LLM); (4) pipeline com Airflow.

**D. Pontos fortes para recrutadores.** Experiência em produção com IA generativa; variedade de domínios (finanças, governo, crédito); formação forte; prova de execução em volume no vídeo.

**E. Pontos fracos.** Muitos empregos curtos e sobrepostos; projetos do GitHub antigos e de estudo; trabalho de vídeo sem métricas públicas; ferramenta de geração de vídeo não comprovada.

**F. Posicionamento.** Principal: **Data Scientist & AI Engineer**. Secundário: **AI Video Creator**, numa página própria. A ponte entre os dois é "IA de verdade, nos dois lados: construindo sistemas e criando com ela".

**G. Arquitetura.** Duas páginas **independentes** (uma não cita nem linka a outra — pedido do Jonas), duas línguas:
- `/` — portfólio principal (EN) · `/pt/` (PT)
- `/ai-video-creator/` — página de vídeo, fora do menu principal, `noindex` · `/pt/ai-video-creator/`

**H. Direção visual.** Minimalista, "bate-olho". Claro e quente na principal; escuro e cinematográfico na de vídeo. Ver `DESIGN.md`.

**I. Seleção para /ai-video-creator.** Ordem definida pelo Jonas: cabeçalho com o nome dela e um leque de pôsteres dos dramas → números → grade com 6 episódios. **O leque do topo e a grade usam séries diferentes** (pedido do Jonas, para não repetir). Leque: The Doomed Consort, Billionaire Hearts and Fireworks, Walking Away From My Alpha's Frozen Regret, Love Tides EP 61, Daddy Lost the Past (só pôster + prévia de 4 s). Grade: America's Favorite Ex-Husband (Hollywood), Chained by Loyalty (leitura de livro), Claiming the Luna (escola), The Shadows Between Us (militar), The Hidden Healer Goddess (fantasia), Studio Diary EP 60 (integração de produto). Evitados: episódios com logos de marcas reais (NHL), cenas sensuais e episódios repetitivos. **Capas removidas** (não foram feitas por ela). Depois o comercial do jogo (seção "Cinematográfico") e uma parede de ferramentas de IA por categoria.

**J. A confirmar.** Ver `FACTS.md → Pendências`.

## Decisões do Jonas (08/11/2026)
- Páginas independentes: a página de dados não fala de vídeo; a de vídeo não fala de dados.
- Sem capas/key art na página de vídeo (não foi ela que fez).
- Parede grande de ferramentas de IA (versatilidade) — ver ressalva em `FACTS.md`.
- Local: só "Brasil".
- Sem monograma "MC". Identidade com personalidade, sem cara de template/IA (ver `DESIGN.md`).

## Regra de conteúdo (pedido direto do Jonas e da Mica)

> "Ela odeia texto demais. Tem que ser puramente vídeo e resultados." — "Qualquer pessoa que bater o olho entende, sem ler demais. Simples, direto, completo, de encher os olhos."

Por isso:
- **Nada de parágrafos explicativos.** Cada projeto = imagem + título de uma linha + chips de tecnologia + botão.
- **Cada experiência = uma linha de resultado.**
- **Números grandes** fazem o trabalho de convencer (4+, ~8M, USP, 121 / 121, 27, 40, 2).
- Os textos longos (loglines, processo, bullets completos) ficam em `docs/_long-copy-*.json` para usar em currículo, propostas e entrevistas.

Referência de estilo: https://minimalio.org/video-portfolio-website-8-minimalist-examples/ (fundo escuro, grade de miniaturas, pouco texto, navegação mínima).

## Revisão como recrutador (feita e aplicada)

**Recrutador 1 — vaga de dados/IA.**
Impressiona: Prysmo com LLM/RAG em produção, ~8M de cooperados, USP + artigo. Dúvida: muitos empregos curtos → mitigado mostrando resultado por linha, sem destacar duração. Em nov/2026 o `projeto-machine-learning-ia` foi refeito com ML de verdade e voltou, junto com o RAG jurídico e o lakehouse no Databricks.

**Recrutador 2 — vaga criativa.**
Impressiona: volume e consistência visual, capas com lettering. Dúvida: "ela criou as histórias?" → o site não afirma roteiro; os textos longos (docs) explicam que é adaptação.

**Recrutador 3 — AI Video Creator.**
Impressiona: abertura com o comercial fotorrealista + 6 episódios de gêneros diferentes, 1 clique para assistir com som. Dúvida: "quais ferramentas de vídeo?" → hoje só mostramos as comprovadas; confirmar a ferramenta de geração (pendência 3).

**O que poderia fazer alguém sair do site:** demora para carregar (resolvido: nenhum vídeo baixa antes do clique, exceto o comercial em loop mudo quando visível) e excesso de texto (resolvido nesta versão).

## Ideias para depois
- Link direto do artigo publicado.
- Currículo em PDF.
- Um reel de 30–45 s juntando os melhores momentos dos episódios.
- Se os vídeos ficarem pesados para o GitHub, hospedar no Vimeo/Cloudflare Stream e trocar o `data-src`.
