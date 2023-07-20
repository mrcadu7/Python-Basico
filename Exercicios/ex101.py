def voto(nasc):
    from datetime import date #eu não tinha me ligado no escopo
    idade = date.today().year - nasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        return 'NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 70:
        return 'VOTO OPCIONAL!'
    else:
        return 'VOTO OBRIGATÓRIO!'


#Programa principal
n = int(input('EM QUAL ANO VOCÊ NASCEU:'))
print(voto(n))