galera = []
dados = []
pesg = []
pesm = []
esc = pesg = pesm = ''
cont = gord = 0
magr = 999
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    galera.append(dados[:])
    dados.clear()
    cont += 1
    esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    while esc not in 'SN':
        print('OPÇÃO INVALIDA')
        esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if esc == 'N':
        break
for p in galera:
    if p[1] > gord:
        gord = p[1]
        pesg = p[0]
    elif p[1] < magr:
        magr = p[1]
        pesm = p[0]
print('=-'*15)
print(f'Foram cadastradas {cont} pessoas!')
print(f'O maior peso foi {gord}Kg. Peso de {pesg}')
print(f'O menor peso foi {magr}Kg. Peso de {pesm}')
