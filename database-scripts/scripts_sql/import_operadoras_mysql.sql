-- Importa os dados do arquivo CSV de operadoras para a tabela "operadoras"
LOAD DATA LOCAL INFILE 'C:/caminho/para/Relatorio_cadop.csv'  
-- Substitua pelo caminho real local onde o arquivo está armazenado

INTO TABLE operadoras  
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
-- Ignora a primeira linha do CSV (cabeçalho)

(
  Registro_ANS,           -- Coluna 1 do CSV
  CNPJ,                   -- Coluna 2 do CSV
  Razao_Social,           -- Coluna 3 do CSV
  Nome_Fantasia,          -- Coluna 4 do CSV
  Modalidade,             -- Coluna 5 do CSV
  Logradouro,             -- Coluna 6 do CSV
  Numero,                 -- Coluna 7 do CSV
  Complemento,            -- Coluna 8 do CSV
  Bairro,                 -- Coluna 9 do CSV
  Cidade,                 -- Coluna 10 do CSV
  UF,                     -- Coluna 11 do CSV
  CEP,                    -- Coluna 12 do CSV
  DDD,                    -- Coluna 13 do CSV
  Telefone,               -- Coluna 14 do CSV
  Fax,                    -- Coluna 15 do CSV
  Endereco_eletronico,    -- Coluna 16 do CSV
  Representante,          -- Coluna 17 do CSV
  Cargo_Representante,    -- Coluna 18 do CSV
  Regiao_de_Comercializacao,  -- Coluna 19 do CSV
  @Data_Registro_ANS      -- Coluna 20 do CSV (capturada em uma variável para conversão)
)
SET Data_Registro_ANS = STR_TO_DATE(@Data_Registro_ANS, '%Y-%m-%d');  
-- Converte a string da data para o formato DATE (ajuste a máscara se necessário)
