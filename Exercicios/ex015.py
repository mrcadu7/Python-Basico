d = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos Km rodados?'))
#vd = d*60
#vkm = km*0.15
#vtotal = vd+vkm
v = (d*60)+(km*0.15)
print (f'O valor total a ser pago por {d} dias de aluguel e por {km}Km rodados é de R${v:.2f}')
