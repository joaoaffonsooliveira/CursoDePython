# Catetos e hipotenusa
from math import hypot
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hip = hypot(co, ca)
print(f'A hipotenusa de um triângulo retângulo de lados {ca:.2f} e {co:.2f} vale: {hip:.2f}')