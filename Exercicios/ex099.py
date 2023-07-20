def maior(*num):
    print('ANALISANDO OS VALORES RECEBIDOS:')
    if len(num) > 0:
        print(f'Recebi os valores {num}, um total de {len(num)} números')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print('NÃO FORAM INFORMADOS NUMEROS')

#programa principal
maior(2, 3, 5, 9, 2, 1,)
maior(4, 7, 0)
maior(6)
maior()