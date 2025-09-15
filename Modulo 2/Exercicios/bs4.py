import requests
from bs4 import BeautifulSoup

url = "https://github.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Pegando apenas o título principal (<title>)
title_tag = soup.find("title")
if title_tag:
    print(f" {title_tag.get_text().strip()}")
else:
    print("Não foi possível encontrar o título principal.")
