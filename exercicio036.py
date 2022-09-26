# Aprovando empréstimo
print('-=-' * 20)
print('Empréstimo para financiamento de uma casa')
print('-=-' * 20)

valorCasa = float(input('Quanto custará a casa que você deseja financiar? '))
salario = float(input('Qual é o valor do seu salário? '))
tempoPagamento = int(input('Em quantos anos você pagará a casa? '))
prestacao = (valorCasa / (tempoPagamento * 12))
valorLimite = 1.30 * salario

print(f'Para pagar uma casa de R${valorCasa:.2f} em {tempoPagamento} anos, ', end='')
print(f'a prestação será de {prestacao:.2f}')

if prestacao <= valorLimite:
    print('Lamentamos, porém seu empréstimo foi NEGADO!')
else:
    print('Parabéns, seu empréstimo foi CONCEDIDO!')