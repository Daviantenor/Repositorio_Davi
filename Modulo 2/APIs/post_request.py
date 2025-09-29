import requests

url = "https://jsonplaceholder.typicode.com/posts"

novo_usuario = {
"Nome": "Neymar Junior",
"Idade": 27,
"Altura": "1.76"
}

response = requests.post(url, json=novo_usuario)

if response.status_code == 201:
    print("Criação de novo usuário bem sucedida.")
    print(response.json()) 
else:
    print(f" Algo deu errado,tente novamente: {response.status_code}")
