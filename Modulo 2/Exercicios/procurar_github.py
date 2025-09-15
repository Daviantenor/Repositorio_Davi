import requests
from bs4 import BeautifulSoup

# URL de um repositório do GitHub (pode trocar para outro repo ou perfil)
url = "https://github.com/python/cpython"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Procura a tag <title> (título principal da página)
title = soup.find("title")
if title:
    print("Título encontrado no GitHub:")
    print(title.get_text(strip=True))
else:
    print("Nenhuma tag <title> encontrada.")
