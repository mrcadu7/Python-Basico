n = 1
while True:
    num = int(input('Digite o número multiplicador de sua tabuada:'))
    if num < 0:
        break
    while n <= 10:
        print(f'{num} X {n} = {num * n}')
        n += 1
    n = 0
print('fim')
