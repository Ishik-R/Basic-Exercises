# Exercício Python #046 - Contagem regressiva
# https://www.youtube.com/watch?v=NR1RKt6NT8s

# Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício.
#  A contagem vai de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('\n#046 - Contagem regressiva')
print('--' * 16)
print('INICIANDO CONTAGEM')

for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('*FOGOS ESTOURANDO*')