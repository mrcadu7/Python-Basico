def fatorial(n, show=False):
    """
    -> Calcula o FATORIAL de um número.
    :param n: O numero a ser calculado
    :param show: (opcional) Mostar OU NÃO a conta.
    :return: O valor fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


#programa principal
print(fatorial(5, show=True))