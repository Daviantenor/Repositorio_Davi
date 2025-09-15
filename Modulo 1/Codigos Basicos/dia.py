total=0
maior=0
for Dia in range(1,6):
    participantes=int(input(f"quantos participantes tem hoje no dia:{Dia}? "))
    total += participantes
   
    if participantes > maior:
     maior = participantes

print(f"maior é:{maior}")

print(f"total e:{total}")
media= total / 5
print(f"media e:{media}")
