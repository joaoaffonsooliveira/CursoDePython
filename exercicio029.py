from time import sleep
n = float(input('Qual é a velocidade atual do carro? '))
print('PROCESSANDO...')
sleep(2)
if n <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! você excedeu o limite de velocidade permitido que é de 80 Km/h')
    print(f'Você deve pagar uma multa de R${(n - 80) * 7:.2f}')