from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
randint(1,10), randint(1,10))
print('Os números sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ',)
print(f'\nO maior número sorteado foi {max(numeros)} enquanto o menor foi {min(numeros)}')

