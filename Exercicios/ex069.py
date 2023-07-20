s = esc = ''
contmai = conth = contmul = 0
while True:
    print('CADASTRE UMA PESSOA')
    i = int(input('IDADE:'))
    s = str(input('SEXO [M/F]:')).strip().upper()[0]
    while s not in 'MF':
        s = str(input('SEXO [M/F]:')).strip().upper()[0]
    if i >= 18:
        contmai += 1
    if s == 'M':
        conth += 1
    if s == 'F' and i < 20:
        contmul += 1
    esc = str(input('GOSTARIA DE CONTINUAR? [S/N]')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('GOSTARIA DE CONTINUAR? [S/N]')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Dos dados acrescentados:')
print(f'{contmai} eram maiores de idades, {conth} eram o numero de homens e {contmul} o numero de mulheres abaixo dos 20')
