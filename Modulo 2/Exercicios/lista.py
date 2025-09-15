lista=["maça","banana","laranja"]

def atualizar_lista():
    antigo = input("item que deseja substituir:")
    if antigo in lista:
        novo = input("Novo item ")
        index = lista.index(antigo)
        lista[index] = novo
        print(f"Lista atualizada",lista)
    else:
        print(f"{antigo} não está na lista.")
atualizar_lista()

o index serve para procurar um valor dentro da váriavel, caso ele não encontre , o sistema avisará que não encontrou.
