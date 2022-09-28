# Comparando números
print('-=-' * 20)
print('COMPARADOR DE NÚMEROS...')
print('-=-' * 20)
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print(f'O número {num1} é MAIOR que o número {num2}')
elif num1 == num2:
    print(f'O número {num1} é IGUAL ao número {num2}')
else:
    print(f'O número {num1} é MENOR que o número {num2}')