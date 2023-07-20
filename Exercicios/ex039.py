from datetime import date
atual = date.today().year
nasc = int(input('Por favor, digite o ano de seu nascimento:'))
idade = atual-nasc
if idade == 18:
    print(f'Você está na idade correta para os alistamento militar!')
elif idade <= 17:
    print(f'Você ainda não pode se alistar, apenas em {18-idade} anos no ano de {atual+(18-idade)}')
elif idade >= 19:
    print(f'Você está atrasado no alistamento em {idade-18} anos! O ano correto foi {atual-(idade-18)}')
    print('procure a junta militar mais próxima!')
print('TENHA UM ÓTIMO DIA!')
print('Brasil acima da minha pica, Meu pau acima de todos!')
