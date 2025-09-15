import requests


url = "https://www.nike.com.br/?srsltid=AfmBOooGo9CCLqlgKjBG1FOmHg8vMVzy74nBrX9Lmw4Kg4QgaIJzfv_B"
resposta = requests.get(url)
print(resposta.status_code)
