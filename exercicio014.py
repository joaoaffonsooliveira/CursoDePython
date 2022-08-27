# Conversor de temperatura
n = int(input('Digite uma temperatura em ºC: '))
k = n + 273
f = n*(9/5) + 32

print(f'A temperatura {n}ºC é equivalente a: \nKelvin: {k:.1f}K \nFarenheit: {f:.1f}F')