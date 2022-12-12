#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#(MAT 89) Dizemos que um inteiro positivo n é perfeito se for igual à soma de seus divisores positivos diferentes de n.
#Exemplo: 6 é perfeito, pois 1+2+3 = 6.
#Dado um inteiro positivo n, verificar se n é perfeito.

def main():
    print("Teste se um número é perfeito ou não")
    numene=int(input("\nDigite um número inteiro positivo: "))
    vetor=[0 for x in range(numene)]

    soma=0
    for contad in range(1,numene):
        if numene%contad==0:
            vetor[contad]=contad
            soma+=contad

    if soma==numene:
        print(f"{numene} número perfeito")
        for contad in range(1,numene):
            if vetor[contad]!=0:
                print(f"{vetor[contad]}")

    else:
        print(f"{numene} não é número perfeito")

main()

####
#def perfeito(n4): #resposta mais completa q tras os números perfeitos até o número digitado
    
#    soma=0
#    for val in range(1,n4):
#        if n4 % val == 0:
#            soma += val

#    if soma==n4:
#        return True
#    else:
#        return False
        
#def exibe():
#    n = int(input('\nExibir perfeitos até o número: '))
    
#    for valb in range(1,n+1):
#        if(perfeito(valb)):
#            print(valb)
    
#while True:
#    exibe()
