from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O valor fatorial de {n}! é: {f}')
c = ' '
while c != 'N':
    c = str(input('Quer continuar calculando o fatorial? [S/N]: ')).strip().upper()
    if c == 'S':
        n = int(input('Digite um número: '))
        print(f'O valor fatorial de {n}! é: {f}')
    elif c == 'N':
        print('ENCERRANDO...')
    else:
        print('POR FAVOR DIGITE UMA OPÇÃO VÁLIDA!')
print('OBRIGADO PELA PREFERENCIA!')