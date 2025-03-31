--Query 1 – Top 10 Operadoras com Maiores Despesas no Último Trimestre (por exemplo, Q4 de 2023)
-- Este script SQL consulta as 10 operadoras com maiores despesas no último trimestre de 2023, filtrando por um indicador específico e agrupando os resultados por operadora.
-- O resultado é ordenado em ordem decrescente de despesas, mostrando o código de registro da operadora, seu nome e o total de despesas.
-- O intervalo de datas é fixo para o ano de 2023, mas pode ser alterado para 2024 conforme necessário.
USE ans_data;

SELECT 
    o.Registro_ANS,                  -- Código de registro da operadora
    o.Razao_Social,                  -- Nome/razão social da operadora
    SUM(d.VL_SALDO_FINAL) AS total_despesas  -- Soma dos valores finais, que representam as despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.Registro_ANS = o.Registro_ANS  -- Une as duas tabelas com base no campo Registro_ANS
WHERE 
    TRIM(d.indicador) = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
    -- Certifique-se de que o valor usado aqui corresponde exatamente ao que existe na tabela
    AND d.periodo BETWEEN '2023-10-01' AND '2023-12-31'
    -- Esse intervalo corresponde ao último trimestre de 2023; ajuste se necessário
GROUP BY 
    o.Registro_ANS, o.Razao_Social
ORDER BY 
    total_despesas DESC
LIMIT 10;


--Query 2 – Top 10 Operadoras com Maiores Despesas no Último Ano (por exemplo, para 2023)
-- Para o ano de 2024, altere o intervalo para '2024-01-01' e '2024-12-31'
USE ans_data;

SELECT 
    o.Registro_ANS,                  -- Código de registro da operadora
    o.Razao_Social,                  -- Nome/razão social da operadora
    SUM(d.VL_SALDO_FINAL) AS total_despesas  -- Soma dos valores finais, que representam as despesas
FROM demonstracoes_contabeis d
JOIN operadoras o 
    ON d.Registro_ANS = o.Registro_ANS  -- Une as tabelas usando Registro_ANS
WHERE 
    TRIM(d.indicador) = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MÉDICO HOSPITALAR'
    -- Filtra para o indicador exato (copie e cole o valor exato da tabela, se necessário)
    AND d.periodo BETWEEN '2023-01-01' AND '2023-12-31'
    -- Intervalo fixo para todo o ano de 2023; para 2024, altere para '2024-01-01' e '2024-12-31'
GROUP BY 
    o.Registro_ANS, o.Razao_Social
ORDER BY 
    total_despesas DESC
LIMIT 10;
