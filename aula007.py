n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
exp = n1**n2
# Melhor forma de escrever para mim
print(f'A soma é {s}, a multiplicação é {m}, a divisão é {d:.3f}')
print(f'A divisão inteira é {di} e a exponenciação é {exp}')

# Outra forma de escrever
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s,m,d))
print('A divisão inteira é {} e a exponenciação é {}'.format(di, exp))

# Quebra de linha e não pular linhas
print('A soma é {},\na multiplicação é {},\na divisão é {:.3f}'.format(s,m,d), end=' ')
print('A divisão inteira é {} e a exponenciação é {}'.format(di, exp))