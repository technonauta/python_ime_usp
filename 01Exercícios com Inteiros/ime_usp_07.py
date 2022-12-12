#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
# Dados n e uma seqüência de n números inteiros, determinar a soma dos números pares.

def main():
    numini=int(input("Digite o primeiro número: "))
    seqnum=int(input("Digite a quantidade de elementos na sequência: "))

    if numini%2==0:
        soma=numini
        contador=1
        somatotal=0

        while contador <= seqnum:
            somatotal=somatotal+soma
            #print(f"IF PARES {soma}")
            soma += 2
            contador +=1

    else:
        soma=numini+1
        contador=1
        somatotal=0

        while contador <= seqnum:
            somatotal=somatotal+soma
            #print(f"ELSE IMPARES {soma}")
            soma += 2
            contador +=1
        
    print(f"SOMA {somatotal}")

main()
