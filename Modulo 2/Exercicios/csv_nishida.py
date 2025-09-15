import csv

pasta=open("yuri.csv")
dados=csv.DictReader(pasta)

for coluna in dados:
    if coluna['nome'] == 'Nishida':
        print(coluna)
