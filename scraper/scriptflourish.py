import pandas as pd
from bs4 import BeautifulSoup
import os
import re
import json
import requests
from tqdm import tqdm

diretorio = 'public'  # COLOQUE AQUI O DIRETÓRIO DOS ARQUIVOS HTML
arquivos_html = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith('.html')]
caminho_saida_excel = os.path.join(diretorio, 'urls.xlsx')  

data = []  

for arquivo in tqdm(arquivos_html, desc="Processando arquivos", unit="arquivo"):
    caminho_arquivo = os.path.join(diretorio, arquivo)

    with open(caminho_arquivo, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    iframes = soup.find_all('iframe')

    ordem = 1  
    for iframe in iframes:
        url = iframe.get('src')

        if url and 'visualisation' in url:
            response = requests.get(url)
            iframe_html = response.text

            settings_match = re.search(r'var _Flourish_settings = ({.*?});', iframe_html, re.DOTALL)

            if settings_match:
                settings_data = json.loads(settings_match.group(1))
                layout_title = settings_data.get('layout.title')
                layout_source = settings_data.get('layout.source_name')
            else:
                layout_title = "Título não encontrado"
                layout_source = "Fonte não encontrada"

            data.append([arquivo, url, layout_title, 'Flourish', layout_source, ordem])
            ordem += 1 
        elif url and 'powerbi' in url:
            data.append([arquivo, url, 'None', 'Power BI', 'Fonte não aplicável', ordem])
            ordem += 1  
        else:
            data.append([arquivo, url, 'None', 'Desconhecido', 'Fonte não aplicável', ordem])
            ordem += 1  

df = pd.DataFrame(data, columns=['Nome do Arquivo', 'URL', 'Título', 'Tipo', 'Fonte', 'Ordem'])

df.to_excel(caminho_saida_excel, index=False)
print("Arquivo Excel criado com sucesso!") 
