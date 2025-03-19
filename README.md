# Pesquisa de Smartphones com Selenium e BeautifulSoup

Este projeto utiliza Selenium e BeautifulSoup para realizar uma pesquisa no Mercado Livre por smartphones da Samsung, extraindo informações como nome, preço, link do produto, nota de avaliação e total de avaliações. Os dados extraídos são salvos em um arquivo Excel para futura consulta.

## Tecnologias Utilizadas

- Python
- Selenium
- BeautifulSoup (bs4)
- Pandas
- WebDriver do Google Chrome

## Instalação e Configuração

Antes de rodar o código, certifique-se de ter instalado os seguintes pacotes:

```sh
pip install selenium beautifulsoup4 pandas openpyxl
```

Também é necessário ter o WebDriver do Google Chrome compatível com a sua versão do navegador. Ele pode ser baixado [aqui](https://chromedriver.chromium.org/downloads) e deve estar no PATH do sistema ou na mesma pasta do script.

## Como Usar

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```
2. Acesse a pasta do projeto:
   ```sh
   cd nome-do-repositorio
   ```
3. Execute o script:
   ```sh
   python pesquisa_smartphones.py
   ```

O script abrirá o site do Mercado Livre, pesquisará por "smartphone samsung" e extrairá os dados, que serão salvos no arquivo `planilha.xlsx`.

## Estrutura do Projeto

```
/
|-- pesquisa_smartphones.py  # Script principal
|-- planilha.xlsx            # Arquivo Excel gerado com os resultados (depois da execução)
|-- README.md                # Documentação do projeto
```

## Exemplo de Saída no Terminal

```
Nome: Samsung Galaxy S23 Ultra
Preço: 5.499,00
Link: https://www.mercadolivre.com.br/samsung-galaxy-s23-ultra
Nota: 4.8
Total de avaliações: 1200
----------------------------------------------------------------------
```
Se você achou este projeto útil, considere dar uma estrela ⭐ no repositório!

