# Exercício Python #025 - Procurando uma string dentro de outra
# https://www.youtube.com/watch?v=WHWGz2Dy1ZU

# Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
print('\nEXERCÍCIO 025 - Procurando uma string dentro de outra')
print('--' * 16)

nome = input('Qual é o seu nome completo? ').upper()

if 'SILVA' in nome:
    print('Seu nome tem Silva.')
else:
    print('Seu nome não tem Silva.')