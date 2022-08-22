# Exercício Python #023 - Separando dígitos de um número
# https://www.youtube.com/watch?v=wD2aerLMBWA

# Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

print('\nEXERCÍCIO 23 - Separando dígitos de um número')
print('--' * 16)

n = int(input('Digite um número inteiro entre 0 e 9999: '))

print(f'Número selecionado: {n}')
print(f'Unidade: {n // 1 % 10}')
print(f'Dezena: {n // 10 % 10}')
print(f'Centena: {n // 100 % 10}')
print(f'Milhar: {n // 1000 % 10}')