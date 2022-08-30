# Separando dígitos de um número
# Forma matemática de resolver o problema
num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'unidade:  {u}')
print(f'dezena:  {d}')
print(f'centena:  {c}')
print(f'milhar:  {m}')


# O problema poderia ser resolvido dessa forma com o incremento de uma estrutura de repetição que veremos futuramente.
"""
n = str(input('Digite um número de 0 a 9999: '))
print(f'O número digitado foi: {n}')
print(f'O número na casa das unidades é: {n[3]}')
print(f'O número na casa das dezenas é: {n[2]}')
print(f'O número na casa das centenas é: {n[1]}')
print(f'O número na casa de milhar é: {n[0]}')
"""



