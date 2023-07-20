cont = n = soma = 0
while True:
    n = int(input('Por favor digite um número:'))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} com o somatório de {soma}')

