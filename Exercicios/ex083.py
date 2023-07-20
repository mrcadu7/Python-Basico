fatiado = []
cont = 0
exp = str(input('Digite uma expressão matemática qualquer:')).strip()
for simb in exp:
    if simb == '(':
        fatiado.append('(')
    elif simb == ')':
        if len(fatiado) > 0:
            fatiado.pop()
        else:
            fatiado.append(')')
            break
if len(fatiado) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está errada')
