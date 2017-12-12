print('Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, \n'
      'calcule a sua área e a quantidade de tinta necessária para pintá-la, \n'
      'sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))

area = larg * alt

print('Sua parede tem a dimensão de {}mª x {}mª e sua area é de {}mª.'.format(larg, alt, area))

tinta = area / 2

print('Para pintar essa parede, você precisa de {} lt de tinta.'.format(tinta))