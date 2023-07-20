num = int(input('Digite um número inteiro qualquer para ser convertido:'))
opc = int(input('Por favor, digite 1 para BINÁRIO, 2 para OCTAL ou 3 para HEXADECIMAL:'))
if opc == 1:
    print(f'O número Binário referente ao número {num} é:')
    print(f'{bin(num)[2:]}')
elif opc == 2:
    print(f'O número Octal referente ao número {num} é:')
    print(f'{oct(num)[2:]}')
elif opc == 3:
    print(f'O número Hexadecimal referente ao número {num} é:')
    print(f'{hex(num)[2:]}')
else:
    print('Por favor, reinicie e faça uma escolha VÁLIDA!')
print('Tenha um bom dia!')
