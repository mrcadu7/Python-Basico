cond = 'S'
tot = soma = maior = menor = 0
while cond == 'S':
    n = int(input('Digite aqui um número inteiro:'))
    tot += 1
    soma += n
    if tot == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cond = str(input('Gostaria de digitar outro número [S/N]?')).strip().upper()
print(f'Você digitou {tot} números e a média deles é {soma/tot}, com o maior valor sendo {maior} e o menor sendo {menor}')



