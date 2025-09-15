import csv

pasta=open("marca.csv")
dados=csv.DictReader(pasta)

for linha in dados:
    if linha['Marca'] =='Ford':
        print(linha)
