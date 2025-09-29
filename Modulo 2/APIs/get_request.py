import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code < 300:
    print("Usuários encontrados com sucesso.")
    print(response.json())
else:
    print(f"Ocorreu um erro,tente novamente")
