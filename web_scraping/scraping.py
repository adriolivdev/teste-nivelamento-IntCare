import requests
from bs4 import BeautifulSoup
import os
import zipfile
import re

def download_pdfs():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        # Procura por links que contenham os textos "Anexo I" e "Anexo II"
        links = soup.find_all("a")
        pdf_urls = {}
        for link in links:
            texto = link.get_text(strip=True)
            # Usa regex para identificar os anexos de forma flexível
            if re.search(r'Anexo\s*I', texto, re.IGNORECASE):
                pdf_urls["anexo_I"] = link.get("href")
            if re.search(r'Anexo\s*II', texto, re.IGNORECASE):
                pdf_urls["anexo_II"] = link.get("href")
        
        print("PDF URLs encontrados:", pdf_urls)
        
        # Define o diretório onde o script está (dentro de web_scraping)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Cria a pasta 'pdfs' dentro do diretório do script
        pdfs_folder = os.path.join(script_dir, "pdfs")
        if not os.path.exists(pdfs_folder):
            os.makedirs(pdfs_folder)
            print(f"Pasta '{pdfs_folder}' criada.")
        
        # Baixa os PDFs e salva na pasta 'pdfs'
        for key, pdf_url in pdf_urls.items():
            # Se o link for relativo, completa-o com o domínio
            if not pdf_url.startswith("http"):
                pdf_url = "https://www.gov.br" + pdf_url
            pdf_response = requests.get(pdf_url)
            if pdf_response.status_code == 200:
                file_path = os.path.join(pdfs_folder, f"{key}.pdf")
                with open(file_path, "wb") as f:
                    f.write(pdf_response.content)
                print(f"{key}.pdf baixado com sucesso e salvo em '{file_path}'.")
            else:
                print(f"Erro ao baixar {key}.pdf")
    else:
        print("Erro ao acessar a página.")

def compress_pdfs(zip_filename="anexos.zip"):
    # Define o diretório do script (dentro de web_scraping)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Pasta onde os PDFs estão salvos
    pdfs_folder = os.path.join(script_dir, "pdfs")
    # Cria a pasta 'pdfs_zipados' dentro do diretório do script
    zipped_folder = os.path.join(script_dir, "pdfs_zipados")
    if not os.path.exists(zipped_folder):
        os.makedirs(zipped_folder)
        print(f"Pasta '{zipped_folder}' criada.")
    
    # Lista dos arquivos PDF que serão compactados
    pdf_files = [os.path.join(pdfs_folder, "anexo_I.pdf"),
                 os.path.join(pdfs_folder, "anexo_II.pdf")]
    # Caminho completo para o arquivo ZIP a ser criado na pasta 'pdfs_zipados'
    zip_path = os.path.join(zipped_folder, zip_filename)
    with zipfile.ZipFile(zip_path, "w") as zipf:
        for pdf in pdf_files:
            if os.path.exists(pdf):
                # Adiciona o arquivo ao ZIP usando apenas o nome base
                zipf.write(pdf, os.path.basename(pdf))
                print(f"{pdf} adicionado ao arquivo ZIP.")
            else:
                print(f"{pdf} não encontrado.")
    print(f"Arquivo {zip_path} criado com sucesso.")

if __name__ == "__main__":
    download_pdfs()
    compress_pdfs()
