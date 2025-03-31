import os
import csv
import mysql.connector
from datetime import datetime

def import_csv_to_demonstracoes(conn, csv_file):
    """Importa os dados de um arquivo CSV para a tabela demonstracoes_contabeis e retorna a quantidade de linhas importadas."""
    cursor = conn.cursor()
    print(f"Importando arquivo: {csv_file}")
    linhas_importadas = 0
    batch = []
    batch_size = 1000  # número de linhas por lote

    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        header = next(reader, None)
        if header is None:
            print("Arquivo vazio ou sem cabeçalho.")
            return 0
        for row in reader:
            if len(row) < 6:
                print(f"Linha com colunas insuficientes ignorada: {row}")
                continue

            # Extrai os dados
            data_str = row[0].strip()      # DATA
            reg_ans = row[1].strip()         # REG_ANS
            conta = row[2].strip()           # CD_CONTA_CONTABIL
            descricao = row[3].strip()       # DESCRICAO
            saldo_inicial_str = row[4].strip()  # VL_SALDO_INICIAL
            saldo_final_str = row[5].strip()    # VL_SALDO_FINAL

            # Converter a data para objeto date
            try:
                if "/" in data_str:
                    # Caso a data esteja no formato DD/MM/YYYY
                    periodo = datetime.strptime(data_str, '%d/%m/%Y').date()
                else:
                    # Assume o formato YYYY-MM-DD
                    periodo = datetime.strptime(data_str, '%Y-%m-%d').date()
            except Exception as e:
                print(f"Erro convertendo data '{data_str}' no arquivo {csv_file}: {e}")
                continue

            # Converter valores para float
            try:
                saldo_inicial = float(saldo_inicial_str.replace(',', '.')) if saldo_inicial_str else 0.0
            except Exception as e:
                print(f"Erro convertendo VL_SALDO_INICIAL '{saldo_inicial_str}' no arquivo {csv_file}: {e}")
                saldo_inicial = 0.0

            try:
                saldo_final = float(saldo_final_str.replace(',', '.')) if saldo_final_str else 0.0
            except Exception as e:
                print(f"Erro convertendo VL_SALDO_FINAL '{saldo_final_str}' no arquivo {csv_file}: {e}")
                saldo_final = 0.0

            batch.append((reg_ans, periodo, conta, descricao, saldo_inicial, saldo_final))
            linhas_importadas += 1

            if len(batch) >= batch_size:
                try:
                    sql = """
                    INSERT INTO demonstracoes_contabeis
                    (Registro_ANS, periodo, CD_CONTA_CONTABIL, indicador, VL_SALDO_INICIAL, VL_SALDO_FINAL)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.executemany(sql, batch)
                    conn.commit()
                    batch = []
                except Exception as e:
                    print(f"Erro inserindo lote no arquivo {csv_file}: {e}")
                    batch = []

    # Inserir as linhas restantes
    if batch:
        try:
            sql = """
            INSERT INTO demonstracoes_contabeis
            (Registro_ANS, periodo, CD_CONTA_CONTABIL, indicador, VL_SALDO_INICIAL, VL_SALDO_FINAL)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.executemany(sql, batch)
            conn.commit()
        except Exception as e:
            print(f"Erro inserindo lote final no arquivo {csv_file}: {e}")
    cursor.close()
    print(f"Arquivo {csv_file} importado com sucesso. Linhas importadas: {linhas_importadas}")
    return linhas_importadas

def import_demonstrativos(conn, base_dir, anos):
    """
    Percorre a pasta base_dir/demonstracoes/<ano>/extracted/ e importa todos os arquivos CSV encontrados.
    Retorna um dicionário com o nome de cada arquivo e a contagem de linhas importadas.
    """
    resumo = {}
    for ano in anos:
        extraction_dir = os.path.join(base_dir, "demonstracoes", ano, "extracted")
        if not os.path.exists(extraction_dir):
            print(f"Pasta de extração não encontrada para o ano {ano}: {extraction_dir}")
            continue
        for filename in os.listdir(extraction_dir):
            if filename.lower().endswith(".csv"):
                csv_file = os.path.join(extraction_dir, filename)
                linhas = import_csv_to_demonstracoes(conn, csv_file)
                resumo[csv_file] = linhas
    return resumo

def main():
    # Define a pasta base para os downloads (supondo que "downloads" esteja na pasta "database-scripts")
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")
    
    # Conecta ao MySQL (ajuste usuário, senha, host e banco conforme necessário)
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="Nome de eusuário",
            password="Senha do banco de Dados",  # Substitua pela sua senha
            database="ans_data",   # Aqui é o nome do bando de dados masss Certifique-se de que este é o banco onde a tabela 'demonstracoes_contabeis' existe!!
            allow_local_infile=True
        )
        print("Conexão com o MySQL estabelecida com sucesso.")
    except mysql.connector.Error as err:
        print("Erro na conexão com o MySQL:", err)
        return

    # Define os anos para os quais os demonstrativos foram baixados (ex: 2023 e 2024)
    anos = ["2023", "2024"]
    resumo = import_demonstrativos(conn, base_dir, anos)
    
    conn.close()
    
    # Exibe o resumo das importações
    total_linhas = 0
    print("\nResumo de importação dos arquivos:")
    for arquivo, linhas in resumo.items():
        print(f"Arquivo: {arquivo}\n  Linhas importadas: {linhas}\n")
        total_linhas += linhas
    print(f"Total de linhas importadas de todos os arquivos: {total_linhas}")

if __name__ == "__main__":
    main()
 
