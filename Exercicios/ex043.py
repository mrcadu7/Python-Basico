peso = float(input('Digite aqui o seu peso:'))
altura = float(input('Digite aqui a sua altura:'))
imc = peso/(altura*altura)
print(f'Seu imc é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal!')
elif 25 <= imc < 30:
    print('Você está com sobrepeso!')
elif 30 <= imc < 40:
    print('Você está com obesidade!')
elif imc >= 40:
    print('Você está com obesidade mórbida!')
print('Tenha uma boa tarde!')
