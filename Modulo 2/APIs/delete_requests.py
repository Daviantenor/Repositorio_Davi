import requests

# ID do usuário que será excluído
id_do_usuário = 100 # Coloque o ID do usuário que você quer excluir
# Fazendo a requisição DELETE para excluir o usuário
url = f"https://67efe7452a80b06b8896368d.mockapi.io/Users/{id_do_usuário}"
response = requests.delete(url)
print(f"usuário deletado com sucesso {id_do_usuário}.")
