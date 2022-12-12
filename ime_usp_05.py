#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#Uma loja de discos anota diariamente durante o mês de março a quantidade de discos vendidos.
#Determinar em que dia desse mês ocorreu a maior venda e qual foi a quantidade de discos vendida nesse dia.

def main():
    mes=str(input("Digite o número do mês que quer consultar: "))

    if mes=="março":
        mesdias=31
    else: mesdias=30

    vetor=[0 for x in range(mesdias)]

    maisvendido=0
    for contagem in range(mesdias):
        discosdia=int(input(f"Número de discos vendidos no dia {contagem+1}: "))
        if discosdia>maisvendido:
            maisvendido=discosdia
            diadomes=contagem
    print(f"No mês {mes} o dia com mais vendas foi {diadomes} num total de {discosdia} discos vendidos")

main()