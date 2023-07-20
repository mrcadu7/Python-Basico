import math
opo = float(input('Digite o valor do cateto oposto:'))
adj = float(input('Digite o valor do cateto adjacente'))
h = math.hypot(opo, adj)
#h = math.sqrt(opo**2+adj**2)
print (f'O valor da sua hipotenusa é {h:.2f}')
