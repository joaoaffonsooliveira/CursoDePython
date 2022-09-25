nome = input('Digite seu nome: ')

# Primeira forma de digitar (formato que mais gosto)
print(f'Olá \033[4;34m{nome}\033[m, é um prazer te conhecer!')

# Segunda forma de digitar
print('É um prazer te conhecer,\033[4;34m',nome,'\033[m')

# Terceira forma de digitar
print('Olá {}{}{}, é um prazer te conhecer!'.format('\033[4;34m', nome, '\033[m'))

