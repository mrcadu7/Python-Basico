n = int(input('Digite aqui a distância de sua viagem em Km para o calculo do valor correto:'))
p = float(n*0.50)
l = float(n*0.45)
if n <= 200:
    print(f'Sua viagem está estipulada em cerca de R${p:.2f}')
else:
    print(f'Sua viagem está estipulada em cerca de R${l:.2f}')
print('Tenha uma boa viagem!')
