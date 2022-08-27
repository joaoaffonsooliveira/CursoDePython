# Aula 008
'''
import math
num = int(input('Digite um número: '))

raiz = math.sqrt(num)
print(f'A raíz de {num} é igual a {raiz:.2f}')

# Outra forma de escrever
print(f'A raíz de {num} é igual a {math.sqrt(num):.2f}')
'''

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raíz de {num} é igual a {floor(raiz):.2f}')


