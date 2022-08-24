# Exercício Python #038 - Comparando números
# https://www.youtube.com/watch?v=iuPbB9uHczM

# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

print('\n#038 - Comparando números')
print('--' * 16)
print('Insira dois valores para serem comparados:')
n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))

if n1 > n2:
    print(f'O primeiro valor é maior: {n1} > {n2}')
elif n2 > n1:
    print(f'O segundo valor é maior: {n2} > {n1}')
else:
    print(f'Os dois valores são iguais: {n1} = {n2}')  