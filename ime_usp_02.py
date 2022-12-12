#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dado um número inteiro positivo n, calcular a soma dos n primeiros números inteiros positivos.

def main():

    numdigi=int(input("Quantos números serão digitados? "))

    contagem=1
    soma=0
    while contagem <= numdigi:
        soma=soma+contagem
        contagem=contagem+1

    print(f"a soma dos primeiros {numdigi} positivos inteiros é {soma}")

main()