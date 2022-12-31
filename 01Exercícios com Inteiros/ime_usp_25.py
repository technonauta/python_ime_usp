#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#25.  Simule a execução do programa abaixo destacando a sua saída:

#tradução do código em C para python.


print(f"Digite um par de numeros: ")
a=int(input("digite a: "))
b=int(input("digite b: "))
print(f"({a}, {b})\n")

total = 0 
soma  = 0

while a!=0:
  total = total + 1 
  termo = 1

  for i in range(b):
    termo = termo * a
  print(f"Resp = {termo}")
  soma = soma + termo
  print(f"Soma = {soma}\n")

  print(f"Digite um par de numeros: ")
  a=int(input("digite a: "))
  b=int(input("digite b: "))
  print(f"({a}, {b})\n")

print(f"Total de pares: {total}\n")
