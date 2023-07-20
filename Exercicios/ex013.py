n = float(input('Digite o valor de seu salário atual para verificarmos o valor do seu reajuste de 15%:'))
r = n*(15/100)
t = n+r
print (f'Seu salário atualizado possui o valor de R${t:.2f}')
