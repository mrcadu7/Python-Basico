from time import sleep
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite mais um número diferente dos demais:'))
print('ANALISANDO...')
sleep(2)
if n1>n2 and n1>n3:
    print(f'Seu número maior é {n1}')
if n2>n1 and n2>n3:
    print(f'Seu número maior é {n2}')
if n3>n1 and n3>n2:
    print(f'Seu número maior é {n3}')
if n1<n2 and n1<n3:
    print(f'Seu número menor é {n1}')
if n2<n1 and n2<n3:
    print(f'Seu número menor é {n2}')
if n3<n1 and n3<n2:
    print(f'Seu número menor é {n3}')
