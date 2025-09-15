peso_do_aluno=str(input("nos diga o seu nome:" ))
altura=float(input("nos diga o sua altura:"))
peso=float(input("nos diga o seu peso:"))
imc = peso / (altura * altura)

if imc <=18.5:

    print(f"abaixo do peso")

elif imc <=24.9:

    print(f"peso normal")

elif imc <=29.9:
    print(f"sobrepeso")

elif imc <=34.9:
    print(f"sobrepeso")

elif imc <=39.9:
    print(f"sobrepeso")
    
else:
    print(f"sobrepeso")
