# Verificando as primeiras letras de um texto
cid = input('Digite o nome de alguma cidade: ').strip()
print(f'O nome da cidade digitada pcomeça com "Santo"? {cid[:5].upper() == "SANTO"}')
