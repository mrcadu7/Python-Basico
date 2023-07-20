sexo = str(input('Por favor digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos! Por favor digite seu sexo [M/F]: ')).strip().upper()[0]
print(f'Seu sexo é {sexo}! Dados cadastrados!')