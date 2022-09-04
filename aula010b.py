# Parte prática - Condição if (Parte 01)
nome = str(input('Qual é o seu nome?\n')).strip()
nomeMaiusculo = nome.upper()
if nomeMaiusculo == 'GUSTAVO':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia! {nome.title()}')