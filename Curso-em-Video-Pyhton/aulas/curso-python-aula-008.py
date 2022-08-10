# Curso Python #08 - Utilizando Módulos
# https://www.youtube.com/watch?v=oOUyhGNib2Q

# REPOSITÓRIO DE MÓDULOS PYTHON: https://pypi.org/
# import random (gerador de números aleatórios)
# import emoji (apresentação de emojis) - necessária instalação para a utilização!

import math
# Para importar funções específicas: from math import sqrt, ceil, floor

print('\nCALCULADORA DE RAIZ')
print('--' * 16)

num = int(input('Insira um número inteiro: '))
root = math.sqrt(num)

print(f'\nA raiz de {num} é igual a {root}.')
print(f'Arredondado para cima: {math.ceil(root)}')
print(f'Arredondado para baixo: {math.floor(root)}')
print(f'Arredondado com duas casas decimais: {root:.2f}')