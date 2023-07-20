dados = []
jogadores = {}
partida = []
#coleta de dados
while True:
    jogadores['nome'] = str(input('Nome do jogador: '))
    quant = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for q in range(quant):
        partida.append(int(input(f'Quantos gols na partida {q+1}? ')))
    jogadores['gols'] = partida[:]
    jogadores['total'] = sum(partida)
    dados.append(jogadores.copy())
    partida.clear()
    while True:
        resp = str(input('DESEJA CONTINUAR? [S/N]'))
        if resp in 'sSnN':
            break
        else:
            print('DIGITE UMA OPÇÃO VALIDA!')
    if resp in 'nN':
        break
print('=-'*15)
'''print(f'{"cod":<6}{"nome":<12}{"total":<9}{"gols"}')'''
#tabela geral
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(dados):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
'''for c, jogadores in enumerate(dados):
    print(f' {c:<4} {jogadores["nome"]:<13} {jogadores["total"]:<6} {jogadores["gols"]}')'''
print('=-'*20)
#Individual
while True:
    n = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if n == 999:
        break
    elif n > len(dados)-1:
        print('Digite uma opção válida')
    else:
        print(f'Mostrando os dados do jogador {dados[n]["nome"]}:')
        for i, v in enumerate(dados[n]['gols']):
            print(f'    => Na partida {i+1}, fez {v} gols')
print('OBRIGADO POR USAR ESSE APP ARROMBADO!')


