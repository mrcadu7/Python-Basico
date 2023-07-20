pt = int(input('Digite aqui o primeiro termo de sua P.A: '))
r = int(input('Digite aqui a sua razão da P.A: '))
t = pt
c = 1
tot = 0
m = 10
while m != 0:
    tot = tot + m
    while c <= tot:
        print(f'{t}', end=' -> ')
        t = t + r
        c = c + 1
    print('PAUSA')
    m = int(input('Quantos termos a mais? '))
print(f'PROGRESSÃO FINALIZADA COM {tot} termos')