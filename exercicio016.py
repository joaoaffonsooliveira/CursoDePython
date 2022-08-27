# Quebrando um número
from math import trunc
n = float(input('Digite um número real: '))
print(f'O número: {n} tem a parte inteira: {trunc(n)}')

# Outra opção seria:
print(f'O número: {n} tem a parte inteira: {int(n)}')
