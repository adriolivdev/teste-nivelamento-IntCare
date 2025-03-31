import os

# Defina o caminho do JDK. Ajuste o caminho conforme a sua instalação.
os.environ["JAVA_HOME"] = r"C:\Program Files\Java\jdk-24"

# Opcional: forçar o Java a usar UTF-8 (pode ajudar em problemas de encoding)
os.environ["JAVA_TOOL_OPTIONS"] = "-Dfile.encoding=UTF-8"

import tabula
import pandas as pd
import zipfile

def extract_table_from_pdf(pdf_path):
    abs_path = os.path.abspath(pdf_path)
    print(f"Tentando abrir o arquivo: {abs_path}")

    if not os.path.exists(abs_path):
        print(f"Arquivo não encontrado: {abs_path}")
        return None

    try:
        dfs = tabula.read_pdf(abs_path, pages="all", multiple_tables=True)
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
        return None

    if dfs:
        print("Tabela(s) encontrada(s).")
        return dfs[0]
    else:
        print("Nenhuma tabela encontrada no PDF.")
        return None

def process_table(df):
    df = df.rename(columns={
        "OD": "Ortopedia e Dermatologia",
        "AMB": "Ambulatorial"
    })
    print("Colunas renomeadas com sucesso.")
    return df

def save_csv_and_compress(df, nome="Seu_Nome"):
    # Define o diretório onde o script está e cria a pasta "resultados" nele
    script_dir = os.path.dirname(os.path.abspath(__file__))
    resultados_folder = os.path.join(script_dir, "resultados")
    if not os.path.exists(resultados_folder):
        os.makedirs(resultados_folder)
        print(f"Pasta '{resultados_folder}' criada.")

    # Define os caminhos completos para os arquivos CSV e ZIP dentro da pasta "resultados"
    csv_filepath = os.path.join(resultados_folder, "dados_procedimentos.csv")
    zip_filepath = os.path.join(resultados_folder, f"Teste_{nome}.zip")

    # Salva o DataFrame como CSV
    df.to_csv(csv_filepath, index=False, encoding="utf-8")
    print(f"Arquivo CSV '{csv_filepath}' criado com sucesso.")
    
    # Cria o arquivo ZIP contendo o CSV
    with zipfile.ZipFile(zip_filepath, "w") as zipf:
        zipf.write(csv_filepath, os.path.basename(csv_filepath))
    print(f"Arquivo ZIP '{zip_filepath}' criado com sucesso.")

if __name__ == "__main__":
    # Caminho absoluto para o PDF; 
    pdf_path = r"C:\Users\adria\OneDrive\Desktop\teste_de_Nivelamento\web_scraping\pdfs\anexo_I.pdf"
    df = extract_table_from_pdf(pdf_path)
    if df is not None:
        df = process_table(df)
        save_csv_and_compress(df, nome="Adriane-Oliveira")  # Pode alterar o nome aqui!!
