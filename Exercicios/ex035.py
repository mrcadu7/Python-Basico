from time import sleep
print('Por favor, nos informe o segmento de 3 retas para verificarmos se podemos criar um triângulo')
r1 = float(input('Digite o segmento da primeira reta:'))
r2 = float(input('Digite o segmento da segunda reta:'))
r3 = float(input('Digite o segmento da terceira reta:'))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print(f'Segundo as condições de existência de um triângulo, suas retas {r1},{r2} e {r3} formam um triângulo!')
else:
    print(f'Segundo as condições de existência de um triângulo, suas retas {r1},{r2} e {r3} não formam um triângulo!')
print('As condições de existência são: A soma de dois lados é SEMPRE maior que o terceiro lado!')
