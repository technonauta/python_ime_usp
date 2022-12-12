#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dada uma seqüência de números inteiros não-nulos, seguida por 0, imprimir seus quadrados.

import math
def main():

    while seqnum !=0:
        seqnum = int(input(f"\nDigite um número: "))
        conta = math.pow (seqnum, 2);

        print(f"O quadrado é: {conta}")

main()
