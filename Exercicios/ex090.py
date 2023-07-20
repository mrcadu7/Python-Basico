alunos = {}
alunos['nome'] = str(input('Nome:'))
alunos['media'] = float(input(f'Média de {alunos["nome"]}:'))
if alunos['media'] >= 7:
    alunos['situacao'] = 'aprovado'
elif 5 <= alunos['media'] < 7:
    alunos['situacao'] = 'recuperação'
else:
    alunos['situacao'] = 'reprovado'
for k, v in alunos.items():
    print(f'{k} é igual a {v}')


