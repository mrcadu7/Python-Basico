a1 = int(input('Digite aqui o primeiro termo de sua P.A:'))
n = 10
r = int(input('Digite aqui a sua razão da P.A:'))
an = a1 +(n-1) * r
for c in range(a1,an+r,r):
    print(c,end=' -> ')
print('FIM')