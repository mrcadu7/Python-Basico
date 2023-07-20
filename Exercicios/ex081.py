n = []
while True:
    n.append(int(input('Digite um valor')))
    esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    while esc not in 'SN':
        print('OPÇÃO INVALIDA')
        esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if esc == 'N':
        break
print(f'Os valores digitados são:')
print(n)
print(f'No total foram digitados {len(n)} números')
print('Em ordem decrescente sua lista fica:')
n.sort(reverse=True)
print(n)
if 5 in n:
    print('O valor 5 foi digitado!')
else:
    print('O valor 5 não foi digitado!')
