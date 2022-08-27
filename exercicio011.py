# Ler altura e largura de uma parede, calcular sua área e quanto de tinta será necessário para pintar
la = int(input('Digite a largura da parede em metros: '))
alt = int(input('Digite a altura da parede em metros: '))
area = la*alt
tinta = area/2

print(f'Sua parede possui: \n{la}m de largura \n{alt}m de altura \n{area}m2 de área \nPrecisará de {tinta}L de tinta')
