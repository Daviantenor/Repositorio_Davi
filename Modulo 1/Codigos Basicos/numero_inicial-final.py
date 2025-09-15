nome=input("nos diga o seu nome: ")
numero_escolhido=int(input("escolha um numero: "))
numero_inicial=int(input("começe com 1 ,por favor: " ))
numero_final=int(input("termine com o numero escolhido: " ))



for i in range(numero_inicial, numero_final+1):
    print(f"{numero_inicial}+{i}={numero_escolhido}")
    
