from random import randint
from time import sleep

r = randint (0,5)
print('-=-' *15)
print('Vou pensar em um número de 0 a 5 e você deve acertar, se não morre!')
print('-=-' *15)
n = int(input('Em qual número pensei?'))
print('CALCULANDO...')
sleep(3)
print('-=-' *15)
if n == r:
    print(f'Parabéns, você disse o número {n} e a sua vida será poupada! Bip bip bop!')
else:
    print(f'O NÚMERO CORRETO É {r}, VOCÊ ERROU E EU VOU COMER O SEU CU!! BOP BOP BIP BOP!!')
print('-=-' *15)
