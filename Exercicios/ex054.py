from datetime import date
c = 0
c2 = 0
atual = date.today().year
for ano in range(1,8):
    idade = int(input(f'Digite o ano em que a {ano}ª pessoa nasceu:'))
    if atual-idade >= 18:
        c = c + 1
    elif atual-idade < 18:
        c2 = c2 + 1
print(f'Das idades apresentadas, apenas {c} atingiram a maioridade enquanto {c2} são menores de idade!')

