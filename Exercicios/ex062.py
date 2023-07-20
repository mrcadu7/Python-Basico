pt = int(input('Digite aqui o primeiro termo de sua P.A: '))
r = int(input('Digite aqui a sua razão da P.A: '))
t = pt
c = 1
mais = 10
tot = 0
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print(f'{t}', end=' -> ')
        t = t + r
        c = c + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais? '))
print(f'Progressão finalizada com {tot} termos!')
