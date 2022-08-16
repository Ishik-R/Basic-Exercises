# Exercício Python #018 - Seno, Cosseno e Tangente
# https://www.youtube.com/watch?v=9GvsphwW26k

# Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

print('\nEXERCÍCIO 18 - Seno, Cosseno e Tangente')
print('--' * 16)

a = float(input('Insira o valor de um ângulo qualquer (em graus): '))
aSin = sin(radians(a))
aCos = cos(radians(a))
aTan = tan(radians(a))
print(f'\nSeno de {a:.1f}: {aSin:.3f}')
print(f'Cosseno de {a:.1f}: {aCos:.3f}')
print(f'Tangente de {a:.1f}: {aTan:.3f}\n')