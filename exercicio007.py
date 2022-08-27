# Ler duas notas de um aluno e dar sua média aritmética
aluno = input('Digite o nome do aluno: ')
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print(f'A média do {aluno} é: {m:.2f}')
