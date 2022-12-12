#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados n e dois números inteiros positivos i e j diferentes de 0, imprimir em ordem 
# crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
#Exemplo: Para n = 6 , i = 2 e j = 3 a saída deverá ser : 0,2,3,4,6,8.

def main():
    print("Exercício dos múltiplos números inteiros positivos")

    n=int(input("digite n: "))
    i=int(input("digite i: "))
    j=int(input("digite j: "))
    
    mult_i=mult_j=0

    for k in range(n):
        if mult_i==mult_j:
            print(mult_i)
            mult_i += i
            mult_j += j

        elif mult_i<mult_j:
            print(mult_i)
            mult_i += i

        else:
            print(mult_j)
            mult_j += j

main()