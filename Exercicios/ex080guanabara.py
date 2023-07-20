n = []
lista = []
for c in range(0,5):
    n = int(input('Digite um valor:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos+1}')
                break
            pos += 1
print(f'Os valores digitados em ordem são: {lista}')

