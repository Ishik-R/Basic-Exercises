# Exercício Python #022 - Analisador de Textos
# https://www.youtube.com/watch?v=EQQt-6QqXOs

# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

print('\nEXERCÍCIO 22 - Analisador de Nomes')
print('--' * 16)

nome = input(str('Digite seu nome completo: '))
pNome = nome.split()[0]

print(f'Exibição de todas as letras sendo maiúsculas: {nome.upper()}')
print(f'Exibição de todas as letras sendo minúsculas: {nome.lower()}')
print(f'Quatidade total de caracteres sem considerar espaços: {len(nome.replace(" ",""))}')
print(f'Número de caracteres no primeiro nome: {len(pNome)}')
