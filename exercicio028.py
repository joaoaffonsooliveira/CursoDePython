# Jogo da advinhação

import random
from time import sleep
print('-=-' * 15)
print('Estou pensando em um número entre 0 e 5')
print('-=-' * 15)
n1 = random.randint(0, 5)
n2 = float(input('Qual número entre 0 e 5 você acha que o computador selecionou?\n'))
print('PROCESSANDO...')
sleep(2)
if n1 == n2:
    print('Parabéns, você acertou!')
else:
    print(f'Infelizmente você errou! O computador escolheu: {n1}\n')

# Poderia usar random.uniform(0, 5) para gerar números aleatórios com ponto flutuante