import os
import zipfile
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, dest_path):
    """Faz o download de um arquivo a partir da URL e salva no caminho destino."""
    print(f"Baixando: {url}")
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(dest_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
            print(f"Salvo em: {dest_path}")
        else:
            print(f"Erro ao baixar {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")

def get_links_from_directory(url, file_extension):
    """Retorna uma lista de URLs completas dos links que terminam com a extensão desejada."""
    print(f"Acessando {url}")
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return []
    if response.status_code != 200:
        print(f"Erro ao acessar {url}: Status code {response.status_code}")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a in soup.find_all("a"):
        href = a.get("href")
        if href and href.lower().endswith(file_extension.lower()):
            full_url = urljoin(url, href)
            links.append(full_url)
    return links

def download_files_from_directory(base_url, file_extension, download_dir):
    """Faz o download de todos os arquivos com a extensão especificada a partir de uma URL de diretório."""
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Pasta '{download_dir}' criada.")
    
    links = get_links_from_directory(base_url, file_extension)
    print(f"Encontrados {len(links)} arquivos com extensão '{file_extension}' em {base_url}")
    for file_url in links:
        filename = os.path.basename(file_url)
        dest_path = os.path.join(download_dir, filename)
        download_file(file_url, dest_path)

def unzip_all_files_in_folder(zip_folder, extraction_folder):
    """
    Descompacta todos os arquivos ZIP encontrados em 'zip_folder'
    e extrai os conteúdos para 'extraction_folder'.
    """
    if not os.path.exists(extraction_folder):
        os.makedirs(extraction_folder)
        print(f"Pasta de extração '{extraction_folder}' criada.")
    
    for filename in os.listdir(zip_folder):
        if filename.lower().endswith(".zip"):
            zip_path = os.path.join(zip_folder, filename)
            print(f"Descompactando {zip_path} em {extraction_folder}...")
            try:
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extraction_folder)
                print(f"Arquivo {filename} descompactado com sucesso.")
            except Exception as e:
                print(f"Erro ao descompactar {filename}: {e}")

def main():
    # Ajustando a pasta base para downloads: usando o diretório "database-scripts"
    # em vez de "scripts_python". Assumindo que o script está em database-scripts/scripts_python,
    # pegamos o diretório pai.
    base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "downloads")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Pasta base de downloads '{base_dir}' criada.")
    
    ## Parte 1: Demonstrações Contábeis para os anos 2023 e 2024
    demonstracoes_base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/"
    anos = ["2023", "2024"]
    for ano in anos:
        ano_url = urljoin(demonstracoes_base_url, ano + "/")
        # Pasta para salvar os arquivos deste ano
        download_dir_ano = os.path.join(base_dir, "demonstracoes", ano)
        # Baixar arquivos ZIP (que contêm os dados de cada trimestre)
        download_files_from_directory(ano_url, ".zip", download_dir_ano)
        # Descompactar os arquivos ZIP baixados
        extraction_folder = os.path.join(download_dir_ano, "extracted")
        unzip_all_files_in_folder(download_dir_ano, extraction_folder)
    
    ## Parte 2: Operadoras de Plano de Saúde Ativas
    operadoras_url = "https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/"
    download_dir_operadoras = os.path.join(base_dir, "operadoras")
    # Baixar arquivos CSV (geralmente há um arquivo CSV com os dados das operadoras)
    download_files_from_directory(operadoras_url, ".csv", download_dir_operadoras)
    print("Processo concluído.")

if __name__ == "__main__":
    main()
