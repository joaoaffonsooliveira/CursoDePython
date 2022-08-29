# Divisão em strings
frase = 'Curso em Vídeo Python'
# Cada palavra da lista inicial que foi quebrada vira uma nova lista
fraseCortada = frase.split()
print(fraseCortada)
# Unindo as palavras cortadas adicionando '-' entre elas
print('-'.join(fraseCortada))