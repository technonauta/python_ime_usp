#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#(POLI 89) Dados n e uma seqüência de n números inteiros, determinar o 
# comprimento de um segmento crescente de comprimento máximo.
#Exemplos:
#Na seqüência   5,  10,  3,  2,  4,  7,  9,  8,  5   o comprimento do segmento crescente máximo é 4.
#Na seqüência   10,  8,  7,  5,  2   o comprimento de um segmento crescente máximo é 1.

def main():
    quatnum=int(input("quantos números você vai digitar? "))
    numant = 0
    compseg = 0
    compmax =0

    for cont in range(1,quatnum+1):
        num=int(input(""))
        if num>numant:
            compseg +=1
            if compmax<compseg:
                compmax=compseg
        else:
            compseg=1
        numant=num
    print(f"o comprimento crescente máximo é {compmax}")

main()