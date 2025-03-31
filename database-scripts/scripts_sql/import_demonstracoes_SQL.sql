-- Importa os dados do arquivo CSV de demonstrativos para a tabela "demonstracoes_contabeis"
LOAD DATA LOCAL INFILE 'C:/caminho/para/demonstrativos.csv'
-- Substitua pelo caminho real do arquivo CSV de demonstrativos

INTO TABLE demonstracoes_contabeis  
-- Tabela onde os dados serão inseridos

CHARACTER SET utf8mb4  
-- Define a codificação do arquivo

FIELDS TERMINATED BY ';'  
-- Define que os campos são separados por ponto-e-vírgula

OPTIONALLY ENCLOSED BY '"'  
-- Define que os campos podem estar entre aspas

LINES TERMINATED BY '\n'  
-- Define que cada linha é finalizada com uma quebra de linha

IGNORE 1 LINES  
-- Ignora o cabeçalho do CSV

(
  @DATA,                   -- Coluna 1 do CSV (DATA) capturada em variável para conversão
  Registro_ANS,            -- Coluna 2 do CSV
  CD_CONTA_CONTABIL,       -- Coluna 3 do CSV
  indicador,               -- Coluna 4 do CSV (DESCRICAO)
  VL_SALDO_INICIAL,        -- Coluna 5 do CSV
  VL_SALDO_FINAL           -- Coluna 6 do CSV
)
SET periodo = STR_TO_DATE(@DATA, '%Y-%m-%d');  
-- Converte a data capturada (@DATA) para o formato DATE e a armazena na coluna "periodo"
-- Ajuste a máscara de data conforme necessário