# Verificando as primeiras letras de um texto
c = input('Digite o nome de alguma cidade: ')
# Divide o nome da cidade em uma lista de nomes
cDividido = c.split()
print(f'A cidade digitada começa com "Santo" em seu nome? {("Santo" in cDividido[0])}')