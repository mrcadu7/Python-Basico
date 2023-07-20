n = input('Digite algo:')
'''if n == 'True':
    n = {\033[1;31m}
else:
    n = {\033[1;30m}'''
print('O tipo primitivo deste valor é:',(type(n)))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada?', n.istitle())
