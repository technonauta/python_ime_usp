#https://www.ime.usp.br/~macmulti/exercicios/inteiros/index.html
#(FIS 88) Qualquer número natural de quatro algarismos pode ser dividido 
# em duas dezenas formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplos:  1297: 12 e 97. >> 5314: 53 e 14.
#Escreva um programa que imprime todos os MILHARES (4 algarismos) cuja raiz 
# quadrada seja a soma das dezenas formadas pela divisão acima.
#Exemplo: raiz de 9801 = 99 = 98 + 01. Portanto 9801 é um dos números a ser impresso.

def main ():
    natural=int(input("Digite um número natural:"))
    multi = natural

    for contd in range(natural):  
        resultado = multi*multi
        contagem=resultado
        num=len(str(contagem))
        lista = []

        for cont in range(num):
            
            if multi>3 : #evita o "bug" str.join(iterable) 
                separar = resultado % 10
                lista.insert(0,separar)
                diminuir = resultado // 10
                resultado = diminuir
        
                metade_um = lista[:len(lista) // 2]
                metade_dois = lista[len(lista) // 2:]

        prim_meta=''.join([str(item) for item in metade_um])
        segn_meta=''.join([str(item) for item in metade_dois])

        #str.join(iterable) >> Return a string which is the concatenation of the strings in iterable. 
        #A TypeError will be raised if there are any non-string values in iterable, including bytes objects. 
        # The separator between elements is the string providing this method.

        conferencia = int(prim_meta) + int(segn_meta) #ValueError: invalid literal for int() with base 10:''

        if conferencia == multi:
            print(f"{multi}² = {contagem}")
            print(f"{prim_meta} + {segn_meta}= {multi}")
            print("")

        multi = multi - 1
main()