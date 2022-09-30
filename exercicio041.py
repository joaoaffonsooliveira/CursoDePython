# Classificando atletas
print('-=-' * 20)
print('CLASSIFICANDO ATLETAS DE ACORDO COM SUA IDADE...')
print('-=-' * 20)
nomeAtleta = str(input('Digite o nome do atleta: '))
idade = int(input(f'Digite a idade do atleta {nomeAtleta}: '))
if idade <= 9:
    print('Atleta MIRIM')
elif idade > 9 and idade <= 14:
    print('Atleta INFANTIL')
elif idade > 14 and idade <= 19:
    print('Atleta JUNIOR')
elif idade == 20:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')