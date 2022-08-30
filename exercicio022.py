# Analisador de textos
nome = str(input('Digite seu nome completo: '))
nomeSemEspacos = nome.replace(' ', '')
nomeDividido = nome.split()
print(f'Seu nome completo é: {nome}')
print(f'Seu nome completo com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome completo com todas as letras minúsculas é: {nome.lower()}')
print(f'Seu nome completo em capitalize é: {nome.capitalize()}')
print(f'Seu nome completo em title é: {nome.title()}')
print(f'Seu nome tem {len(nomeSemEspacos)} letras')
print(f'Seu primeiro nome possui {len(nomeDividido[0])} letras')

# Outra forma de realizar o desafio:
"""
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print(f'Seu nome completo com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome completo com todas as letras minúsculas é: {nome.lower()}')
print(f'Seu nome completo em capitalize é: {nome.capitalize()}')
print(f'Seu nome completo em title é: {nome.title()}')
print(f'Seu nome tem {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
"""

