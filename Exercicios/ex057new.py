sexo =' '
while sexo not in 'MF':
    sexo = str(input('Por favor, digite o seu sexo [M/F]:')).strip().upper()
    if sexo in 'MF':
        print('Muito obrigado!')
    else:
        print('Por favor digite uma opção válida!')
print('FIM')