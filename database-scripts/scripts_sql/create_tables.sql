-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS ans_data;
USE ans_data;

-- Criação da tabela de Operadoras
DROP TABLE IF EXISTS operadoras;
CREATE TABLE operadoras (
    id_operadora INT PRIMARY KEY AUTO_INCREMENT,
    Registro_ANS VARCHAR(50),
    CNPJ VARCHAR(20),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(100),
    Logradouro VARCHAR(255),
    Numero VARCHAR(20),
    Complemento VARCHAR(100),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP VARCHAR(15),
    DDD VARCHAR(5),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao INT,
    Data_Registro_ANS DATE
) ENGINE=InnoDB;

-- Criação da tabela de Demonstrações Contábeis
DROP TABLE IF EXISTS demonstracoes_contabeis;
CREATE TABLE demonstracoes_contabeis (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Registro_ANS VARCHAR(50),
    periodo DATE,
    CD_CONTA_CONTABIL VARCHAR(50),
    indicador VARCHAR(255),
    VL_SALDO_INICIAL DECIMAL(15,2),
    VL_SALDO_FINAL DECIMAL(15,2)
) ENGINE=InnoDB;
