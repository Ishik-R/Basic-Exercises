# Exercício Python #019 - Sorteando um item na lista
# https://www.youtube.com/watch?v=_Nk02-mfB5I

# Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
#  Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

print('\nEXERCÍCIO 19 - Sorteando um item na lista')
print('--' * 16)
print('Insira o nome de 4 alunos: ')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
print(f'\nO aluno sorteado foi: {choice(lista)}\n')