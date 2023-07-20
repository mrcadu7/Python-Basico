from random import sample
temp = []
jogos = int(input('QUANTOS JOGOS PARA SORTEAR? '))
print(f'=-=-=- SORTEANDO {jogos} JOGOS! =-=-=-')
for j in range(jogos):
    print(f'Jogo {j+1}: ', end='')
    for r in sample(range(1, 61), 6):
        temp.append(r)
    print(sorted(temp), end=' ')
    temp.clear()
    print()
print('BOA SORTE!')



