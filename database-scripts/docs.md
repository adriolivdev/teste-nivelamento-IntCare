# Projeto de Manipulação de Dados – Teste de Nivelamento

## Objetivo

O objetivo deste projeto é automatizar o fluxo de dados a partir dos repositórios públicos da ANS, abrangendo:
- O download de arquivos (ZIP de demonstrações contábeis para os anos 2023 e 2024 e CSV de operadoras ativas).
- A extração dos arquivos ZIP para obter os CSVs.
- A importação dos dados para um banco de dados MySQL, com a criação das tabelas necessárias.
- A análise dos dados importados por meio de queries SQL para identificar, por exemplo, as Top 10 operadoras com maiores despesas em um indicador específico.

## Tecnologias Utilizadas

- **Python:** Utilizado para automatizar o download (com `requests` e `BeautifulSoup`), a extração dos arquivos ZIP (com `zipfile`) e a importação dos CSVs para o MySQL (usando `mysql-connector-python`).
- **MySQL:** Banco de dados utilizado para armazenar os dados.
- **SQL:** Linguagem para criação de tabelas e desenvolvimento das consultas analíticas.
- **Ferramentas de Desenvolvimento:** VS Code (ou outro editor) e MySQL Workbench para edição e validação.

## Estrutura do Projeto

A organização do projeto é a seguinte:
database-scripts/
├── downloads/
│   ├── demonstracoes/
│   │   ├── 2023/
│   │   │   ├── (arquivos ZIP dos trimestres)
│   │   │   └── extracted/
│   │   │       └── (CSV extraídos)
│   │   └── 2024/
│   │       ├── (arquivos ZIP dos trimestres)
│   │       └── extracted/
│   │           └── (CSV extraídos)
│   └── operadoras/
│       └── Relatorio_cadop.csv
|__ imagens_db
├── scripts_python/
│   ├── download_arquivos.py
│   ├── import_demonstracoes.py
│   └── import_operadoras.py
├── scripts_sql/
│   ├── create_tables.sql
│   └── queries_analise.sql
└── README.md





## Etapas do Projeto

1. **Criação do Banco de Dados e Tabelas**  
   - Criação do banco `ans_data` e das tabelas:
     - `operadoras` (dados cadastrais das operadoras).
     - `demonstracoes_contabeis` (dados financeiros dos demonstrativos).
   - Consulte o script `create_tables.sql` para mais detalhes.

2. **Download e Extração dos Arquivos**  
   - Desenvolvi scripts Python que realizam o download dos arquivos ZIP (demonstrações contábeis) e CSV (operadoras) a partir dos repositórios da ANS.
   - Os arquivos ZIP são descompactados, e os CSVs resultantes são organizados em pastas por ano.

3. **Importação dos Dados para o MySQL**  
   - Utilize scripts Python para ler os arquivos CSV, converter os formatos (por exemplo, datas e valores numéricos) e inserir os dados nas tabelas do MySQL.
   - Para otimizar a importação, implementei a inserção em lote (batch insert).

4. **Análise dos Dados**  
   - Desenvolvi queries SQL para analisar os dados, como:
     - Top 10 operadoras com maiores despesas no último trimestre.
     - Top 10 operadoras com maiores despesas no último ano.
   - Os filtros utilizam critérios de data e valores exatos do indicador, com atenção especial à formatação (acentos, espaços, etc.).

## Dificuldades Encontradas

- **Conversão de Datas:**  
  Tive que ajustar o código para lidar com datas em formatos diferentes (por exemplo, `DD/MM/YYYY` vs. `YYYY-MM-DD`).

- **Performance na Importação:**  
  A inserção de dados foi otimizada utilizando a técnica de inserção em lote para reduzir a sobrecarga de transações.

- **Correspondência de Valores:**  
  Foi necessário garantir que os valores dos indicadores, especialmente no filtro das queries, correspondessem exatamente ao que estava armazenado, levando em conta acentos e espaços.

## Resultados e Validação

Após a importação, realizei consultas no banco de dados para confirmar que os dados foram carregados corretamente.  

- **Contagem de Linhas Importadas:**  
  ```sql
  SELECT COUNT(*) FROM demonstracoes_contabeis;
  SELECT COUNT(*) FROM operadoras;

##Conclusão
Nesta etapa, consegui automatizar o processo de ETL (Extract, Transform, Load), que abrange:

Download e extração dos arquivos de dados.

Importação dos dados para o MySQL, com tratamento de formatação e performance otimizada.

Desenvolvimento de queries analíticas para extrair insights dos dados importados.

Este fluxo me permitiu garantir que os dados estejam estruturados e prontos para análises mais avançadas, cumprindo os requisitos do teste de nivelamento.

