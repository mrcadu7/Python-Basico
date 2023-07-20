cont = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',\
'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
while True:
    valor = int(input('Digite um número de 0 a 20:'))
    if valor >= 0 and valor <= 20:
        break
print(f'Você digitou o número {cont[valor]}')