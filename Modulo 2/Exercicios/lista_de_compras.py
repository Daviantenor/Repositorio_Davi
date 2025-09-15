lista_de_compras = []

opção=7
while opção != 5:
    opção =int(input("O que eu devo comprar no supermercado hoje?: \n1-ver lista \n2-adicionar item á lista \n3-remover o item da lista \n4-limpar lista \n5-Ver a lista mais tarde"))


    if opção == 1:
        print(f"sua lista de compras:\n {lista_de_compras} ")
 

    elif opção == 2:
        lista=input("Fale qual item deseja adicionar á sua compra:")
        lista_de_compras.append(lista)
    elif opção == 3:
        lista=input("Fale qual item voçê deseja  remover:")
        lista_de_compras.remove(lista)
    elif opção == 4:
        print("lista limpada com sucesso.")
        lista_de_compras.clear()
    
    
    else:
        print(f"voçê poderá ver sua lista mais tarde.")
