import requests
# ID do usuário que será atualizado
user_id = 100 # Coloque o ID do usuário que você quer atualizar



# Dados do usuário atualizado
usuario_atualizado = {
"Nome": "Neymar Junior",
"Idade": 27, # Atualizando a idade
"Profissão":"Craque do Fut" # Atualizando o curso
}
# Fazendo a requisição PUT para atualizar o usuário
url = f"https://jsonplaceholder.typicode.com/posts/{user_id}"
response = requests.put(url, json=usuario_atualizado)
# Verificando se deu certo
if response.status_code == 200:
    print("Usuário atualizado com sucesso!")
    print(response.json()) # Mostra os dados do usuário atualizado
else:
    print(f"Ops! Algo deu errado. Status: {response.status_code}")
