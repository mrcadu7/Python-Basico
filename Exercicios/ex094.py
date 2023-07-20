pessoas = {}
lista = []
mulheres = []
idade = []
soma = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: '))
    while pessoas['sexo'] not in 'mfMF':
        if pessoas['sexo'] in 'mfMF':
            break
        else:
            print('Digite uma opção válida')
            pessoas['sexo'] = str(input('Sexo [M/F]: '))
    if pessoas['sexo'] in 'fF':
        mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    lista.append(pessoas.copy())
    while True:
        resp = str(input('DESEJA CONTINUAR? [S/N]'))
        if resp in 'sSnN':
            break
        else:
            print('Digite uma opção válida')
    if resp in 'nN':
        break
print(f'Foram cadastradas um total de {len(lista)} pessoas')
print(f'A média de idade do grupo é: {soma/len(lista):.2f} anos')
print(f'As mulheres cadastradas são: {mulheres}')
print('As pessoas que estão com idade acima da média são:')
for p in lista:
    if p['idade'] > soma/len(lista):
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<ENCERRADO>>>')
