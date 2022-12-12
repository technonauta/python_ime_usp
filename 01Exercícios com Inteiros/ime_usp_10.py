#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
#Exemplo: 120 é triangular, pois 4.5.6 = 120.
#Dado um inteiro não-negativo n, verificar se n é triangular.

def main(): #resposta exercicio
    numene=int(input("Digite o n: "))

    cont=1
    while cont*(cont+1)*(cont+2) < numene:
        cont+= 1
  
    if cont*(cont+1)*(cont+2) == numene:
        print("%d é o produto %d*%d*%d" %(numene,cont,cont+1,cont+2))
    else:
        print("%d não é triangular" %(numene))
main()


def main(): #minha resposta
    #print("Verificar se n é triangular")
    numene=int(input("\nDigite o n: "))

    cont=1
    for cont in range(numene):
        triang=cont*(cont+1)*(cont+2) #solução q o problema pede
        
        if (triang==numene):
            print(f"\nnúmero triangular (solç 3n): {numene} = {cont}*{cont+1}*{cont+2}")
                   
    cont=1
    for cont in range(numene):
        postri=(cont*(cont+1))/2 #solução q segue a definição
        
        if (postri==numene):
            print(f"número triangular (solç formula): {postri:.0f}=({cont}*({cont+1}))/2")
        
    print(f"\nfim.")
    print(f"(sem resposta implica em não ser triangular)")
main()
