listagem = ('Pão', 1.50, 'Queijo', 5.50, 'Açucar', 6.75,
            'Margarina', 8, 'Frango', 15, 'Tempero', 1.50)
print('~='*20)
print(f'{"LISTAGEM DE PREÇOS":^35}')
print('~='*20)
for l in range(0, len(listagem)):
    if l%2 == 0:
        print(f'{listagem[l]:.<30}', end=' ')
    else:
        print(f'R$ {listagem[l]:>5.2f}')
"""for i in listagem:
    if type(i) is str:
        print(f'{i:.<32}', end='')
    else:
        print(f'R$ {i:>5.2f}')
print('--'*20)"""
