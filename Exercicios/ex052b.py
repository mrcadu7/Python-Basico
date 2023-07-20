num = int(input('Digite um número '))
tot = 0 #aqui ele vai contar quantas divisões
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ') #nessas duas condições:amarelo o num é divisivel, vermelho não é divisivel
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end='')
print(f'\n\033[mO número {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso é numero Primo')
else:
    print('E por isso NÃO PRIMO')