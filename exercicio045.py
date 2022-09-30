# Game Pedra Papel tesoura
from os import system
from datetime import date
import random
import platform
autor = "Joao Affonso"

so = platform.system()
if so == "Linux":
    s = "clear"
else:
    s = "cls"

hoje = date.today()
dia = hoje.day
mes = hoje.month
ano = hoje.year

system(s)

print("Autor: "+f" {autor}".rjust(100, "-"))
print("Data: "+f" {dia}/{mes}/{ano}".rjust(100, "-"))

# Unicode Emojis: op[0] es piedra op[1] es papel y op[2] es tijera
op = ["\U0000270A", "\U0001F91A", "\U0000270C"]
e1 = int(input('Vamos jogar Jo Ken Po!\nEscreva um dos números abaixo para jogar:\n'
               '1 para escolher "\U0000270A" \n2 para escolher "\U0001F91A" \n3 para escolher "\U0000270C"\n'))
if e1 == 1:
    j1 = op[0]
elif e1 == 2:
    j1 = op[1]
elif e1 == 3:
    j1 = op[2]
j2 = random.choice(op)

# Opções que o jogador 1 vence
if (j1 == op[0] and j2 == op[2]) or (j1 == op[2] and j2 == op[1]) or (j1 == op[1] and j2 == op[0]):
    print(f'Você escolheu: {j1}\n    X \nJogador 2 escolheu: {j2}  \n{"-"*15}\nVocê ganhou!!!')
# Opções que ambos jogadores empatam
elif (j1 == op[0] and j2 == op[0]) or (j1 == op[1] and j2 == op[1]) or (j1 == op[2] and j2 == op[2]):
    print(f'Você escolheu: {j1}\n    X \nJogador 2 escolheu: {j2}  \n{"-"*15}\nOs jogadores empataram')
# Opções que o jogador 1 perde
else:
    print(f'Você escolheu: {j1}\n    X \nJogador 2 escolheu: {j2}  \n{"-"*15}\nVocê Perdeu!!')