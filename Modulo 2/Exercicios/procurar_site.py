import requests

try:
    url="https://sp.senai.br/unidade/santanadeparnaiba/"
    resultado = requests.get(url)
    status = resultado.status_code
    if status ==200:
        print(f"site encontrado status:{status}")
    else:
        print(f"site não encontrado status:{status} ")
except:
    print("ocorreu um erro , tente novamente mais tarde")
