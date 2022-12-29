#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
# Dizemos que um número i é congruente módulo m a j se i % m = j % m.
#Exemplo: 35 é congruente módulo 4 a 39, pois 35 % 4 = 3 = 39 % 4.
#Dados inteiros positivos n, j e m, imprimir os n primeiros naturais congruentes a j módulo m.

def main(): 
  print("congruência módulo")
  ene=int(input("Digite a q// de n.º naturais congruentes a j (mod m) q deseja: "))
  jota=int(input("Digite j: "))
  eme=int(input("Digite m: "))

  # i ≡ j (mod m)
  # n -> q// de is
  # restoI=iii%eme

  restoJ=jota%eme
  #print(f"RestoJ: {restoJ}")

  iii=0
  contador=0

  while contador < ene:
    iii+=1
    restoI=iii%eme

    if restoI == restoJ:
      print(f"{iii} ≡ {jota} (mod {eme}) resto {restoI}")
      contador +=1

main()