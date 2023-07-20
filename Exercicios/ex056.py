totm = 0
sidade = 0
midade = 0
mhomem = 0
nomevelho = ''
for p in range (1,5):
    print(f'=+=+=+ {p}ª PESSOA =+=+=+')
    nome = str(input(f'Nome:')).strip()
    idade = int(input(f'Idade:'))
    sexo = str(input(f'Sexo [M/F]:')).strip()
    sidade += idade
    if p == 1 and sexo in 'Mm':
        mhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > mhomem:
        mhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totm += 1
midade = sidade / 4
print(f'A média de idade do grupo é de {midade} anos!')
print(f'O nome do homem mais velho é {nomevelho.capitalize()}!')
print(f'E o grupo possui {totm} mulheres abaixo dos 20 anos!')
