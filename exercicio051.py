# Contagem em uma PA

primeiro = int(input('Ingresse o primeiro termo da PA: '))
razao = int(input('Ingresse o valor da razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' -> ')
print('FIM')
