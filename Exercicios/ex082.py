lista = []
pares = []
impares = []
while True:
    v = (int(input('Digite um valor:')))
    lista.append(v)
    if v%2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    while esc not in 'SN':
        print('OPÇÃO INVALIDA')
        esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if esc == 'N':
        break
print(f'Sua lista: {lista}')
print(f'Sua lista com valores pares: {pares}')
print(f'Sua lista com valores impares: {impares}')
