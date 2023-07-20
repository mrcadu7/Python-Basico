from datetime import date
ano = int(input('Digite aqui o ano de seu nascimento para o classificarmos na categoria correta:'))
idade = date.today().year - ano
print(f'Você tem {idade} anos!')
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade == 20:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')
print ('Tenha um bom dia!')
