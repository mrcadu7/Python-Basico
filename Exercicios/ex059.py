n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))
o = 0
while o != 5:
        print('Por favor escolha uma das opções abaixo: \n[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NUMEROS'
              '\n[5] ENCERRAR')
        o = int(input('Qual sua opção? '))
        if o == 1:
            print(f'A soma dos valores {n1} e {n2} é igual a {n1+n2}')
        elif o == 2:
            print(f'A multiplicação entre os valores {n1} e {n2} é igual a {n1*n2}')
        elif o == 3:
            if n1>n2:
                print(f'O primeiro número ({n1}) é maior que o segundo ({n2})!')
            elif n1==n2:
                print(f'Os dois números possuem valor {n1}, portanto são iguais!')
            else:
                print(f'O segundo número ({n2}) é maior que o primeiro ({n1})!')
        elif o == 4:
            print('Por favor, diga seus novos números abaixo!')
            n1 = int(input('Digite um número:'))
            n2 = int(input('Digite mais um número:'))
            print(f'Seus novos números são {n1} e {n2}')
        elif o == 5:
            print('FINALIZANDO...')
        else:
            print('Opção inválida, tente novamente!')
        print('+='*20)
print('OBRIGADO PELA PREFERÊNCIA!')