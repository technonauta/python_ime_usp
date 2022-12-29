#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados três números naturais, verificar se eles formam os lados de um triângulo retângulo.

def main():
    print("Triângulo Retângulo")
    print("Digite 03 numeros para verificar se forma tri ret")
    aaa=int(input("a: "))
    bbb=int(input("b: "))
    ccc=int(input("c: "))

    #triang retang
    #(a*a)=(b*b)+(c*c)

    cala=(bbb*bbb)+(ccc*ccc)
    calbc=(aaa*aaa)

    if cala == calbc:
        print("\ntriângulo retângulo")
    else:
        print("\nnão triângulo retângulo")

main()