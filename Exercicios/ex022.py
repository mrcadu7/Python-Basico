nomec = str(input('Digite aqui o seu nome completo:')).strip()
nomep = nomec.split()
print(f'Seu nome em caixa alta é: {nomec.upper()}')
print(f'Seu nome em caixa baixa é: {nomec.lower()}')
print(f'Seu nome possui o total de {len(nomec.replace(" ",""))} letras')
print(f'Seu primeiro nome é {nomep[0]} e possui o total de {len(nomep[0])} letras')
