opção=1
while opção != 2:
    nome = input("nos diga seu nome")
    peso = float(input("qual o seu peso?"))
    minha_altura = float (input("qual a sua altura?"))
   
        
    imc = peso / (minha_altura * minha_altura)
        
    if imc <=18.6 :
            
            print(f"abaixo do peso")
    elif imc <=25 :
             
            print(f"peso normal")
    elif imc <=30 :
            
            print(f"sobrepeso")
        
    elif imc <=35.7 :
            
            print(f"obesidade de 1°grau")
        
    elif imc <=38.6 :
            
            print(f"obesidade de 2°grau")
   
    else :
            print(f" offline ")    
           
    opção = int(input("escolha uma:\n1-digite  para prosseguir:\n2- digite para parar"))
