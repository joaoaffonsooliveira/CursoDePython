# Analisando strings
# Calcular quantidade de caracteres (espaços na memória)
frase = 'Curso em Vídeo Python'
print(len(frase))
# Calcular quantos 'o' existem dentro da frase
print(frase.count('o'))
# Calcular quantos 'o' existem dentro do range estabelecido
print(frase.count('o', 0, 13))
# Imprimir na tela em qual 'casa' começa o 'deo'
print(frase.find('deo'))
# Retorna -1 porque 'Android' não há na sentença
print(frase.find('Android'))
# Retorna True
print('Curso' in frase)