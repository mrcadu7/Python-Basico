import math
ang = float(input('Digite o valor do seu angulo:'))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print (f'Baseado no seu ângulo de {ang}º, temos os valor de seno {sen:.2f}, cosseno {cos:.2f} e tangente {tan:.2f}')
