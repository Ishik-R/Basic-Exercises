# Exercício Python #088 - Palpites para a Mega Sena
# https://www.youtube.com/watch?v=Hd7Ycaj61xE

# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

print("\n#088 - Palpites para a Mega Sena")

from random import randint
from time import sleep

print("--" * 16)
print("    JOGOS PARA A MEGA SENA    ")
print("--" * 16)
quant = int(input("Quantos jogos devem ser gerados? "))
jogos = list()
jogo = list()
print(f"=-=-=-= SORTEANDO {quant} JOGOS =-=-=-=")
for j in range(1, quant+1):
    sleep(1)
    while len(jogo) < 6:
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    print(f"Jogo {j}: {jogos[-1]}")
    jogo.clear()