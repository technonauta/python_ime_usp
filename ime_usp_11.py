#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dado um inteiro positivo n, verificar se n é primo.

def main():
    numene = int(input("Digite um número inteiro positivo: "))

    divisor=1
    contad=0
    while divisor<=numene:
        resul=numene/divisor #conta de divisão comum
        resultado=numene%divisor #conta para resto zero

        if resultado==0:
            contad+=1
            print(f"R: {numene} dividido {divisor} = {resul:.0f}")

        divisor+=1
        
    if contad==2:
        print(f"\nPRIMO {numene}")
    else:
        print(f"\nNÃO É PRIMO {numene}")
main()