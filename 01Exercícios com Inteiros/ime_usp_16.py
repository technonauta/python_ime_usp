#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
# Dado um número natural na base binária, transformá-lo para a base decimal.
# Exemplo: Dado 10010 a saída será 18, pois 1. 2 4 + 0. 2 3 + 0. 2 2 + 1. 2 1 + 0. 2 0 = 18.

def main():
    print("converter número binário para decimal")

    binario=int(input("Digite o n.º:"))
    n=len(str(binario)) #conta o n.º de algarismos
    cont_binario = binario
    decimal = 0
    i = 0

    while n >=0 :

        resultado = binario % 10    #resto da divisão > n.º q sera multiplicado por 2 elevado a 0....10...
        decimal = decimal + (resultado * (2**i))
        n = n - 1
        i = i + 1
        binario = binario //10      #divisao inteira > tira o último n.º do n.º inicial

    
    print(f"binario: {cont_binario} >> decimal: {decimal}")

main()