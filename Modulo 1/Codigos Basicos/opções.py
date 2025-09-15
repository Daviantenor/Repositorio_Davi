opção=3
while opção!=4:
    opção = int(input("digite uma opção: \n1 - faz um pix \n2 - mostra o extrato\n3 -   para depositar\n4 - sai do sistema"))
    saldo=246
        
  
    



    if opção == 1:
        nome=input("nos diga o seu nome : ")
        nome_da_pessoa = input("para quem voce pretende mandar pix? \n")
        valor = input(f"digite para nós o quanto o(a) {nome_da_pessoa} irá receber \n")
        print(f"{nome_da_pessoa} recebeu {valor} ")
    elif  opção==2:
        nome_da_pessoa = input("nos diga seu nome \n")
        valor=input(f"digite para nós o valor da extração {nome} \n")
        print(f"{nome} estraiu {valor}")
    elif  opção==3:
        nome_da_pessoa = input("nos diga seu nome\n")
        valor=input(f"digite o quanto quer depositar {nome} \n")
        print(f"{nome} depositou {valor}")
    else :
        print(f" voce desconectado(a) ")
