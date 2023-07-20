lista = []
for v in range(5):
    valores = (int(input('Digite aqui um valor')))
    p = 0
    while p < len(lista) and lista[p] < valores:
        p += 1
    lista.insert(p, valores)
    print(f'Valor adicionado na posição {p+1}')
print(lista)
