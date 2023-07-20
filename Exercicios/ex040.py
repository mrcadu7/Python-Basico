n1 = float(input('Por favor digite o valor de sua primeira nota:'))
n2 = float(input('Por favor digite o valor de sua segunda nota:'))
m = (n1+n2)/2
if m < 5:
    print(f'Infelizmente a sua média foi {m:.1f} e você foi REPROVADO!')
elif m >= 7:
    print(f'Sua média foi {m:.1f} e você foi APROVADO! PARABÉNS!')
else:
    print(f'Sua média é {m:.1f} e você precisará fazer RECUPERAÇÃO! BONS ESTUDOS')
