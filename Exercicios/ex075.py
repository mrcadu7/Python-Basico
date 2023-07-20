valor = (int(input('Digite um número:')), int(input('Digite um segundo número:')),
int(input('Digite um terceiro número:')), int(input('Digite um ultimo número:')))
print('Os valores digitados foram:', end=' ')
for v in valor:
    print(f'{v}', end=' ')
print(f'\nO valor nove apareceu {valor.count(9)} vezes')
if 3 in valor:
    print(f'O 3 foi digitado pela primeira vez na {valor.index(3)+1}ª pergunta')
else:
    print('O 3 não foi digitado nenhuma vez')
print(f'Os números pares digitador foram', end=' ')
for v in valor:
    if v%2 == 0:
        print(v, end=' ')

