totm = 0
idadev = 0
nomev = ''
totidade = 0
for p in range (1,5):
    print(f'<><><><> {p}ª PESSOA <><><><>')
    nome = str(input('NOME:')).strip()
    idade = int(input('IDADE:'))
    sexo = str(input('SEXO [M/F]:'))
    totidade += idade
    if p == 1 and sexo in 'Mm':
        idadev = idade
        nomev = nome
    if sexo in 'Mm' and idade > idadev:
        idadev = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
media = totidade/4
print(f'A média de idade do grupo é: {media}')
print(f'O homem mais velho possui {idadev} anos e se chama {nomev.capitalize()}')
print(f'Dentro do grupo, {totm} mulheres estão abaixo dos 20 anos!')
