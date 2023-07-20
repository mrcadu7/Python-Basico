from random import randint


def sorteia(lista):
    print('SORTEANDO 5 VALORES:')
    for cont in range(5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print()

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Os valores pares sorteados são {lista} e seu somatório é {soma}')


#Programa Principal
numeros = []
sorteia(numeros)
somapar(numeros)



