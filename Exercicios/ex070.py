esc = p = pb = ''
tot = ptot = pmil = n = menor = 0
while True:
    p = str(input('Digite o nome do produto:'))
    n = float(input('Digite o valor: R$'))
    tot += 1
    if n > 1000:
        pmil += 1
    if tot == 1: ###or preço < menor:###
        menor = n
        pb = p
    else:
        if n < menor:
            menor = n
            pb = p
    ptot += n
    esc = str(input('GOSTARIA DE CONTINUAR? [S/N]')).strip().upper()[0]
    while esc not in 'SN':
        esc = str(input('GOSTARIA DE CONTINUAR? [S/N]')).strip().upper()[0]
    if esc == 'N':
        break
print(f'O total da compra será R${ptot}')
print(f'Temos {pmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {pb} que custa R${menor}')
