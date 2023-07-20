n = cont = soma = 0
n = int(input('Digite aqui um número (999 PARA PARAR):'))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite aqui um número (999 PARA PARAR):'))
print(f'Foram digitados um total de {cont} números com o somatório {soma}!')
