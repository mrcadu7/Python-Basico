pt = int(input('Digite aqui o primeiro termo de sua P.A:'))
r = int(input('Digite aqui a sua razão da P.A:'))
t = pt
c = 1
while c <= 10:
    print(f'{t}', end=' -> ')
    t = t + r
    c = c + 1
print('FIM')