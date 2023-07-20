import math

n = int(input('Por favor, digite quantos termos você deseja ver: '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end='')
c = 3
while c <= n:
    t3 = t1 + t2
    print(f' > {t3}', end='')
    t1 = t2
    t2 = t3
    c = c + 1
print(' > FIM')

#p = ((1.618034 ** n - (1 - 1.618034) ** n)/(5 ** 0.5))
#print(f'{math.floor(p)}')
