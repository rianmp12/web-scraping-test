# Teste de Web Scraping

Este projeto é um teste de web scraping desenvolvido em **Python** com o objetivo de:

1. Acessar a página da ANS:  
   https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos  
2. Fazer o download dos anexos **Anexo I** e **Anexo II** em formato PDF.
3. Compactar todos os anexos encontrados em um único arquivo `.zip`.

---

## 🛠️ Requisitos

- Python 3.12

## 📁 Estrutura do Projeto

- `downloads/`: pasta onde os PDFs são salvos.
- `output/`: pasta onde o arquivo `.zip` será gerado.
- `requirements.txt`: bibliotecas necessárias com versões fixas.
- `main.py`: script principal com toda a lógica.

---

## ▶️ Como executar

### 1. Clonar o repositório

```bash
https://github.com/rianmp12/web-scraping-test.git
cd web-scraping-test
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate   # No Linux/macOS
venv\Scripts\activate      # No Windows
```

### 3. Instalar as depedências

```bash
pip install -r requirements.txt
```
As versões das bibliotecas estão fixadas no `requeriments.txt` para evitar problemas com atualiazações futuras.

### 4. Executar o script

```bash
python main.py
```

## 📦 Bibliotecas utilizadas

- `requests` - Para fazer requisições HTTP.
- `beautifulsoup4` - Para fazer o parsing e busca de links na página.
- `zipfile` - Para compactar os arquivos PDF.

## ✅ Requisitos atendidos

- Acesso ao site da ANS.
- Download dos Anexos I e II (PDF).
- Compactação dos arquivos em .zip.
