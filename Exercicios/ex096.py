def area(larg, comp):
    a = larg*comp
    print(f'A área de um terreno {larg}x{comp} é {a}m².')


#Programa principal
print('CONTROLE DE TERRENOS!')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
