import random
a = str(input('Digite o nome do primeiro aluno para o sorteio:'))
b = str(input('Digite o nome do segundo aluno para o sorteio'))
c = str(input('Digite o nome do terceiro aluno para o sorteio'))
d = str(input('Digite o nome do quarto aluno para o sorteio'))
lista = [a, b, c, d]
sort = random.choice(lista)
print(f'O aluno sorteado aleatóriamente para limpar o quadro é {sort}')

