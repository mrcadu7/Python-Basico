def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print()
            print('\033[0;31mDIGITE UM NUMERO VALIDO\033[m')
        if ok:
            return valor


#Programa Principal
n = leiaint('Digite um número:')
print(f'Você digitou o número {n}')
