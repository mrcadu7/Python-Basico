num = int(input('Digite um numero de 0 a 9999:'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
#n = str(num)
print(f'Seu numero é {num}')
print(f'A unidade do seu número é: {u}')
print(f'A dezena do seu número é: {d}')
print(f'A centena do seu número é: {c}')
print(f'O milhar do seu número é: {m}')
