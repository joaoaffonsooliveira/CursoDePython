# Maior e menor valores
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

# Testando quem é o menor valor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O menor valor é: {menor}')

# Testando quem é o maior valor:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior valor é: {maior}')

# Testando se os valores são iguais
if n1 == n2 == n3:
    print('Os valores digitados são iguais')