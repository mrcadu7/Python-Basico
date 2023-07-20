val = float(input('Digite aqui o valor da casa desejada: R$'))
sal = float(input('Digite aqui o seu salário mensal: R$'))
tempo = int(input('Quantos anos de financiamento?'))
mens = tempo*12
vparc = val/mens
porc = sal*30/100
print('De acordo com nossas contas:')
if vparc > porc:
    print('Infelizmente o empréstimo foi NEGADO, devido as parcelas serem superiores a 30% de seu salário atual')
    print(f'A mensalidade a ser paga seria de R${vparc:.2f} e 30% de seu salário é R${porc:.2f}')
else:
    print('Seu pedido de empréstimo foi ACEITO!')
    print(f'A mensalidade a ser paga é {mens} parcelas de R${vparc:.2f}')
print('Desejamo-lhe um ótimo dia!')
