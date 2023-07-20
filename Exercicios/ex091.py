from random import randint
from time import sleep
print('VALORES SORTEADOS:')
sleep(1)
jogadores = {'jogador1': randint(1,6),
             'jogador2': randint(1,6),
             'jogador3': randint(1,6),
             'jogador4': randint(1,6)}
ranking = []
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('RANKING DOS JOGADORES:')
ranking = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)




