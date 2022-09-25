# Cores no terminal ANSI (Escape sequence)
#      style; text; background
# \033[0;33;44m
# Style 0(none), 1(negrito), 4(sublinhado) e 7(inverter cor de fundo e de letra)
# Text de 30 a 37
# Background de 40 a 47

# Testando estilos
print('\033[0;31;40mOlá mundo!\033[m')
print('\033[1;31;40mOlá mundo!\033[m')
print('\033[4;31;40mOlá mundo!\033[m')
print('\033[7;31;40mOlá mundo!\033[m\n')

# Testando cor de texto
print('\033[1;30;41mOlá mundo!\033[m')
print('\033[1;31;40mOlá mundo!\033[m')
print('\033[1;32;40mOlá mundo!\033[m')
print('\033[1;33;40mOlá mundo!\033[m')
print('\033[1;34;40mOlá mundo!\033[m')
print('\033[1;35;40mOlá mundo!\033[m')
print('\033[1;36;40mOlá mundo!\033[m')
print('\033[1;37;40mOlá mundo!\033[m\n')

# Testando cor de background
print('\033[1;31;40mOlá mundo!\033[m')
print('\033[1;32;41mOlá mundo!\033[m')
print('\033[1;31;42mOlá mundo!\033[m')
print('\033[1;31;43mOlá mundo!\033[m')
print('\033[1;31;44mOlá mundo!\033[m')
print('\033[1;31;45mOlá mundo!\033[m')
print('\033[1;31;46mOlá mundo!\033[m')
print('\033[1;31;47mOlá mundo!\033[m')