import requests
from bs4 import BeautifulSoup

url = "https://sp.senai.br/unidade/santanadeparnaiba/"
response = requests.get(url)
response.raise_for_status()  # Garante que a requisição teve sucesso

soup = BeautifulSoup(response.text, "html.parser")
h1 = soup.find("h1")
if h1:
    print("A melhor do mundo")
    print( h1.get_text(strip=True))
else:
    print("Nenhuma tag <h1> encontrada.")
         
