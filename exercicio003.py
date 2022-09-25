# Somando dois números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print(f'A soma entre \033[1;31m{n1}\033[m e \033[1;31m{n2}\033[m é: \033[1;31m{s}\033[m')

# Outra forma de escrever:
'''
print('A soma entre {} e {} é: {}'.format(n1, n2, s))
'''