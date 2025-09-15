nome = input("Nos diga seu nome:")
Peso = float(input("Nos diga seu peso:"))
altura=float(input("Nos diga sua altura:"))

try:
    imc = Peso / (altura * altura)
    with open("privado.txt", "a") as pasta:
        pasta.write(nome + " | " + f"{Peso} " +" | " + f"{altura}" + "|" f" imc: {imc:.2f}" "\n")

except:
    print("use pontos , para peso e altura , evite usar as vírgulas.")
