# Calculador de alistamento no serviço militar
from datetime import date

print('-=-' * 20)
print('CALCULADOR DE ALISTAMENTO MILITAR...')
print('-=-' * 20)

anoDeNascimento = int(input('Digite seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoDeNascimento
print(f'Quem nasceu em {anoDeNascimento} possui {idade} anos em {anoAtual}')
if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para seu alistamento militar.'
          f'Seu alistamento será em {anoAtual + saldo}')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.'
          f'Seu alistamento deveria ter sido feito em {anoAtual - saldo}')
else:
    print(f'Você está na idade de realizar o alistamento militar.')

