# Ler salário e aplicar algum percentual de aumento
f = input('Digite o nome do funcionário: ')
s = int(input(f'Digite o valor do salário de {f} atualmente: '))
pa = int(input(f'Digite o percentual de aumento salarial que {f} receberá: '))
ns = s * (pa/100 + 1)
print(f'O salário de {f} com {pa}% de aumento passará a ser: R${ns:.2f}')

