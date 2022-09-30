# Calculadora IMC
from time import sleep
print('-=-' * 20)
print('CALCULADORA DE IMC...')
print('-=-' * 20)
nome = str(input('Qual é o seu nome? ')).strip()
peso = float(input('Quanto você pesa? '))
altura = float(input('Quanto de altura você possui? '))
imc = peso / (altura ** 2)
print('-=-' * 20)
print('PROCESSANDO...')
print('-=-' * 20)
sleep(2)
if imc < 18.5:
    print(f'{nome}, você está ABAIXO do peso ideal')
elif imc >= 18.5 and imc < 25:
    print(f'{nome}, você está no peso IDEAL')
elif imc >= 25 and imc < 30:
    print(f'{nome}, você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'{nome}, você está OBESO')
else:
    print(f'{nome}, você está com OBESIDADE MÓRBIDA')