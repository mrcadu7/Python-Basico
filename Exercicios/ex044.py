preco = float(input('Digite qual o preço do seu produto:'))
dinh = preco - (preco*10/100)
cart = preco - (preco*5/100)
cart2x = preco
cart3x = preco + (preco*20/100)
cond = int(input('''Digite 1 para pagamento a vista com dinheiro \n2 para a vista com cartão \n3 para parcelar em 2x
4 para parcelar em 3x ou mais:'''))
print(f'O valor do seu produto é R${preco:.2f}')
if cond == 1:
    print('Você escolheu pagamento a vista em espécie!')
    print(f'Nesta condição de pagamento o preço total fica a R${dinh:.2f}')
elif cond == 2:
    print('Você escolheu pagamento a vista pelo cartão!')
    print(f'Nesta condição de pagamento o preço total fica a R${cart:.2f}')
elif cond == 3:
    print('Você escolheu parcelar em até 2x!')
    print(f'Nesta condição de pagamento o preço total fica a R${cart2x:.2f}')
elif cond == 4:
    print('Você escolheu parcelar em 3x ou mais!')
    print(f'Nesta condição de pagamento o preço total fica a R${cart3x:.2f}')
else:
    print('Por favor, escolha uma condição válida e tente novamente!')
print('Tenha um bom dia!')
