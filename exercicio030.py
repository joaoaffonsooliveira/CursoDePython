# Paridade de um número

from time import sleep
print('-=-' * 20)
n = int(input('Digite um número e te direi se ele é par ou ímpar: '))
print('-=-' * 20)
print('PROCESSANDO...')
sleep(1.5)
if n % 2 == 0:
    print(f'O número {n} é par')
else:
    print(f'O número {n} é ímpar')