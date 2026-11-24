# matheusneder.com

Site pessoal e profissional de **Matheus Neder** (Matheus Villela Neder Issa): portfólio e extensão do currículo, em português do Brasil e inglês.

O site é **100% estático**: HTML5 semântico, CSS e JavaScript puro. Não há framework, dependências, build, backend, banco de dados, cookies nem rastreamento.

## Estrutura

```
/
├── index.html            Página principal: escolhe o idioma (com links de fallback sem JS)
├── pt-br/index.html      Versão completa em português (pt-BR)
├── en/index.html         Versão completa em inglês (en)
├── 404.html              Página de erro bilíngue (usa caminhos absolutos)
├── favicon.svg
├── robots.txt
├── sitemap.xml           Com alternates hreflang
└── assets/
    ├── css/main.css      Todo o estilo; tokens de design no topo (variáveis CSS)
    ├── css/psychedelic.css  Camada opcional de efeitos psicodélicos leves (cores e rolagem)
    ├── js/main.js        Melhorias progressivas (tema, idioma, navegação, vídeo)
    ├── fonts/            Inter e Manrope (woff2, subset latin) + licenças OFL
    ├── icons/            icons.svg (sprite) e apple-touch-icon.png
    └── images/           Retrato, imagens da seção de música e imagem Open Graph
```

## Executar localmente

As páginas usam um sprite SVG externo e caminhos que pressupõem um servidor HTTP; abrir os arquivos com `file://` não exibe os ícones. Use qualquer servidor estático na raiz do projeto:

```powershell
python -m http.server 8080
```

Depois, acesse `http://localhost:8080/` (a raiz redireciona para `/pt-br/` ou `/en/`), ou diretamente `http://localhost:8080/pt-br/` e `http://localhost:8080/en/`.

## Publicação

Basta publicar a pasta inteira como site estático, na raiz do domínio. Não há etapa de build.

- **GitHub Pages (configuração atual):** o workflow `.github/workflows/pages.yml` valida o site (`scripts/check_site.py`) em todo push e pull request e, em push na `master`, publica no GitHub Pages. Veja a seção abaixo.
- **Cloudflare Pages / Netlify:** crie o projeto apontando para o repositório, sem comando de build e com diretório de saída `/` (raiz). O `404.html` também é reconhecido automaticamente.
- **Servidor web convencional (Nginx, Apache etc.):** copie os arquivos para o *document root* e configure `404.html` como página de erro (`error_page 404 /404.html;` no Nginx, `ErrorDocument 404 /404.html` no Apache).

O site pressupõe ser servido **na raiz do domínio** (a página 404 usa caminhos absolutos como `/assets/...`). As demais páginas usam caminhos relativos.

### GitHub Pages e domínio próprio (GoDaddy)

**1. Repositório.** Para o endereço `https://matheusneder.github.io` (site de usuário), o repositório precisa se chamar exatamente `matheusneder.github.io` (*Settings → General → Rename*). O remote local precisa ser atualizado depois: `git remote set-url origin https://github.com/matheusneder/matheusneder.github.io.git`.

**2. Fonte de publicação.** Em *Settings → Pages → Build and deployment → Source*, escolha **GitHub Actions**. O primeiro push na `master` (ou *Run workflow*) publica o site.

**3. DNS na GoDaddy** (*Meus produtos → DNS do matheusneder.com*). Remova os registros `A` e `CNAME` de `www` padrões de estacionamento da GoDaddy e crie:

| Tipo | Nome | Valor |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |
| CNAME | `www` | `matheusneder.github.io` |

Confira os IPs na [documentação do GitHub](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) antes de criar. Opcional e recomendado: verifique o domínio em *Settings (da conta) → Pages → Add a domain* (registro TXT) para evitar sequestro de domínio.

**4. Domínio no GitHub.** O arquivo `CNAME` (com `matheusneder.com`) já vai no deploy. Em *Settings → Pages → Custom domain* confirme `matheusneder.com`, aguarde a verificação do DNS e marque **Enforce HTTPS** (o certificado leva alguns minutos). Com o domínio próprio ativo, `matheusneder.github.io` e `www.matheusneder.com` redirecionam para `https://matheusneder.com`.

## Domínio definitivo

O domínio assumido é **`https://matheusneder.com/`** (nome do repositório). Se for outro, substitua `https://matheusneder.com` em todos os arquivos abaixo:

| Arquivo | O que depende do domínio |
| --- | --- |
| `index.html`, `pt-br/index.html`, `en/index.html` | `canonical`, `hreflang`, `og:url`, `og:image` e URLs do JSON-LD |
| `sitemap.xml` | Todas as URLs |
| `robots.txt` | Endereço do sitemap |
| `assets/images/og-image.jpg` | O texto "matheusneder.com" está na imagem (regerar se o domínio mudar) |

Um comando que faz a substituição em todos os arquivos de texto (PowerShell):

