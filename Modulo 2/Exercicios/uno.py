import csv

with open('marca.csv', 'a' ,newline="")as pasta:
    escritor=csv.writer(pasta)
    escritor.writerow(['Fiat','Uno de escada','2005','40.000'])
