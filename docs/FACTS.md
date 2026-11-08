# Fatos verificados e pendências

Tudo que aparece no site precisa estar nesta lista, com a fonte. Se não está aqui, **não entra no site**.
Auditoria feita em 08/11/2026.

## Fontes consultadas

| Fonte | Onde | Observação |
|---|---|---|
| LinkedIn (PDF exportado, nov/2026) | `source-materials/profile/linkedin-profile-2026-11.pdf` | Fonte principal de experiência, formação, certificações. O LinkedIn público exige login. |
| GitHub | https://github.com/Micaelly2222 | 17 repositórios públicos; READMEs lidos. |
| Portfólio antigo | https://micaelly2222.github.io/portfolio/ | HTML simples (2023), projetos de estudo. |
| Projeto "vagas-da-mica" | `C:\Users\Jonas\Downloads\JonasdaFonseca\localizador-de-vagas` | Ferramenta pessoal de busca de vagas feita pelo Jonas. Mostra o que ela procura: Python, backend, ciência/engenharia/análise de dados, ML, FastAPI, Django. |
| Vídeos AnimePocky ("Creator 5") | `source-materials/animepocky/Creator 5-*.zip` | 121 MP4 verticais, 27 séries, criados entre 16/04 e 23/05/2026. |
| Capas AnimePocky | `source-materials/animepocky/cover-*.zip` | 40 capas + 40 letterings + 4 PSDs (jun–jul/2026). |
| Comercial de jogo | `source-materials/game-ad/Example 02.mp4` | 26 s, 1942×1080, 60 fps, set/2026. |
| Site AnimePocky | http://animepocky.com · https://linktr.ee/animepocky | "Animation studio · London", ANIME POCKY LTD. |

## Fatos usados no site

### Pessoal
- Nome: Micaelly Cristine (completo: Micaelly Cristine de Moura Santos — artigo/Zenodo).
- Local: Brasil. (O LinkedIn diz Cuiabá e região, mas **o site mostra só "Brasil"** — pedido do Jonas, 08/11/2026.)
- E-mail público: micaellycristine01@gmail.com (GitHub e portfólio antigo). **O telefone do PDF não é publicado de propósito.**
- LinkedIn: https://www.linkedin.com/in/micaelly-cristine/ (o GitHub aponta para outra URL antiga: `/in/micaelly-cristine-8a5205200/`).
- Idiomas: português (nativo), inglês profissional (LinkedIn: "Professional Working").
- GitHub marca "hireable: true".

### Experiência (LinkedIn)
| Empresa | Cargo | Período |
|---|---|---|
| Prysmo | Cientista de dados | jan/2026 – atual |
| Risk3 Tecnologia em Análise de Crédito | Desenvolvedora Python | mar–out/2025 |
| Tech6 Group | Engenheira de dados | jun/2024 – ago/2025 (banco com ~8 milhões de cooperados) |
| SOFTEX | Analista de Inovação e Empreendedorismo (bolsista CNPq) | jul–dez/2024 |
| EBAC | Tutora – Cientista de Dados | mai–ago/2024 |
| Seno | Desenvolvedora Back End Júnior | nov/2023 – abr/2024 |
| SEPLAG-MT | Desenvolvedora PL/SQL | jun/2022 – jan/2024 |
| Frexco | Analista/Engenheira de Dados | jun/2022 – jun/2023 |
| Anteriores | Sec. Municipal de Educação (concursada), Agenda Assessoria, Faspec/Uniorka, Núcleo de Pesquisas UFMT | 2018–2022 |

"4+ anos em dados e IA" = desde jun/2022 (Frexco/SEPLAG).

### Formação
- MBA Data Science e Analytics — USP/Esalq (mai/2022 – fev/2024, segundo o LinkedIn; o portfólio antigo dizia dez/2023).
- Análise e Desenvolvimento de Sistemas — UniFCV (mar/2022 – abr/2024; portfólio antigo: jun/2024).
- Ciências Econômicas — UFMT (2016–2020).
- Certificações (LinkedIn, sem emissor informado): Programming for Everybody; Python Fundamentos para Análise de Dados; Docker; Scraping com Python; Introdução à Virtualização de Dados – Denodo.

