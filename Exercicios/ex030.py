from math import modf
n = int(input('Digite um número inteiro:'))
d = n%2
if d == 0:
    print(f'O seu número {n} é um número par!')
else:
    print(f'O seu número {n} é um número ímpar')

