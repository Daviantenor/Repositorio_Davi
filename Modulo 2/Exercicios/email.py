nome = input("Nos diga seu nome: ")
email=input("Nos diga seu email: ")

with open("pessoal.txt", "a") as beraldo:
    beraldo.write(nome + " | " + email + "\n")
