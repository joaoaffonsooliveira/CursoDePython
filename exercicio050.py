# Soma apenas numeros pares dos 6 ingressados
soma: int = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} números PARES e a soma entre eles foi: {soma}')

