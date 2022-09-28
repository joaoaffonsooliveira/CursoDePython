# Conversor de bases
numero = int(input('Digite um número inteiro: '))
base = int(input('''Para qual base você quer convertê-lo? Digite:
[1] Converter para um número binário \n[2] Converter para um número octal
[3] Converter para um númerohexadecimal\n'''))
if base == 1:
    print(f'O número {numero} em binário é equivalente a: {bin(numero)[2:]}')
elif base == 2:
    print(f'O número {numero} em octal é equivalente a: {oct(numero)[2:]}')
else:
    print(f'O número {numero} em hexadecimal é equivalente a: {hex(numero)[2:]}')