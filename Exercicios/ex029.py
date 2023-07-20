from time import sleep
v = int(input('Digite aqui a sua velocidade:'))
m = float(v-80)*7
if v <= 80:
    print(f'Sua velocidade, que era de {v}km/h, estava dentro do limite de velocidade!')
    print('Continue dirigindo com segurança!')
else:
    print(f'Sua velocidade, que era de {v}km/h, excedia o limite de velocidade!')
    print('Uma multa será aplicada de acordo com a velocidade excedida')
    print('CALCULANDO...')
    sleep(3)
    print(f'Sua multa é de R${m:.2f}')
    print('Por favor, dirija com segurança!')
