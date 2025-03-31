# Teste de Nivelamento

Este repositório contém a solução completa do Teste de Nivelamento, que envolve:
- **Web Scraping** de documentos oficiais da ANS,
- **Transformação de Dados** (extraindo informações de PDFs e gerando CSV),
- **Scripts de Banco de Dados** para criação e importação de dados em MySQL/PostgreSQL,
- **API Backend** em FastAPI para disponibilizar uma rota de busca de operadoras,
- **Frontend** em Vue.js para consumir a API e exibir os resultados,
- **Coleção do Postman** para demonstrar e testar as rotas da API.

---

## Sumário

- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Descrição de Cada Módulo](#descrição-de-cada-módulo)
- [Desafios e Aprendizados](#desafios-e-aprendizados)
- [Como Executar](#como-executar)
  - [Requisitos](#requisitos)
  - [Configuração e Execução](#configuração-e-execução)
- [Como Contribuir](#como-contribuir)
- [Licença](#licença)

---

## Estrutura do Projeto




### Principais diretórios:

- **api_backend/**: Contém o código em Python com FastAPI. É onde fica a rota `/search` para buscar operadoras no banco.
- **data-transformation/**: Scripts e arquivos relacionados à extração de dados dos PDFs (Rol de Procedimentos) e transformação em CSV.
- **database-scripts/**: Scripts SQL para criar tabelas e importar dados no banco de dados (MySQL ou PostgreSQL).
- **frontend/**: Projeto em Vue.js, responsável por exibir a interface de busca de operadoras e consumir a API.
- **web_scraping/**: Scripts para realizar o download (scraping) dos PDFs e compactá-los conforme solicitado.
- **API de Busca de Operadoras - Teste de Nivelamento.postman_collection.json**: Coleção do Postman para demonstrar e testar os endpoints da API.
- **.gitignore**: Lista de arquivos e pastas ignorados no versionamento.

---

## Tecnologias Utilizadas

1. **Python 3.9+**  
   - **FastAPI**: Framework para construção de APIs rápidas e eficientes.  
   - **MySQL Connector**: Para conexão com o banco de dados MySQL.  
   - **Bibliotecas de Web Scraping** (como `requests`, `BeautifulSoup` ou similar).

2. **Node.js** (versão 14 ou superior)  
   - **Vue.js**: Framework para construção de interfaces reativas e componentizadas.  
   - **Axios**: Para requisições HTTP ao backend.

3. **Banco de Dados**  
   - **MySQL 8** (ou PostgreSQL, dependendo da escolha) para armazenar os dados das operadoras e resultados das demonstrações contábeis.

4. **Ferramentas**  
   - **Postman**: Para testar e documentar os endpoints da API.  
   - **Git/GitHub**: Versionamento de código.

---

## Descrição de Cada Módulo

1. **Web Scraping**  
   - Baixa os Anexos I e II em PDF do site da ANS.  
   - Compacta esses anexos em um único arquivo `.zip`.

2. **Transformação de Dados**  
   - Extrai dados da tabela "Rol de Procedimentos e Eventos em Saúde" do PDF do Anexo I.  
   - Salva os dados em formato CSV e compacta em `Teste_{seu_nome}.zip`.  
   - Substitui abreviações (OD, AMB) pelas descrições completas, conforme a legenda no rodapé do PDF.

3. **Banco de Dados**  
   - Scripts SQL para criar as tabelas necessárias (dados cadastrais das operadoras, demonstrações contábeis, etc.).  
   - Scripts para importar os arquivos CSV baixados do site de Dados Abertos da ANS.  
   - Queries analíticas para descobrir as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre e no último ano.

4. **API Backend (FastAPI)**  
   - Fornece uma rota `/search` para buscar operadoras com base em um termo de busca (`Razao_Social`).  
   - Conecta-se ao banco de dados para retornar até todas as correspondências encontradas.  
   - Utiliza CORS para permitir requisições do frontend Vue.js.

5. **Frontend (Vue.js)**  
   - Interface simples de busca de operadoras.  
   - Um componente principal (`SearchComponent.vue`) faz requisições à rota `/search` da API.  
   - Exibe os resultados de forma amigável ao usuário.

6. **Coleção Postman**  
   - Arquivo `.postman_collection.json` com requisições configuradas para testar o endpoint `/search`.  
   - Inclui scripts de teste para validar status code e estrutura da resposta.

---

## Desafios e Aprendizados

- **Integração de Múltiplas Etapas**: O teste exigiu habilidades de web scraping, extração de dados de PDF, manipulação de CSV, criação de scripts SQL e desenvolvimento de API + frontend.
- **Gerenciamento de Dependências**: Foi necessário configurar ambientes virtuais (Python) e gerenciar pacotes (npm) para cada parte do projeto.
- **Boas Práticas de Segurança**: Remoção de credenciais sensíveis do repositório, uso de variáveis de ambiente e `.gitignore` adequados.
- **Tratamento de Dados em PDF**: A extração da tabela "Rol de Procedimentos" demandou cuidado com a formatação e conversão para CSV.
- **Performance**: Ajustar consultas SQL e garantir que o frontend e backend se comuniquem de forma eficiente.
- **Organização**: Manter cada etapa em seu respectivo diretório ajudou a manter o projeto limpo e modular.

---

## Como Executar

### Requisitos

- **Python 3.9+**  
- **MySQL** (ou PostgreSQL, se preferir) instalado e configurado.
- **Node.js 14+** e **npm** (ou **Yarn**).
- **Ferramentas opcionais**: Postman, Git, etc.

### Configuração e Execução

1. **Clonar o Repositório**  
   ```bash
   git clone https://github.com/adriolivdev/teste-nivelamento-IntCare.git
   cd teste_de_nivelamento
