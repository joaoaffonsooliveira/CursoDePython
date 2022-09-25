# Analisador de triângulos v1.0
print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 20)

c1 = int(input('Digite o primeiro comprimento: '))
c2 = int(input('Digite o segundo comprimento: '))
c3 = int(input('Digite o terceiro comprimento: '))

# Para existir triângulo é preciso que um dos lados seja menor que a soma dos outros dois.
if c1 < (c2 + c3) and c2 < (c1 + c3) and c3 < (c1 + c2):
    print('É possível existir um triângulo com os esses tamanhos de segmentos')
else:
    print('Não é possível existir um triângulo com esses tamanhos de segmentos')
