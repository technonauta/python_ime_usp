#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Dizemos que um número natural n é palíndromo se
#567765 e 32423 são palíndromos.
#567675 não é palíndromo.
#Dado um número natural   n > 10 , verificar se n é palíndrome.


def main():

  num=int(input("Digite um natural: "))

  aux = num
  reverso = 0

  while aux != 0:
    reverso = reverso * 10 + aux % 10 # /* acrescenta mais um digito a direita */
    #print(f"reverso {reverso}")
    #print(f"aux r {aux}")
    aux = aux // 10                   #  /* joga fora esse digito */
    #print(f"aux {aux}")

  if reverso == num:
    print(f" {num} é palindrome")
  else:
    print(f" {num} não é palindrome")


main()