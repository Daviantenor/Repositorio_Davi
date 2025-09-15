import csv

pasta=open("marca.csv")
dados=csv.DictReader(pasta)

for linha in dados:
    if linha['Ano']=='2022':
        
        print(linha)
