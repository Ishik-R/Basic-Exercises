# Exercício Python #026 - Primeira e última ocorrência de uma string
# https://www.youtube.com/watch?v=23UOVEetNPY

# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('\nEXERCÍCIO 026 - Primeira e última ocorrência de uma string')
print('--' * 16)

frase = input("Escreva uma frase qualquer: ")

print(f"\nSua frase foi: {frase}")
print(f"A letra a aparece {frase.lower().count('a')} vezes")
print(f"A letra a aparece pela primeira vez na posição {frase.lower().find('a')+1}")
print(f"A letra a aparece pela última vez na frase na posição {frase.lower().rfind('a')+1}\n")