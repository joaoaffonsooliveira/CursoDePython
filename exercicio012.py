# Ler produto e mostrar preço com 5% de desconto
p = input('Qual é o produto que você deseja comprar? ')
n = int(input('Escreva o valor desse produto: '))
pa = n*0.95

print(f'O preço do produto "{p}" com 5% de desconto é: R${pa:.2f}')
