# Exercício Python #016 - Quebrando um número
# https://www.youtube.com/watch?v=-iSbDpl5Jhw

# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc 

print('\nEXERCÍCIO 16')
print('--' * 16)

n = float(input('Digite um número: '))
print(f'\nO número {n} possui como parte inteira o valor {trunc(n)}')
print(f'Também é possível converter o número {n} para int: {int(n)}\n')