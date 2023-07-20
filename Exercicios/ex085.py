lista = []
pares = []
impares = []
temp = []
for v in range(7):
    temp.append(int(input('Digite um valor:')))
    if temp[0]%2 == 0:
        pares.append(temp[:])
    else:
        impares.append(temp[:])
    temp.clear()
lista = pares, impares
lista[0].sort()
lista[1].sort()
print(f' A lista de números pares é: {lista[0]}')
print(f' A lista de números impares é: {lista[1]}')