```powershell
Get-ChildItem -Recurse -Include *.html,*.xml,*.txt | ForEach-Object { (Get-Content $_ -Raw) -replace 'https://matheusneder\.com', 'https://NOVO-DOMINIO' | Set-Content $_ -NoNewline -Encoding utf8 }
```

## Atualizar o conteúdo

Cada idioma tem seu próprio documento HTML com todo o conteúdo, para que ambos sejam indexados de forma independente. **Toda alteração de conteúdo deve ser feita nos dois arquivos**, `pt-br/index.html` e `en/index.html`, que têm a mesma estrutura e a mesma ordem de seções:

1. Apresentação (hero): nome, perfil profissional, resumo, links para LinkedIn, GitHub e e-mail, e três fatos-chave
2. Sobre / About: inclui o nome completo (Matheus Villela Neder Issa), que também aparece na `meta description`, no rodapé e no JSON-LD (`alternateName`), para associar as buscas pelos dois nomes
3. Experiência / Experience: `<ol class="timeline">`, um `<li class="job">` por cargo; cargos antigos em `.early-career`
4. Competências / Expertise: um `<li class="card">` por área
5. Projetos / Projects: contribuições open source, repositórios, pesquisa e palestras
6. Formação / Education: graduação, prêmios, cursos e idiomas
7. Fora do trabalho / Outside work: música e voluntariado (`.music` e `.volunteer`); seção pessoal, propositalmente discreta

Por decisão editorial, os textos não usam o travessão (—); prefira vírgula, dois-pontos ou parênteses.

Ao alterar conteúdo, revise também:

- `<title>`, `meta description` e `og:*` no `<head>` de cada idioma;
- o bloco JSON-LD (`jobTitle`, `worksFor`, `knowsAbout`, `award`, `sameAs`, `dateModified`);
- `lastmod` em `sitemap.xml`;
- o ano no rodapé.

### Currículo para download

O currículo fornecido contém dados pessoais (estado civil, idade, telefone) e não há uma versão em PDF preparada para publicação, por isso o site não oferece download. Para incluir: coloque o arquivo em `assets/documents/` (por exemplo `matheus-neder-cv-pt.pdf` e `matheus-neder-cv-en.pdf`) e adicione um botão em `.hero-actions` de cada idioma:

```html
<a class="btn btn-ghost" href="../assets/documents/matheus-neder-cv-pt.pdf" download>Baixar currículo (PDF)</a>
```

## Identidade visual

Todos os tokens ficam no início de `assets/css/main.css`, em `:root`:

- **Cores:** `--c-bg`, `--c-surface`, `--c-text`, `--c-muted`, `--c-line`, `--c-accent`, `--c-accent-bg`, `--c-focus`. Cada uma usa `light-dark(claro, escuro)`, então os dois temas ficam lado a lado. A cor de destaque é um verde-petróleo sóbrio (`#1f5f5b` no claro, `#7fc4ba` no escuro). Ao trocar cores, mantenha contraste mínimo de 4,5:1 para texto (WCAG AA).
- **Tipografia:** `--font-sans` (Inter, texto) e `--font-display` (Manrope, nome e títulos); escala em `--fs-*`.
- **Espaçamento e forma:** `--space-*`, `--radius`, `--measure` (largura de leitura), `--container`.

O favicon (`favicon.svg`) e o `apple-touch-icon.png` usam a mesma cor de destaque; a imagem `og-image.jpg` (1200×630) foi gerada a partir do retrato, com o nome em Manrope e o restante do texto em Inter.

### Camada psicodélica (`assets/css/psychedelic.css`)

Um arquivo separado, carregado depois de `main.css` em todas as páginas, acrescenta um toque psicodélico leve, só em CSS (sem JavaScript):

- manchas de cor suaves no fundo, que giram e mudam de tom conforme a rolagem;
- barra de progresso de rolagem com gradiente de arco-íris no topo;
- gradiente iridescente no nome e nos títulos de seção, que desliza com a rolagem;
- anel colorido em volta do retrato, que gira na primeira tela;
- cartões que sobem de leve ao entrar na tela e ganham uma borda iridescente quando estão no meio dela;
- uma leve lavagem de cor na seção de música e sublinhado ondulado nos links ao passar o mouse.

Os efeitos de rolagem usam `animation-timeline: scroll()` / `view()` dentro de `@supports`; navegadores sem suporte ficam com o visual estático. Os tokens `--psy-*` no início do arquivo definem as cores (com `light-dark()`, para os dois temas); as cores de texto do gradiente mantêm contraste mínimo de 4,5:1. Para suavizar, reduza a opacidade das cores `--psy-blob*` ou os ângulos dos `@keyframes`; para desligar tudo, basta remover a linha `<link rel="stylesheet" href="…/psychedelic.css">` das quatro páginas.

Com `prefers-reduced-motion: reduce`, nenhum movimento é aplicado (a barra de progresso some e o resto fica estático, só com as cores). Na impressão o arquivo não tem efeito (tudo fica dentro de `@media screen`), e no modo de alto contraste do Windows (`forced-colors`) as camadas decorativas são removidas.

