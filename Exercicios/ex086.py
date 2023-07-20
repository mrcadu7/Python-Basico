matriz = [[[],[],[]], [[],[],[]], [[],[],[]]]
for c in range(0,3):
    matriz[0][c-1].append(int(input(f'Digite um valor para [0, {c}]:')))
for c in range(0,3):
    matriz[1][c-1].append(int(input(f'Digite um valor para [1, {c}]:')))
for c in range(0,3):
    matriz[2][c-1].append(int(input(f'Digite um valor para [2, {c}]:')))
print(matriz[0][0], matriz[0][1], matriz[0][2])
print(matriz[1][0], matriz[1][1], matriz[1][2])
print(matriz[2][0], matriz[2][1], matriz[2][2])
