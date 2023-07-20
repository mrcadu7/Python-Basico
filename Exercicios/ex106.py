def sistema(msg):
    from time import sleep
    while True:
        print('SISTEMA DE AJUDA PyHELP')
        msg = str(input('Função ou Biblioteca: '))
        (sleep(0.3))
        if msg != 'fim':
            print(f'Acessando o manual do comando "{msg}" ')
            sleep(1)
            print(help(msg))
        else:
            print('ATÉ LOGO!')
            break


#Programa principal
sistema('')