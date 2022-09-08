# Exercício Python #091 - Jogo de Dados em Python
# https://www.youtube.com/watch?v=cwrqIztaAwk

# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#  Guarde esses resultados em um dicionário em Python.
#  No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# MATERIAL COMPLEMENTAR: How do I sort a dictionary by value?
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

print("\n#091 - Jogo de Dados em Python")
print("--" * 16)

from random import randint
from time import sleep
import operator

players = dict()
classification = dict()
for n in range(1,5):
    players[f'jogador {n}'] =  randint(1,6)
for key, info in players.items():
    print(f"{key} tirou {info} no dado")
    sleep(1)

print("=-" * 16)
print("MÉTODO 1: operator.itemgetter() - requer import")
pos = 1
classification = sorted(players.items(), key=operator.itemgetter(1), reverse=True)
for p in classification:
    print(f"{pos}: {p[0]}, tirando {p[1]} no dado!")
    pos += 1

print("=-" * 16)
print("MÉTODO 2: lambda x: x[i]")
pos = 1
classification = sorted(players.items(), key=lambda x:x[1], reverse=True)
for p in classification:
    print(f"{pos}: {p[0]}, tirando {p[1]} no dado!")
    pos += 1