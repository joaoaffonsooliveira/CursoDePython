# Possibilidade de triangulos V2.0
from time import sleep
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS V2.0...')
print('-=-' * 20)
lado1 = float(input('Digite o comprimento do primeiro lado: '))
lado2 = float(input('Digite o comprimento do segundo lado: '))
lado3 = float(input('Digite o comprimento do terceiro lado: '))
sleep(1)
print('-=-' * 20)
print('PROCESSANDO...')
print('-=-' * 20)
sleep(2)

# Condição de existência de um triângulo: um lado deve ser menor que a soma dos outros dois
if lado1 < (lado2 + lado3) and lado2 < (lado1 + lado2) and lado3 < (lado1 + lado2):
    print('É possível haver triângulo')
    if lado1 == lado2 == lado3:
        print('O triângulo é do tipo equilátero')
    elif lado1 != lado2 != lado3:
        print('O triângulo é do tipo escaleno')
    else:
        print('O triângulo é do tipo isósceles')
else:
    print('Não é possível existir triângulo com esses comprimentos de lados')