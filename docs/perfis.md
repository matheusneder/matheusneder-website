# Perfis em portais

Registro dos perfis mantidos em nome de Matheus Neder fora deste site: o que cada um contém, de onde vem o conteúdo e como atualizar.

**Este arquivo deve ser atualizado sempre que um perfil for criado ou editado em qualquer portal.** Registre a mudança na seção do portal e no [histórico](#histórico).

> **O repositório é público.** Não registre aqui telefone, e-mail pessoal, candidaturas, pretensão salarial, preferências de vaga, visibilidade para recrutadores, empresas bloqueadas, dados de autoidentificação nem senhas. Registre apenas quais seções existem, de onde vem o conteúdo e como atualizar. A pasta `docs/` não é publicada no site (o workflow de deploy copia só os arquivos do site), mas fica visível no GitHub.

## Fonte de verdade e padrão de texto

- O conteúdo profissional vem deste site: [`pt-br/index.html`](../pt-br/index.html) e [`en/index.html`](../en/index.html). Ao mudar o site, revise os perfis abaixo; ao mudar um perfil, verifique se o site também precisa mudar.
- Textos em **terceira pessoa** ("Matheus..."), linguagem simples, humanizada e profissional, como no site.
- Sem travessão (—); use vírgula, dois-pontos ou parênteses.
- Quando o portal tem versões em português e inglês, as duas devem dizer a mesma coisa.

## Resumo

| Portal | Endereço | Idiomas | Última atualização |
| --- | --- | --- | --- |
| LinkedIn | https://www.linkedin.com/in/matheus-neder-66b16a16/ | Português (perfil principal) e inglês (perfil secundário) | 2026-11-24 |
| MyGreenhouse | https://my.greenhouse.io/profile | Inglês | 2026-11-25 |
| Glassdoor | https://www.glassdoor.com.br/member/profile | Português | 2026-11-25 |
| Indeed | https://profile.indeed.com/ | Português | 2026-11-25 |

Glassdoor e Indeed são da mesma empresa e compartilham o perfil: o que é editado em um aparece no outro (veja [Glassdoor e Indeed](#glassdoor-e-indeed)).

## LinkedIn

### O que é mantido

| Seção | Conteúdo | Idiomas | Origem |
| --- | --- | --- | --- |
| Título (headline) | PT: "Especialista em Arquitetura e Engenharia de Software"; EN: "Software Engineering and Architecture Specialist" | PT e EN | Mantido como estava (a ordem em PT difere do site) |
| Sobre | Apresentação, trajetória, decisões de arquitetura, principais áreas e tecnologias. Sem parágrafo específico sobre a TOTVS | PT e EN | Hero, "Sobre" e "Principais áreas" do site |
| Experiência | 11 cargos, do Editor de Vídeo (2001) à TOTVS (atual). Os 5 principais usam os textos do site, com uma linha de tecnologias; os antigos foram reescritos em 3ª pessoa preservando os fatos | PT e EN | Seção "Experiência" do site e textos anteriores do LinkedIn |
| Projetos | 3 antigos da webAula + Kubernetes/Fluentd (jan/2020), documentação do Kubernetes (set/2018), Prism (mai/2017) e palestra Docker e Kubernetes (2018), com link do GitHub na descrição | Só PT (o LinkedIn não traduz esta seção) | Seção "Projetos" do site; datas dos PRs vindas do GitHub |
| Reconhecimentos e prêmios | Destaque Acadêmico (2008 e 2011) e ACM ICPC, Fase Final Brasileira (2009, sem mês: o LinkedIn exibe "jan. de 2009") | Só PT | Seção "Formação" do site |
| Voluntariado | Teacher, PUC Minas, 2013 até hoje, causa Educação | Texto em inglês, também no perfil principal (o LinkedIn não traduz esta seção) | Fonte da seção "Voluntariado" do site |
| Formação, licenças, cursos, competências, idiomas, recomendações | Não alterados | | |

Cargos em "Experiência" com só o ano (sem mês): webAula, CONAB, PUC Minas (pesquisa), AHMG / Hospital Vila da Serra, Programador e Sysadmin (autônomo) e Editor de Vídeo.

### Como atualizar

1. Abra o perfil no Chrome com a sessão do titular. As edições são feitas pelos formulários do próprio LinkedIn.
2. **Antes de salvar qualquer formulário, confirme que "Notificar a rede" está desativado.**
3. Versão em inglês: abra o formulário com `?language=en&country=US`, por exemplo `.../edit/forms/summary/new/?language=en&country=US` (Sobre) ou `.../edit/forms/position/<id>/?language=en&country=US` (cargo). Só título, Sobre e cargos têm versão em inglês; projetos, prêmios e as demais seções não.
4. Cuidados conhecidos:
   - **Cargos com só o ano:** ao salvar o formulário (em PT ou EN), o LinkedIn preenche o mês com o mês atual. Depois de salvar, reabra o cargo no formulário em português, volte "Mês de início" e "Mês de término" para "Month" e salve de novo.
   - **Cargo novo:** o formulário vem com "Trabalho aqui atualmente" marcado e, no fim, "Atualizar título do perfil" apontando para o novo cargo. Desmarque o primeiro se o cargo não for atual, não marque "Encerrar cargo atual" e mantenha o título atual.
   - **Formulários em inglês:** a digitação às vezes perde caracteres. Confira o texto salvo.
5. Confira o resultado em `/details/experience/` (PT) e `/details/experience/?locale=en-US` (EN).

### Divergências conhecidas

- Voluntariado aparece como atual no LinkedIn; o site o descreve no passado.
- O cargo "Undergraduate Research Assistant" (PUC Minas) está em inglês também no perfil em português.
- O título em PT está em ordem diferente do site ("Arquitetura e Engenharia" no LinkedIn, "Engenharia e Arquitetura" no site).

## MyGreenhouse

### O que é mantido

| Seção | Conteúdo | Origem |
| --- | --- | --- |
| About you | Resumo em 3ª pessoa (até 500 caracteres) | Hero e "Sobre" do site |
| Employment | 11 cargos, espelhando a versão em inglês do LinkedIn, com resumo em cada um (exceto CONAB e AHMG, que não têm descrição) | LinkedIn (EN) e site |
| Education | Bachelor's Degree em Computer Engineering (PUC Minas, 2008 a 2017); Lean Six Sigma Yellow Belt (THOTH Consultoria, 2019); Students to Business Program (Microsoft Innovation Center, 2009) | Site e LinkedIn |
| Skills | 25 competências (limite do portal): arquitetura de software e de soluções, microsserviços, sistemas distribuídos, arquitetura orientada a eventos, modernização de legados, DDD, TDD, Apache Kafka, OpenTelemetry, AWS, GCP, Azure, Kubernetes, Terraform, C#, .NET, Java, Go, Python, SQL Server, PostgreSQL, Oracle Database, Linux e IA aplicada à engenharia de software | Seção "Competências" do site |
| Resume | PDF antigo em português, anterior a estas atualizações | Enviado pelo titular |
| Contact info | Nome, telefone e localização (valores não registrados aqui) | Titular |
| Online profiles | LinkedIn, GitHub e este site | Links do site |
| Work preferences | Preenchidas com o titular (valores não registrados aqui) | Titular e LinkedIn |
| Voluntary self-identification | Não preenchida, por decisão do titular | |

Os 7 cargos que só têm o ano no LinkedIn (webAula, CONAB, PUC Minas, AHMG, Programador, Sysadmin e Editor de Vídeo) aparecem de janeiro a dezembro, porque o Greenhouse exige mês. É uma aproximação.

Candidaturas ficam no próprio portal e não são registradas aqui. O MyGreenhouse não permite desistir de uma candidatura: "Mark as inactive" só move a candidatura para a aba de inativas, sem avisar a empresa. Para desistir, é preciso contatar a empresa.

### Como atualizar

1. Abra https://my.greenhouse.io/profile no Chrome com a sessão do titular e use o lápis de cada seção.
2. Cuidados conhecidos:
   - "About you" aceita até 500 caracteres; o resumo de cada cargo, até 10.000.
   - "Skills" aceita no máximo 25 itens.
   - Mês de início e de fim são obrigatórios em cada cargo.
   - Campos de seleção (mês, grau, escola, disciplina, local): digite e pressione Enter. Escola e disciplina aceitam valores que não estão na lista ("Create ...").
3. Recarregue a página e confira cada seção.

## Glassdoor e Indeed

O Glassdoor guarda o cabeçalho do perfil, habilidades, certificações e preferências, mas experiência, formação e resumo vêm do **Currículo Indeed** (perfil do Indeed). Os dois portais sincronizam esses dados: editar em um atualiza o outro. Tudo está em português.

### O que é mantido

| Seção | Onde editar | Conteúdo | Origem |
| --- | --- | --- | --- |
| Perfil (nome, situação, cargo, empresa e local) | Glassdoor, lápis do perfil | "Matheus Neder", trabalhando, cargo e empresa atuais (TOTVS), Belo Horizonte | Site e LinkedIn |
| Resumo | Currículo Indeed | Resumo curto em 3ª pessoa | Hero e "Sobre" do site |
| Experiência profissional | Currículo Indeed | 11 cargos com os textos do LinkedIn em português. Cargos que só têm o ano ficam só com o ano (o mês é opcional). CONAB e AHMG sem descrição | LinkedIn (PT) e site |
| Escolaridade | Currículo Indeed | Graduação em Engenharia da Computação, PUC Minas, 2008 a 2017 | Site |
| Competências | Currículo Indeed (aparece em "Habilidades e idiomas" do Glassdoor) | 27 competências do site, em português | Seção "Competências" do site |
| Idiomas | Currículo Indeed | Português (língua materna) e inglês (avançado) | LinkedIn |
| Certificações | Glassdoor ou Currículo Indeed | Lean Six Sigma Yellow Belt | Site |
| Prêmios | Currículo Indeed | ACM ICPC, Fase Final Brasileira (2009); Destaque Acadêmico (jun/2011 e nov/2008) | Site e LinkedIn |
| Links | Currículo Indeed | Este site, LinkedIn e GitHub | Links do site |
| Preferências de vagas | Glassdoor ("Preferências de vagas") ou Indeed ("Preferências") | Preenchidas com o titular (valores não registrados aqui) | Titular |
| Visibilidade para recrutadores e empresas bloqueadas | Glassdoor ("Busca de vagas") ou Indeed (status do recrutamento) | Definidas pelo titular (valores não registrados aqui) | Titular |
| Telefone, endereço e dados pessoais | Currículo Indeed | Não preenchidos | |
| Currículo em arquivo | Glassdoor ou Indeed | Nenhum enviado | |

O Indeed mostra "3 informações incompletas" no currículo: são o telefone e a descrição de CONAB e AHMG, deixados em branco de propósito.

### Como atualizar

1. Abra o portal no Chrome com a sessão do titular.
   - Glassdoor: menu do perfil, "Currículo e experiência", "Preferências de vagas" ou o lápis do perfil.
   - Indeed: https://profile.indeed.com/, cartão "Currículo Indeed", menu "...", "Editar".
2. Cuidados conhecidos:
   - No aviso de cookies do Indeed, escolha "Recusar tudo".
   - Cargo, empresa, local e escolaridade são campos de autocompletar: digite e escolha a sugestão. Sem sugestão adequada, Escape mantém o texto digitado.
   - Habilidades, certificados e cargos desejados entram pelo botão "Adicionar" (Enter não adiciona). No Indeed, as sugestões de competência vêm em inglês; use o "+" para manter o texto em português.
   - O portal normaliza alguns cargos (por exemplo, "Especialista em Engenharia De Software", com "De" maiúsculo).
   - Antes de deixar o perfil visível para recrutadores, cadastre as empresas que não devem vê-lo em "Empresas bloqueadas". O próprio Glassdoor avisa que não garante o bloqueio.
   - Os formulários não têm opção de notificar contatos.
3. Recarregue "Currículo e experiência" no Glassdoor e o "Currículo Indeed" e confira.

### Divergências conhecidas

- Dois cargos estão traduzidos aqui e não no LinkedIn em português: "Pesquisador de Iniciação Científica" (LinkedIn: "Undergraduate Research Assistant") e "Administrador de Sistemas" (LinkedIn: "Sysadmin").
- "Students to Business Program" (curso) não foi cadastrado.

## Outros perfis ligados ao site

Referenciados pelo site, mas sem edições registradas até agora:

- **GitHub:** https://github.com/matheusneder (repositórios citados na seção "Projetos").
- **Spotify:** perfil de artista Matheus Neder (seção "Música").
- **YouTube:** canal Neder & Gray (seção "Música").

## Histórico

| Data | Portal | Mudança |
| --- | --- | --- |
| 2026-11-24 | LinkedIn | Sobre e Experiência reescritos em 3ª pessoa a partir do site, em PT e EN. Cargo AHMG / Hospital Vila da Serra adicionado; títulos alinhados ao site (webAula, CONAB, Itaú em EN, "Autônomo"). Prêmio ACM ICPC 2009 e 4 projetos adicionados |
| 2026-11-24 | LinkedIn | Removido do Sobre (PT e EN) o parágrafo sobre o componente de SQL da TOTVS |
| 2026-11-25 | MyGreenhouse | Perfil atualizado em inglês: About you, 11 cargos, formação, 25 competências, GitHub e site, país do telefone e localização, preferências de trabalho |
| 2026-11-25 | Glassdoor e Indeed | Perfis preenchidos em português: cabeçalho do perfil, Currículo Indeed (resumo, 11 cargos, formação, 27 competências, idiomas, certificação, prêmios e links), preferências de vagas, visibilidade e empresas bloqueadas definidas pelo titular |
