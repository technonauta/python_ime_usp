#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dado um inteiro não-negativo n, determinar n! FATORIAL

def main():
    num=int(input(f"Digite um número inteiro não negativo: "))
    
    fator=1
    contador=0
    for contador in range(2,num+1):
        fator=fator*contador

    print(f"{num}! = {fator}")
    
main()