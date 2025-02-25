# Web Scraping utilizando Selenium e Beautifulsoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
from urllib.parse import urlparse, urlunparse
import pandas as pd

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options=chrome_options)

navegador.get('https://www.mercadolivre.com.br')

sleep(3)

pesquisa = navegador.find_element(By.ID,'cb1-edit')
pesquisa.send_keys('smartphone samsung')
pesquisa.send_keys(Keys.ENTER)

sleep(3)

html = navegador.page_source

extrair_produtos = BeautifulSoup(html, 'html.parser')

dados_smartphones = []

produtos = extrair_produtos.find_all('li', class_='ui-search-layout__item shops__layout-item')

# extrair informações dos protudos
for produto in produtos:
    
    nome = produto.find('a', class_='poly-component__title')
    if nome:
        nome = nome.text.strip()
    else:
        nome = "Nome não encontrado"
        
     
    preco = produto.find('span', class_='andes-money-amount')
    if preco:
        preco = preco.text.strip()
        
        # Limpa o preço (remove "R$", substitui a "," por "." e converte em número flutuante)
        preco_limpo = preco.replace("R$", "").replace(".", "")
        # preco_numerico = float(preco_limpo)
        
    else:
        preco = "Preço não encontrado"
        
    
    link = produto.find('a', class_='poly-component__title')
    if link:
        link = link['href']
    else:
        link = "Link não encontrado"
        
        
    nota_avaliacao = produto.find('span', class_='poly-reviews__rating')
    if nota_avaliacao:
        nota_avaliacao = nota_avaliacao.text.strip()
    else:
        nota_avaliacao = "Produto não avaliado"
        
        
    quantidade_avaliacao = produto.find('span', class_='poly-reviews__total')
    if quantidade_avaliacao:
        quantidade_avaliacao = quantidade_avaliacao.text.strip()
        
         # Remover os parenteses e converter a string em número inteiro
        limpar_avaliacao = quantidade_avaliacao.replace("(", "").replace(")", "")
        converter_avaliacao = int(limpar_avaliacao)
        
    else: 
        quantidade_avaliacao = "Sem avaliações"
        
        
    parsed_url = urlparse(link)
    limpar_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
        
    print(f"Nome: {nome}")
    print(f"Preço: {preco_limpo}")
    print(f"Link: {limpar_url}")
    print(f"Nota: {nota_avaliacao}")
    print(f'Total de avaliações: {converter_avaliacao}')
    print("_" * 70)
    
    dados_smartphones.append([nome, preco_limpo, limpar_url, nota_avaliacao, converter_avaliacao]) # formando a lista
    

df = pd.DataFrame(dados_smartphones, columns=['Nome', 'Preço', 'Link', 'Nota', 'Total de avaliações'])
df.to_excel("planilha.xlsx", index=False)

# print(extrair_dados.prettify()) # organizar o código HTML no terminal
navegador.quit()

