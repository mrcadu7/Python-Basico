import sys
from time import sleep
from random import randint
r = randint (1,3)
print('\033[1;032m-=-' *15)
print('\033[1;031mVAMOS JOGAR JOKENPO!')
print('\033[1;032m-=-' *15)
sleep(2)
print('\033[1;031mPOR FAVOR DIGITE \033[1;034m (1) para "PEDRA"\033[m , \033[1;035m(2) para "PAPEL"\033[m E \033['
                    '1;036m(3) para "TESOURA"\033[m!')
escolha = int(input(''))
if escolha == 1:
    print('\033[1;031mVOCÊ ESCOLHEU\033[m \033[1;034mPEDRA!')
elif escolha == 2:
    print('\033[1;031mVOCÊ ESCOLHEU\033[m \033[1;035mPAPEL!')
elif escolha == 3:
    print('\033[1;031mVOCÊ ESCOLHEU\033[m \033[1;036mTESOURA!')
else:
    print('\033[1;031mVOCÊ NÃO CONSEGUE NEM FAZER UMA ESCOLHA!?')
    sys.exit(   )
print('''
\033[1;031mENQUANTO..
''')
sleep(1)
if r == 1:
    print('\033[1;031mEU ESCOLHI\033[m \033[1;034mPEDRA!')
elif r == 2:
    print('\033[1;031mEU ESCOLHI\033[m \033[1;035mPAPEL!')
elif r == 3:
    print('\033[1;031mEU ESCOLHI\033[m \033[1;036mTESOURA!')
print('''
\033[1;031mLOGO..
''')
sleep(1)
if escolha == r:
    print('EMPATAMOS!')
elif escolha == 1 and r == 2 or escolha == 2 and r == 3 or escolha == 3 and r == 1:
    print('HA HA HA VOCÊ PERDEU! HA HA HA')
elif r == 1 and escolha == 2 or r == 2 and escolha == 3 or r == 3 and escolha == 1:
    print('V-v-V-VOCÊ V-v-v-VENCEU! ')
print('\033[1;032m-=-' *15)