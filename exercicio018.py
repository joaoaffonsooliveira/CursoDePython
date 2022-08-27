# Seno, cosseno e tangente
from math import radians, sin, cos, tan
a = float(input('Digite um ângulo qualquer: '))
rad = radians(a)
print(f'O seno, cosseno e tangente do ângulo {a} são: \nSeno: {sin(rad):.2f} \nCosseno: {cos(rad):.2f} \nTangente: {tan(rad):.2f}')
