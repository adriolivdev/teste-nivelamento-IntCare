import os
import csv
import mysql.connector
from datetime import datetime

def import_csv_to_demonstracoes(conn, csv_file):
    """Importa os dados de um arquivo CSV para a tabela operadoras e retorna a quantidade de linhas importadas."""
    cursor = conn.cursor()
    print(f"Importando arquivo: {csv_file}")
    linhas_importadas = 0
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        # Ignora o cabeçalho
        header = next(reader, None)
        if header is None:
            print("Arquivo vazio ou sem cabeçalho.")
            return 0
        for row in reader:
            if len(row) < 20:
                print(f"Linha com colunas insuficientes ignorada: {row}")
                continue

            # Converter valores vazios para None
            row = [None if field == '' else field for field in row]

            # Converter a data (última coluna, índice 19)
            if row[19]:
                try:
                    # Ajuste o formato conforme o CSV. Se o CSV estiver no formato YYYY-MM-DD, mantenha esse; se for DD/MM/YYYY, altere.
                    row[19] = datetime.strptime(row[19], '%Y-%m-%d').date()
                except Exception as e:
                    print(f"Erro convertendo data '{row[19]}' na linha {row}: {e}")
                    continue

            # Converter "Regiao_de_Comercializacao" (índice 18) para inteiro, se aplicável
            if row[18]:
                try:
                    row[18] = int(row[18])
                except Exception as e:
                    print(f"Erro convertendo Regiao_de_Comercializacao '{row[18]}' na linha {row}: {e}")
                    row[18] = None

            sql = """
            INSERT INTO operadoras (
                Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade,
                Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP,
                DDD, Telefone, Fax, Endereco_eletronico, Representante,
                Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            try:
                cursor.execute(sql, row)
                linhas_importadas += 1
            except Exception as e:
                print(f"Erro inserindo linha {row}: {e}")
    conn.commit()
    cursor.close()
    print(f"Arquivo {csv_file} importado com sucesso. Linhas importadas: {linhas_importadas}")
    return linhas_importadas

def import_operadoras(conn, base_dir):
    """
    Percorre a pasta base_dir/operadoras e importa todos os arquivos CSV encontrados para a tabela operadoras.
    Retorna o total de linhas importadas.
    """
    total_linhas = 0
    operadoras_folder = os.path.join(base_dir, "operadoras")
    if os.path.exists(operadoras_folder):
        for filename in os.listdir(operadoras_folder):
            if filename.lower().endswith(".csv"):
                csv_file = os.path.join(operadoras_folder, filename)
                total_linhas += import_csv_to_demonstracoes(conn, csv_file)
    else:
        print(f"Pasta de operadoras não encontrada: {operadoras_folder}")
    return total_linhas

def main():
    # Define a pasta base para os downloads (supondo que a pasta "downloads" esteja em "database-scripts")
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")
    
    # Conectar ao MySQL (ajuste usuário, senha, host e nome do banco conforme necessário)
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="Nome de eusuario",  # Substitua pelo seu nome de usuário
            password="senha",  # Substitua pela sua senha
            database="ans_data",   # Certifique-se que esse é o banco onde a tabela 'operadoras' existe na sua instância do MySQL
            allow_local_infile=True
        )
        print("Conexão com o MySQL estabelecida com sucesso.")
    except mysql.connector.Error as err:
        print("Erro na conexão com o MySQL:", err)
        return

    # Importa os dados da(s) tabela(s) das operadoras
    total_importadas = import_operadoras(conn, base_dir)
    
    conn.close()
    print(f"Importação concluída. Total de linhas importadas para a tabela 'operadoras': {total_importadas}")

if __name__ == '__main__':
    main()
