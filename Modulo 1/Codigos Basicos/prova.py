nome = input("nos diga seu nome: ")
nota1=float(input("nos diga sua primeira nota: "))
nota2=float(input("nos diga sua segunda nota: "))
nota3=float(input("nos diga sua terceira nota: "))
media=(nota1 + nota2 + nota3) / 3
 
if media >=7:
     print(f"{nome} parabéns você passou , continue assim.😄😄 ")

else:
    print(f"{nome} reprovado , sinto muito amigão.😭")
