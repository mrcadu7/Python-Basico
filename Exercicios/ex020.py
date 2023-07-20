import random
a = str(input('Primeiro Aluno:'))
b = str(input('Segundo Aluno:'))
c = str(input('Terceiro Aluno'))
d = str(input('Quarto Aluno'))
lista = [a, b, c, d]
random.shuffle(lista)
print (f'A ordem para apresentação dos trabalhos será {lista}')
