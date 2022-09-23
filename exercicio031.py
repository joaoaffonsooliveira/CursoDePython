# Calculador de viagens

from time import sleep

print('-=-' * 20)
n = float(input('Sua viagem será de quantos Km? '))
print('-=-' * 20)
print('PROCESSANDO...')
sleep(1.5)
if n <= 200:
    print(f'Sua passagem custará: {(0.5 * n):.2f}')
else:
    print(f'Sua passagem custará: {(0.45 * n):.2f}')

# Outra forma de fazer:
'''
d = float(input('Qual é a distância da sua viagem? '))
if d <= 200:
    preco = d * 0.5
else:
    preco = d * 0.45
print(f'Sua passagem custará: {preco:.2f}')
'''