f = str(input('Digite uma frase:')).strip().upper()
p = f.split()
j = ''.join(p)
inv = ''
for l in range(len(j)-1, -1, -1):
    inv += j[l]
if inv == j:
    print('Sua frase é um palíndromo!')
else:
    print('Sua frase não é um palíndromo!')
