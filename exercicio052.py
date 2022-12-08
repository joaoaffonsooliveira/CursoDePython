# Números primos
n = int(input('Digite um número: '))
for c in range(1, n + 1, 1):
    if n % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')