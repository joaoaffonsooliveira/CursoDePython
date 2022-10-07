#Somando ímpares múltiplos de 3
soma = 0
print('SOMA DE NÚMEROS ÍMPARES MÚLTIPLOS DE 3 ENTRE 1 E 500')
for n in range(1, 501):
    if n % 2 != 0 and n % 3 == 0:
        soma = soma + n
print(f'A soma entre números ímpares múltiplos de 3 entre 1 e 500 é: {soma}')