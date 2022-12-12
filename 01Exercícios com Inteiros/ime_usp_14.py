#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
# Faça um programa que, dado n, calcula Fn //seqüência de Fibonacci 

def main():
    print("Sequência de Fibonacci")

    numene=int(input("Digite um número: "))
    #1   2   3   4   5   6    7   8    9
    #1 - 1 - 2 - 3 - 5 - 8 - 13 - 21 - 34

    f1=1
    f2=1

    if (numene==1) or (numene==2):
        print(f"{1}")
    
    else:
        for contad in range(2,numene):
            fibo=f1+f2
            f1=f2
            f2=fibo

        print("F(%d) = %d" %(numene,fibo))

main()
