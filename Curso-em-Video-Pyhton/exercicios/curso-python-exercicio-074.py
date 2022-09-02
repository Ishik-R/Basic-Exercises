# Exercício Python #074 - Maior e menor valores em Tupla
# https://www.youtube.com/watch?v=mlwt2CRQkTQ

# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

print("\#074 - Maior e menor valores em Tupla")
print("--" * 16)

from random import randint
num = tuple(randint(1,10) for i in range(0,5))
print("Os números da tupla são: ", end="")
for n in num:
    print(n, end=" ")    
print(f"\nMaior valor: {max(num)}")
print(f"Menor valor: {min(num)}")    