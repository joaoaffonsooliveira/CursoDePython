# Gerenciador de pagamentos
print('-=-' * 20)
print('GERENCIADOR DE PAGAMENTOS...')
print('-=-' * 20)
produto = str(input('Que produto você deseja comprar? '))
precoNormal = float(input('Quanto custa esse produto? '))
condicaoPagamento = int(input('Digite de que forma você pagará:\n[1] À vista em dinheiro ou cheque\n'
                          '[2] À vista no cartão\n[3] Em até 2x no cartão\n[4] 3x ou mais no cartão\n'))
if condicaoPagamento == 1:
    precoComDesconto = precoNormal * 0.90
    print(f'O preço do {produto} com desconto será: {precoComDesconto}')
elif condicaoPagamento == 2:
    precoComDesconto = precoNormal * 0.95
    print(f'O preço do {produto} com desconto será: {precoComDesconto}')
elif condicaoPagamento == 3:
    print(f'O preço do {produto} será: {precoNormal}')
else:
    precoComJuros = precoNormal * 1.20
    print(f'O preço do {produto} será: {precoComJuros}')