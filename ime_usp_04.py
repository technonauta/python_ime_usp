#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados um inteiro x e um inteiro não-negativo n, calcular x elevado n.

import math

def main():
    numbase=int(input("Digite o númeo base: "))
    numexpo=int(input("Digite a potência: "))

    resultado=math.pow(numbase, numexpo);

    print(f"{resultado}")

main()