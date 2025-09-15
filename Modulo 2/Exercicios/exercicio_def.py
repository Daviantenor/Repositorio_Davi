def medidor():
    

    nome=input("nos diga seu nome: ")
    altura=float(input("nos diga sua altura:"))

    if altura <=1.45:
        print(f"sinto muito te dizer isso mas... você é um anão {nome}😭.")
    elif altura <=1.75:
        print(f"você é até que alto , mas ainda está na média {nome}🙂.")
    else:
        print(f"caraca {nome}, você é um poste🤩🤩.")


medidor()
