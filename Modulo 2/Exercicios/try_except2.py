try:
    nome = str(input("qual seu nome? "))
    idade = int(input("qual sua idade? "))

    if idade >= 18:
        print("maior de idade")
    else:
        print("menor de idade")

except ValueError:
    print(f"\n Não coloque números com ponto , vírgula ou letra na sua idade,pois ela é um número inteiro. (Exemplo:1,2,3,etc)")
