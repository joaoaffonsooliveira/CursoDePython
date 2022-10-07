# Estrutura de repetição FOR
for c in range(1,6): # Conta de 1 a 5
    print(c)
input('FIM...')
for c in range(0, 5): # Conta de 1 a 4
    print(c)
input('FIM...')
for c in range(6, 0, -1): # Conta de trás para frente
    print(c)
input('FIM...')
for c in range(0, 10, 2): # de 0 a 10 de 2 em 2
    print(c)
input('FIM...')
inicio = int(input('Digite um número de início: '))
fim = int(input('Digite um número de fim: '))
passo = int(input('Digite um número que represente de quanto em quanto quer pular: '))
for c in range(inicio, fim+1, passo):
    print(c)
input('FIM...')