#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#(POLI 87) Dados n e uma seqüência de n números inteiros, determinar quantos segmentos de números 
# iguais consecutivos compõem essa seqüência.
#Exemplo: A seguinte seqüência é formada por 5 segmentos de números iguais:   5,  2,  2,  3,  4,  4,  4,  4,  1,  1


lista = [5,  2,  2,  3,  4,  4,  4,  4,  1,  1]
lista_sem_repeticao = list(set(lista))
contagem = len(lista_sem_repeticao)
print(contagem)

#https://www.youtube.com/watch?v=1T_bxlFIshI
#LEN Return the number of items in a container.

