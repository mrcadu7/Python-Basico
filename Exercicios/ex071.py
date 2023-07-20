saque50 = saque20 = saque10 = saque1 = saque = 0
while True:
    saque = int(input('Que valor você quer sacar? R$'))
    if saque >= 50:
        if saque%50 > 0:
            saque50 = saque%50
            print(f'Total de {saque // 50} cédulas de R$50')
        if saque50%20 > 0:
            saque20 = saque50%20
            print(f'Total de {saque50 // 20} cédulas de R$20')
        if saque20%10 > 0:
            saque10 = saque20%10
            print(f'Total de {saque20 // 10} cédulas de R$10')
        if saque10%1 == 0:
            saque1 = saque10%1
            print(f'Total de {saque10 // 1} cédulas de R$1')
            break
    if saque < 50 and saque >19:
        if saque%20 > 0:
            saque20 = saque%20
            print(f'Total de {saque // 20} cédulas de R$20')
        if saque20%10 > 0:
            saque10 = saque20%10
            print(f'Total de {saque20 // 10} cédulas de R$10')
        if saque10%1 == 0:
            saque1 = saque10%1
            print(f'Total de {saque10 // 1} cédulas de R$1')
            break
    if saque < 20 and saque > 9:
        if saque%10 > 0:
            saque10 = saque%10
            print(f'Total de {saque // 10} cédulas de R$10')
        if saque10%1 == 0:
            saque1 = saque10%1
            print(f'Total de {saque10 // 1} cédulas de R$1')
            break
    if saque < 10:
        if saque%1 == 0:
            saque1 = saque%1
            print(f'Total de {saque // 1} cédulas de R$1')
            break
print('fim')
