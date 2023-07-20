times = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Fluminense',
         'Fortaleza', 'Bragantino', 'Athletico-PR', 'Santos', 'Internacional', 'Corinthians', 'Cuiabá', 'Bahia',
         'Goiás', 'Vasco da Gama', 'América-MG', 'Coritiba')
print(f'Dos times do brasileirão, os cinco primeiros colocados são: {times[0:5]}')
print(f'Dos times do brasileirão, os quatro ultimos colocados são: {times[-4:]}')
print(f'Em ordem alfabética, os times são: {sorted(times)}')
print(f'O Internacional está na posição {times.index("Internacional")+1}ª posição')

