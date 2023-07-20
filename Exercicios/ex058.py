from random import randint
from time import sleep
c = 1
r = randint(0,1)
print('-=-' *15)
print('Vou pensar em um número de 0 a 10, em quantas tentativas você consegue acertar!?')
print('-=-' *15)
n = int(input('Em qual número pensei? '))
while n != r:
    c = c + 1
    print('\033[1;031mCALCULANDO...\033[m')
    sleep(1)
    n = int(input('PATÉTICO! VOCÊ ERROU! TENTE OUTRO NÚMERO: '))
print('\033[1;031mCALCULANDO...\033[m')
sleep(1)
if c == 1:
    print(f'Parabéns, você disse o número \033[1;031m{n}\033[m e acertou de \033[1;031mPRIMEIRA!\033[m Bip bip bop!')
elif c < 4:
    print(f'Parabéns, você disse o número \033[1;032m{n}\033[m e acertou na \033[1;032m{c}ª tentativa!\033[m'
          f' Nada mal!')
elif c < 6:
    print(f'Parabéns, você disse o número \033[1;033m{n}\033[m e acertou na \033[1;033m{c}ª tentativa!\033[m'
          f'Podia ser melhor!')
elif c < 10:
    print(f'Carambolas, cara! você disse o número \033[1;034m{n}\033[m e acertou na \033[1;034m{c}ª tentativa!\033[m'
          f'Parece que foi complicado, não é? HA HA HA')
else:
    print(f'Eu já havia ido embora enquanto você estava tentando! VOCÊ É MUITO RUIM! '
          f'você disse o número \033[1;035m{n}\033[m e acertou na \033[1;035m{c}ª tentativa!\033[m')
print('-=-' *15)



