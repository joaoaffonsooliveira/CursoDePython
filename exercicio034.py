# Calculando aumentos múltiplos
s = float(input('Digite o valor do seu salário atual: '))
if s > 1250:
    aumento = 0.10 * s
else:
    aumento = 0.15 * s
print(f'O seu salário receberá um aumento de R${aumento:.2f}, seu salário passará a ser R${(aumento + s):.2f} ')