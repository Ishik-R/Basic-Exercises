# Exercício Python #017 - Catetos e Hipotenusa
# https://www.youtube.com/watch?v=vmPW9iWsYkY

# Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

print('\nEXERCÍCIO 17 - Calculador de Hipotenusa')
print('--' * 16)

c1 = float(input('Insira o valor para o cateto oposto: '))
c2 = float(input('Insira o valor para o cateto adjacente: '))
print(f'\nPelo Teorema de Pitágoras, a hipotenusa deste triângulo retângulo vale aproximadamente {math.sqrt(c1**2+c2**2):.2f}')

# existe também um método específico para calcular a hipotenusa, dado o valor dos catetos: hypot(c1, c2), dentro do módulo math