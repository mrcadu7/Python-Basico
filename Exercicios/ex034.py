from time import sleep
s = float(input('Digite aqui o seu salário atual:'))
s1 = s+(s * 15/100)
s2 = s+(s * 10/100)
print(f'Seu salário é R${s:.2f}')
print('\033[1;31mCALCULANDO...\033[m')
sleep(2)
if s <= 1250.00:
    print(f'Seu salário foi reajustado em \033[1;31m15%\033[m e passará a ser de \033[1;31mR${s1}\033[m')
else:
    print(f'Seu salário foi reajustado em \033[1;31m10%\033[m e passará a ser de \033[1;31mR${s2}\033[m')
print('TENHA UM BOM DIA!')
