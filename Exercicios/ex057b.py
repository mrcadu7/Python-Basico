s = ' '
while s not in 'MF':
    s = str(input('POR FAVOR DIGITE SEU SEXO [M/F]:')).strip().upper()
    if s in 'MF':
        print('Obrigado!')
    else:
        print('Por favor, escolha uma opção válida!')
print('FIM')
