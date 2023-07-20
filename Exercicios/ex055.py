maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Digite aqui o peso da {p}ª pessoa:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
print(f'Dos pesos analisados o maior peso é {maior}Kg, enquanto o menor peso é {menor}Kg')
