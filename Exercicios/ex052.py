n = int(input('Digite um número inteiro:'))
if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 and n % 11 != 0:
    print(f'Seu número {n} é primo!')
elif n == 2 or n==3 or n==5 or n==7 or n==11:
    print(f'Seu número {n} é primo!')
else:
    print(f'Seu número {n} não é primo!')
