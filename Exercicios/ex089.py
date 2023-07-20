ficha = []
cont = 0
while True:
    nome = str(input('NOME: '))
    nota1 = float(input('NOTA 1: '))
    nota2 = float(input('NOTA 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    cont += 1
    esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    while esc not in 'SN':
        print('OPÇÃO INVALIDA')
        esc = str(input('DESEJA CONTINUAR? [S/N]')).strip().upper()
    if esc == 'N':
        break
print('=-'*15)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
for f in range(cont):
    print(f'{f:<4}{ficha[f][0]:<10}{ficha[f][2]:>8}')
print('=-'*15)
while True:
    n = int(input(f'Mostrar notas de qual aluno? (999 interrompe):'))
    if n == 999:
        break
    print(f'Mostrando as notas de {ficha[n][0]}: {ficha[n][1]}')
    print('=-' * 15)
print('Obrigado!')