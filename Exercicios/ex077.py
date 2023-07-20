palavras = ('palavra', 'salgado', 'dislexia', 'mamado', 'sonegado',
            'tambique', 'sexo', 'putaria', 'amor', 'imposto',
            'macaco', 'saxofonista', 'cintaralho')
for p in palavras:
    print(f'\nNa palavra {p} temos as vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

