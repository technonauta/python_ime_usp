#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando o algoritmo de Euclides.

def main():
    numA = int(input("Digite um número inteiro positivo: "))
    numB = int(input("Digite um número inteiro positivo: "))

    anterior = numA
    atual = numB

    resto = atual % anterior
    while resto !=0:
        resto = anterior % atual;
        anterior = atual;
        atual = resto;

    print("MDC (%d,%d)=%d" %(numA,numB,anterior))

main()
