# Transformação de strings
frase = 'Curso em Vídeo Python'
# Substituindo 'Python' por 'Android'
print(frase.replace('Python', 'Android'))
# Colocando em maiúsculo tudo
print(frase.upper())
# Colocando tudo em minúsculo
print(frase.lower())
# Capitalize
print(frase.capitalize())
# Title dá um capitalize em cada palavra
print(frase.title())
# Strip remove espaços inúteis no início e fim das palavras
novaFrase = '  Olá mundo!   '
print(novaFrase)
print(novaFrase.strip())
# rStrip remove espaços inúteis somente na direita
novaFrase2 = '  Olá mundo 2!   '
print(novaFrase2)
print(novaFrase2.rstrip())
# lStrip remove espaços inúteis somente na esquerda
novaFrase3 = '  Olá mundo 3!   '
print(novaFrase3)
print(novaFrase3.lstrip())
