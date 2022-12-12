#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
#Exemplo: Para n=4 a saída deverá ser 1,3,5,7.

def main():
    numdig=int(input("Digite número natural: "))

    contagem=1
    cont=1
    print(f"números ímpares: ")
    while cont <= numdig:
        print(f"{contagem}")
        contagem=contagem+2
        cont=cont+1

main()