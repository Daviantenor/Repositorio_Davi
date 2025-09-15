nome = input("Nos diga seu nome: ")
nota_da_mensal=float(input("Nos diga sua nota da prova mensal: "))
nota_da_global=float(input("Nos diga sua nota da prova global: "))
atividades=float(input("Nos diga a nota das suas atividades: "))
try:
    media = (nota_da_global + nota_da_mensal + atividades) / 3
    with open("planilha2.txt", "a") as pasta:
        pasta.write(nome + " | " + f"{nota_da_global}" + " |" + f"{nota_da_mensal}" +"|" f"{atividades} " + "|" f"media :{media:.2f}" "\n")
except:
    print("Digite as notas corretamente.")
