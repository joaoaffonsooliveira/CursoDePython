# Media escolar
from time import sleep
aluno = str(input('Digite o nome completo do aluno: '))
nota1 = float(input(f'Digite a primeira nota de {aluno}: '))
nota2 = float(input(f'Digite a segunda nota de {aluno}: '))
media = (nota1 + nota2) / 2
if media < 5:
    print(f'{aluno} está aabixo da média.\nREPROVADO!')
elif media >= 7:
    print(f'{aluno} está acima da média.\nAPROVADO!')
else:
    print(f'{aluno} possui média entre 5.0 e 6.9.\nRECUPERAÇÃO!')