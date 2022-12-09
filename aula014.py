"""
for c in range(1, 11):
    print(c)
print('FIM')
"""
'''
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')

n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('FIM')

r = 'S'
while r == 'S':
    n2 = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] \n')).upper()
print('FIM')
'''
n3 = 1
par = impar = 0
while n3 != 0:
    n3 = int(input('Digite um número: '))
    if n3 % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares')
print('ACABOU')