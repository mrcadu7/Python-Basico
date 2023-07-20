aproveit = {}
partida = []
aproveit['nome'] = str(input('Nome do jogador: '))
quant = int(input(f'Quantas partidas {aproveit["nome"]} jogou? '))
for q in range(quant):
    partida.append(int(input(f'Quantos gols na partida {q+1}? ')))
aproveit['gols'] = partida[:]
aproveit['total'] = sum(partida)
print('=-'*15)
print(aproveit)
print('=-'*15)
for k, v in aproveit.items():
    print(f'O campo {k} tem valor {v}')
print('=-'*15)
print(f'O jogador {aproveit["nome"]} jogou {len(aproveit["gols"])} partidas.')
for i, v in enumerate(aproveit['gols']):
    print(f'    => Na partida {i}, fez {v} gols')
print(f'Foram um total de {aproveit["total"]} gols')
