# Separando dígitos de um número
n = str(input('Digite um número de 0 a 9999: '))
print(f'O número digitado foi: {n}')
print(f'O número na casa das unidades é: {n[3]}')
print(f'O número na casa das dezenas é: {n[2]}')
print(f'O número na casa das centenas é: {n[1]}')
print(f'O número na casa de milhar é: {n[0]}')