### Pesquisa
- Artigo: "Previsão do Cumprimento da Lei de Responsabilidade Fiscal por Municípios do Mato Grosso utilizando Random Forest" (LinkedIn → Publications; README do repo `tcc_data_science`).
- Dataset no Zenodo: https://doi.org/10.5281/zenodo.8159329
- Dados IBGE + TCE-MT, 2017–2022 (README).

### Projetos do GitHub em destaque
- `kasper-production-gate` (out/2026): exercício técnico para uma agência; 30 briefings → 19 PASS / 11 BLOCKED; 22 testes; sem custo de LLM (README e NOTES.md do repo).
- `extracao_e_analise_de_dados_do_youtube`: API do YouTube + Pandas + DAG do Airflow diária às 01:30 + SQL de KPIs.
- `tcc_data_science`, `sistema_gerenciamento_python_flask`, `API_gestao_empresa`, `estudos_orm_index`, `contador_tags`, `calculadora_python_azure_functions`.
- **Fora do site de propósito:** `projeto-machine-learning-ia` — o README fala em ML, mas o código classifica por palavras-chave. Mostrar isso a um recrutador técnico seria arriscado.

### Vídeo com IA
- 121 episódios, 27 séries, formato 9:16 (720×1280, alguns 1080×1920 60 fps). Contagem feita nos arquivos.
- 40 capas com lettering existem nos arquivos, mas **não foram feitas pela Mica** (Jonas, 08/11/2026). **Não mostrar capas nem citar key art/lettering.**
- **Ferramentas encontradas nos metadados** (atenção: Seedream e Photoshop vieram das capas, que não são dela; o CapCut veio dos vídeos):
  - **Seedream 4.0** (ByteDance, via BytePlus ModelArk): Content Credentials (C2PA) dentro dos PSDs das capas.
  - **Adobe Photoshop 25.0 (Mac)**: XMP dos PSDs e dos PNGs de lettering.
  - **CapCut**: assinatura de exportação (`te_is_reencode`, `Hw=1`) nos MP4 em 1080p60 e no comercial do jogo.
- Pelas transcrições (Whisper), o áudio dos episódios é de dramas live-action originais (inclui entrevistas de bastidores de atores). Ou seja: o trabalho é **adaptar episódios live-action para anime com IA**, mantendo diálogo e tempo originais. Ela **não** fez roteiro nem voz.
- Comercial: "comercial de um jogo da Steam não anunciado" — informação do Jonas (08/11/2026). O nome do jogo fica fora.

### Lista de ferramentas de IA no site
A parede de ferramentas da página de vídeo (`content/ai-video.json → toolkit.groups`) foi pedida pelo Jonas em 08/11/2026: "pode colocar todas as ferramentas de IA possíveis, pra mostrar versatilidade". **Não é comprovada pelos arquivos.** A Mica deve revisar e tirar qualquer ferramenta que nunca usou, porque recrutadores perguntam sobre elas em entrevista.

## ⚠️ Pendências para confirmar com a Mica

1. **Vínculo com a AnimePocky** (freela, contrato, CLT?) e período exato. Não está no LinkedIn.
2. **Permissão para mostrar** os episódios, capas e o comercial publicamente (NDA?). Se houver restrição, deixar a página só para quem tem o link (já está com `noindex`) ou trocar os vídeos.
3. **Revisar a parede de ferramentas** (`content/ai-video.json → toolkit.groups`): manter só o que ela já usou.
4. **Papel exato no comercial do jogo** (o site diz só "16:9 · 1080p60 · 26 s · Fotorrealista").
5. **Revista do artigo**: o README dela diz "RBPO, v.14, 2024"; uma busca encontrou um artigo parecido na RBTI (Fatec Campinas, 2025). O site não cita a revista até confirmar. Ideal: link direto para o artigo.
6. **Ilustração (retrato com o cachorro)**: agora é o destaque do topo da página principal. Quem desenhou? Se for de outra pessoa, dar crédito no rodapé.
7. **"Aberta a oportunidades remotas"**: ela está empregada na Prysmo. Confirmar se quer o selo (`content/site.json → available`).
8. **Domínio final**: hoje `site_url` aponta para `https://micaelly2222.github.io/portfolio/`.
9. **Currículo em PDF**: não há; se ela quiser, adicionar em `src/static/` e um botão no contato.
