#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#São dados dois números inteiros positivos p e q, sendo que o número 
# de dígitos de p é menor ou igual ao número de dígitos de q. Verificar 
# se p é um subnúmero de q.
#Exemplos:
#p = 23, q = 57238, p é subnúmero de q.
#p = 23, q = 258347, p não é subnúmero de q.

#############################################
#https://www.guj.com.br/t/manipulacao-de-numeros-em-uma-string-iniciante/365308


def main():
    print("solução menor")
    q = input("Digite o valor de Q: ")
    p = input("Digite o valor de P: ")

    if q.find(p) != -1:
        print("P é subnumero de Q")
    else:
        print("P não é subnumero de Q")
main()