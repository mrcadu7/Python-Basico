from random import randint
print('~-~-~-~-'*5)
print('VAMOS JOGAR PAR OU IMPAR?')
cont = 0
while True:
    esceu = str(input('PAR OU IMPAR? [P/I]').strip().upper())
    escpc = ''
    if esceu == 'P':
        escpc = 'I'
    if esceu == 'I':
        escpc = 'P'
    eu = int(input('DIGITE UM VALOR:'))
    pc = randint(0, 10)
    soma = eu + pc
    escolhaf = ''
    if soma%2 == 0:
        escolhaf = 'PAR'
    else:
        escolhaf = 'IMPAR'
    print(f'Você escolheu o valor {eu} e o computador o valor {pc}')
    print(f'A soma foi {soma}, que é um valor {escolhaf}')
    if escolhaf == 'PAR':
        if esceu == 'P':
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE!')
        if escpc == 'P':
            print('EU VENCI!')
            break
    if escolhaf == 'IMPAR':
        if esceu == 'I':
            print('VOCÊ VENCEU! VAMOS JOGAR NOVAMENTE!')
        if escpc == 'I':
            print('EU VENCI!')
            break
    cont += 1
print(f'MUITO FACIL, NÃO QUERO MAIS JOGAR.. VOCÊ TEVE O TOTAL DE {cont} VITÓRIAS')