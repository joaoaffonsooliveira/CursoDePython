# Condições aninhadas
nome = str(input('Digite seu nome: ')).strip().capitalize()
nomeMaiusculo = nome.upper()
if nomeMaiusculo == 'GUSTAVO':
    print(f'Que nome bonito, {nome}')
elif nomeMaiusculo == 'PEDRO':
    print(f'Que nome normal, {nome}')
elif nomeMaiusculo in 'ANA CLÁUDIA JÉSSICA E JULIANA':
    print('Belo nome feminino!')
else:
    print(f'Que nome estranho, {nome}')