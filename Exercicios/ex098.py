from time import sleep
def contador(inic, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=-'*20)
    print(f'Contagem de {inic} até {fim} de {passo} em {passo}:')
    sleep(1)
    cont = inic
    if inic < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += passo
        print()
    else:
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= passo
        print()


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('DIGITE O VALOR INICIAL :'))
f = int(input('DIGITE O VALOR FINAL :'))
p = int(input('DIGITE O VALOR DO PASSO :'))
contador(i, f, p)