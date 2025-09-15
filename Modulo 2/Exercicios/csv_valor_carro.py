import csv

pasta=open("marca.csv")
dados=csv.DictReader(pasta)

for linha in dados:
    if linha['Modelo']=="Ka":
        
        print(linha)
    elif linha["Modelo"]=="Mobi":
        print(linha)
    elif linha['Modelo']=="Gol":
        print(linha)
    else:
        print("...")
