from random import randint
comp = randint(1,100)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == comp:
        acertou = True
    else:
        if jogador > comp:
            print('Menos... Tente mais uma vez!')
        elif jogador < comp:
            print('Mais... Tente mais uma vez!')
print(f'Acertou com {palpites} tentativas!')
