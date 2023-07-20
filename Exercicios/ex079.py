valores = list()
while True:
    n = int(input('Digite um valor:'))
    if n not in valores:
        valores.append(n)
        print('ADICIONADO COM SUCESSO!')
    else:
        print('NUMERO DUPLICADO NÃO ACEITO!')
    r = str(input('Deseja continuar? [S/N]:')).strip().upper()
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]:')).strip().upper()
    if r == 'N':
        break
valores.sort()
print(valores)

