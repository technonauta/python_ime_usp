#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dados o número n de alunos de uma turma de Introdução aos Autômatos a Pilha (MAC 414) e suas notas da primeira prova, 
#determinar a maior e a menor nota obtidas por essa turma (Nota máxima = 100 e nota mínima = 0).

def main():
    numerodenotas=int(input("Quantas notas você vai digitar? "))

    maiornota=-1
    menornota=101
    contador=1

    while contador <= numerodenotas:
        notaluno=float(input(f"Digite a {contador}ª nota: "))
        contador=contador+1

        #menor nota
        if notaluno<menornota:
            menornota=notaluno

        #maior nota
        if notaluno>maiornota:
            maiornota=notaluno

    print(f"A maior nota foi: {maiornota}")
    print(f"A menor nota foi: {menornota}")

main()
