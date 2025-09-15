opçao=2       
while opçao !=3:
        opçao = int(input("digite uma opçao: \n1 -para a conversão de reais para dólares \n2 - Para a conversão de dólares para reais \n3 -para sair")) 
        
        


        
        if opçao == 1:
            

            dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
            cotacao = float(input ("Informe o valor da cotação do dólar: R$ "))
            conversao = dolar*cotacao
            print('A quantidade de dólar convertido em real é: R$',conversao)
        elif opçao == 2:
            
            real = float(input("Informe a quantidade de real para conversão:  RS "))
            cotacao = float(input ("Informe o valor da cotação do real: USS "))
            conversao = real * cotacao
            print('A quantidade do real convertido em dólar é: USS',conversao)
        else:
            print(f"saiu do sistema")
