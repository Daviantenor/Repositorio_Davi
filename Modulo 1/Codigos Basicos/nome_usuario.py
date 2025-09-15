opçao = 6
while opçao!= 3:
    opçao = int(input("digite uma opçao: \n1 -para Fazer login \n2 - Para cadastrar\n3 -para sair")) 

    if opçao==1:
    
        nome_de_usuario1 = input(f"nos diga seu nome de usuario:")
        senha1 = input(f"crie sua senha:")
        print(f"bem-vindo")

    elif opçao==2:
        nome_de_usuario2 = input(f"nos diga seu nome de usuario:")
        senha2 = input(f"crie sua senha:")
        if nome_de_usuario1 == nome_de_usuario2 and senha1 == senha2 :
             print(f"bem-vindo")
        else:
             print("nome de usuario ou senha incorretos")
    else:
  
            print(f"saiu do sistema")    
