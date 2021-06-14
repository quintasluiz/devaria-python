#Faça um programa que leia a altura e largura de uma parede em metros.Calcule a sua area e a quantidade
#tinta necessaria para pinta-la sabendo que cada litro de tinta, pinta uma area de 2m quadrados

larg = float(input('Largura da parede '))
alt = float(input('Altura da parede '))
area = larg * alt
print('Sua parede tem a dimensao de {}x{} e sua area e de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede voce precisara de {}l de tinta'.format(tinta))






