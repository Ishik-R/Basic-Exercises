# Exercício Python #020 - Sorteando uma ordem na lista
# https://www.youtube.com/watch?v=OPh0nngbBSY

# Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
#  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('\nEXERCÍCIO 20 - Sorteando uma ordem na lista')
print('--' * 16)
print('Insira o nome de 4 alunos: ')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'\nA ordem de apresentação é a seguinte: {lista}\n')