### Tema claro/escuro

Por padrão o site segue o tema do sistema operacional (`prefers-color-scheme`). O botão no cabeçalho permite escolher manualmente; a escolha é salva em `localStorage` (`theme`) e aplicada antes da renderização por um pequeno script inline no `<head>`, evitando o "piscar" de tema. Sem JavaScript, o botão fica oculto e o tema do sistema é usado.

## Idiomas

- URLs independentes: `/pt-br/` e `/en/`, cada uma com `lang`, `canonical` próprio e `hreflang` recíproco (`pt-BR`, `en` e `x-default` → `/`).
- **Raiz (`/`)**: usa a preferência salva (`localStorage` `lang`); se não houver, a primeira entrada portuguesa ou inglesa de `navigator.languages`; caso contrário, inglês. Sem JavaScript, mostra links para as duas versões.
- **Seletor de idioma** (PT/EN no cabeçalho): são links comuns entre as versões; ao clicar, a escolha é salva e passa a valer na raiz.
- Acessar `/pt-br/` ou `/en/` diretamente **nunca** redireciona.

## Dependências externas

O site renderiza sem nenhum serviço externo. As únicas requisições a terceiros acontecem **por ação do visitante**:

- **YouTube (`youtube-nocookie.com`)**: o vídeo da seção de música só é carregado ao clicar na miniatura (que é local). Sem JavaScript, o clique abre o vídeo no YouTube.
- Links externos (LinkedIn, GitHub, Spotify, YouTube, Whiplash.Net) abrem em nova aba com `rel="noopener"`.

Não há analytics, cookies, fontes de CDN nem hotlinking.

## Origem e licença dos recursos

| Recurso | Origem | Licença / uso |
| --- | --- | --- |
| Retrato (`matheus-neder-portrait*.webp`, base do `og-image.jpg`) | Foto de perfil pública do GitHub de Matheus Neder | Imagem do próprio autor do site |
| `neder-and-gray.webp` | Imagem do canal do YouTube Neder & Gray | Material do próprio projeto musical do autor |
| `neder-and-gray-driving-all-through-the-night.webp` | Capa exibida no perfil de artista no Spotify | Arte do próprio projeto musical do autor; confirme os direitos de uso com o ilustrador, se aplicável |
| `video-theres-only-one-thing-on-my-mind.webp` | Miniatura do vídeo do autor no YouTube | Material do próprio projeto musical do autor |
| Inter | rsms/inter via Fontsource | SIL Open Font License 1.1 (`assets/fonts/OFL-inter.txt`) |
| Manrope | Mikhail Sharanda via Fontsource | SIL Open Font License 1.1 (`assets/fonts/OFL-manrope.txt`) |
| Ícones de marca (GitHub, YouTube, Spotify, LinkedIn) | Simple Icons | CC0 1.0; as marcas pertencem aos respectivos titulares |
| Ícones de interface (e-mail, sol, lua, seta) | Lucide | ISC |
| Favicon, `apple-touch-icon.png`, `og-image.jpg` | Criados para este site | Não se aplica |

## Fontes do conteúdo

- Currículo fornecido pelo autor (fonte principal de todas as informações profissionais).
- GitHub (`github.com/matheusneder`): repositórios e pull requests citados, todos verificados como incorporados aos projetos.
- Whiplash.Net (2013), canal do YouTube e perfil no Spotify: informações da seção de música.
- Perfil do LinkedIn (seção Voluntariado): informações do trabalho voluntário na PUC Minas.

Dados pessoais do currículo que não agregam à apresentação profissional (estado civil, idade) não foram publicados.

## Decisões técnicas

- **Uma página por idioma, sem i18n via JavaScript:** o conteúdo completo está no HTML, o que favorece indexação, compartilhamento e acessibilidade.
- **Single-page com âncoras:** navegação contínua; no celular, o menu vira uma faixa rolável horizontal (sem menu "hambúrguer", que dependeria de JS).
- **Sem JavaScript, nada se perde:** conteúdo, navegação, seletor de idioma e vídeo (como link) funcionam; o JS só adiciona alternância de tema, persistência de idioma, destaque da seção atual e carregamento do vídeo sob demanda.
- **Desempenho:** duas fontes variáveis (~73 KB no total) pré-carregadas, imagens em WebP com dimensões explícitas (sem *layout shift*), `loading="lazy"` fora da primeira dobra, `fetchpriority="high"` no retrato, um CSS e um JS pequenos.
- **Acessibilidade (WCAG 2.2 AA como referência):** HTML semântico, link "pular para o conteúdo", foco visível, rótulos em controles e links de ícone, contraste verificado nos dois temas, suporte a `prefers-reduced-motion`.
- **SEO:** títulos e descrições por idioma, `canonical`, `hreflang` com `x-default`, Open Graph, `robots.txt`, `sitemap.xml` com alternates e JSON-LD (`WebSite`, `ProfilePage`, `Person`).
- **Sem barras de proficiência:** competências agrupadas por área, com as tecnologias usadas na prática.
