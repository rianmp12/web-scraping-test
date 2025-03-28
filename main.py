import os
import requests
from bs4 import BeautifulSoup
import zipfile

# Faz scraping da página, encontra links de PDFs com "anexo" no nome e realiza o download para o diretório especificado
def download_pdfs(url, dir_download):
    os.makedirs(dir_download, exist_ok=True)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    pdf_links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.text.strip().lower()

        if href and href.endswith(".pdf") and ("anexo i" in text or "anexo ii" in text or "anexo" in text):
            if not href.startswith("http"):
                href = "https://www.gov.br" + href
            pdf_links.append(href)

    downloaded_files = []

    for i, pdf_url in enumerate(pdf_links, start=1):
        try:
            pdf_response = requests.get(pdf_url)
            filename = f"attachment_{i}.pdf"
            filepath = os.path.join(dir_download, filename)

            with open(filepath, "wb") as f:
                f.write(pdf_response.content)

            downloaded_files.append(filepath)
            print(f"Downloaded: {filename}")

        except Exception as e:
            print(f"Error downloading {pdf_url}: {e}")

    return downloaded_files

# Adiciona os arquivos em .zip
def compress_files(files, output_zip):
    os.makedirs(os.path.dirname(output_zip), exist_ok=True)

    with zipfile.ZipFile(output_zip, "w") as zipf:
        for file_path in files:
            zipf.write(file_path, arcname=os.path.basename(file_path))
    print(f"Files compressed into: {output_zip}")

if __name__ == "__main__":

    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    dir_download = "./downloads"
    output_dir = "./output"
    zip_filename = os.path.join(output_dir, "compressed_attachments.zip")

    arquivos_baixados = download_pdfs(url, dir_download)

    if arquivos_baixados:
        compress_files(arquivos_baixados, zip_filename)
    else:
        print("No PDF was downloaded.")