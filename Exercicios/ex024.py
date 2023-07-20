cidade = str(input('Digite o nome de sua cidade:')).strip()
cidadesplit = cidade.lower().split()
print(f'Sua cidade é {cidade}')
print(f'Ela começa com o nome "Santo"? {"santo"in cidadesplit[0]}')
