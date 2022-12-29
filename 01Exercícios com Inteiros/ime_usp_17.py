#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
# Dado um número natural na base decimal, transformá-lo para a base binária.
#Exemplo: Dado 18 a saída deverá ser 10010.

def main():
    print("converter número decimal para binário")

    decimall=int(input("Digite o n.º:"))
    num_decimall = decimall
    contador = 1
    binario = 0


    while num_decimall > 0:
        resto = num_decimall % 2   #proximo digito binario menos significativo
        num_decimall = num_decimall // 2  #remove esse digito do que resta
        binario = binario + resto * contador   #adiciona o digito como o mais significativo
        contador = contador * 10

    print(f"decimal: {decimall} >> binário: {binario}")

main()