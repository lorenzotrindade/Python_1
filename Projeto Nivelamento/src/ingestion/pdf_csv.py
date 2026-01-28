import requests
import pdfplumber
import zipfile
import csv


# download to pdf and save in data/raw/
def download_pdf(url, output_path):
    response = requests.get(url)
    with open(output_path, "wb") as f:
        f.write(response.content)



# open pdf save, after extrac table, if table true?, return dados
def extract_table(pdf_path):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabela = page.extract_table()
            if tabela:
                dados.extend(tabela)
    return dados




#sava dados to extract in archive CSV   
def save_csv(data, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)




#COMPACT TO zip
def zip_csv(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, arcname="teste_lorenzo.csv")





def run():
    url = "https://www.ans.gov.br/images/stories/Legislacao/rn/Anexo_I_Rol_2021RN_465.2021_RN654.2025L.pdf"
    pdf_path = "data/raw/anexo1.pdf"
    csv_path = "src/ingestion/csv_reader.py"
    zip_path = "data/processed/teste_lorenzo.zip"

    download_pdf(url, pdf_path)
    dados = extract_table(pdf_path)
    save_csv(dados, csv_path)
    zip_csv(csv_path, zip_path)


if __name__ == "__main__":
    run()