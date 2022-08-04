# Exercício Python #011 - Pintando Parede
# https://www.youtube.com/watch?v=mzSJpn9ldt4

w = float(input('Largura da parede (em metros): '))
h = float(input('Altura da parede (em metros: '))

print(f'Para pintar esta parede de {w:.2f}m por {h:.2f}m você precisará de aproximadamente {(w*h)/2:.1f}L de tinta.')
# O problema considera que 1L de tinta é suficiente para pintar uma área de 2m^2