def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPOR FAVOR DIGITE UM NUMERO INTEIRO VÁLIDO!\033[m')
        except (KeyboardInterrupt):
            print('\033[31mO USUÁRIO NÃO DIGITOU UM VALOR!\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPOR FAVOR DIGITE UM NUMERO REAL VÁLIDO!\033[m')
        else:
            return n


#Programa Principal
n1 = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {n1}')
n2 = leiafloat('Digite um número real: ')
print(f'Você digitou o número {n2}')