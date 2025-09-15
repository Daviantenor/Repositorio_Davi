time = []
opção=7
while opção != 4:
    opção =int(input("o que voce deseja fazer? \n1-ver seus jogadores \n2-adicionar jogador \n3-remover jogador \n4-sair"))


    if opção == 1:
        print(f" Seus jogadores:\n {time}")
 

    elif opção == 2:
        jogador=input("Fale qual(is) jogador voçê deseja adicionar ao seu time:")
        time.append(jogador)
    elif opção == 3:
        jogador=input("Fale qual jogador voçê quer remover:")
        time.remove(jogador)
    else:
        print(f"Você saiu do sistema.")
