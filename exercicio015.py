# Aluguel de carros
c = input('Qual foi o modelo do carro alugado? ')
d = int(input(f'Por quantos dias o {c} foi alugado? '))
km = int(input(f'Quantos Km o {c} rodou nesse período de {d} dias? '))
p = 60 * d + 0.15 * km
print(f'O preço do aluguel do {c} será de: R${p:.2f}')