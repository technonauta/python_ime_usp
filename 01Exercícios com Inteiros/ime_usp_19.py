#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados três números, imprimi-los em ordem crescente.

def main():
    print("Ordem Crescente")
    num1=int(input("Digite o 1n: "))
    num2=int(input("Digite o 2n: "))
    num3=int(input("Digite o 3n: "))

    if num1<num2<num3:
        print(f"{num1} , {num2} , {num3}")
    elif num2<num1<num3:
        print(f"{num2} , {num1} , {num3}")
    elif num3<num1<num2:
        print(f"{num3} , {num1} , {num2}")
    elif num1<num3<num2:
        print(f"{num1} , {num3} , {num2}")
    elif num2<num3<num1:
        print(f"{num2} , {num3} , {num1}")
    else:
        print(f"{num3} , {num2} , {num1}")
    

main()