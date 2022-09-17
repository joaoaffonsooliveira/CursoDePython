# Primeiro e último nome de uma pessoa
nome = str(input('Digite seu nome completo: ')).strip().title()
nomeDividido = nome.split()
print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é: {nomeDividido[0]}')
print(f'Seu último nome é: {nomeDividido[len(nomeDividido) - 1]}')
# Forma alternativa de mostrar último nome:
print(f'Seu último nome é: {nomeDividido[-1]}')
