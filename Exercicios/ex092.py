from datetime import datetime
cadastro = {}
cadastro['nome'] = str(input('NOME: '))
nasc = int(input('ANO DE NASCIMENTO: '))
cadastro['idade'] = datetime.now().year - nasc
cadastro['ctps'] = int(input('CARTEIRA DE TRABALHO: (0 CASO NÃO TENHA): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('ANO DE CONTRATAÇÃO: '))
    cadastro['salario'] = float(input('SALÁRIO: R$'))
    cadastro['aposentadoria'] = cadastro['idade'] + ((cadastro['contratação'] + 35) - datetime.now().year)
print(cadastro)
for v, k in cadastro.items():
    print(f'{v} tem o valor {k}')
