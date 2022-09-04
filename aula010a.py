# Aula 10 - Condição if (parte 01)

# Estrutura padrão
time = int(input('Quantos anos tem seu carro?\n'))
input('...')
if time <= 3:
    print('Carro novo')
else:
    print('Carro velho')

# Estrutura alternativa
tempo = int(input('Quantos anos tem seu carro?\n'))
input('...')
print('Carro novo' if tempo <= 3 else 'Carro velho')
