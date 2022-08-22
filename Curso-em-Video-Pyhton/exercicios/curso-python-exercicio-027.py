# Exercício Python #028 - Jogo da Adivinhação v.1.0
# https://www.youtube.com/watch?v=kchC5KLZSZ4

# Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
#  Ele deve pedir para o usuário tentar descobrir qual foi o número escolhido. 
#  O programa deverá escrever na tela se o usuário venceu ou perdeu.
print("\n#028 - Jogo da Adivinhação v.1.0")
print("--" * 16)

from random import randint

n = int(input("Tente adivinhar o número inteiro escolhido entre 0 e 5: "))
nComputador = randint(0, 5)

if n == nComputador:
    print("Você acertou!\n")
else:
    print(f"Você errou. O número sorteado foi {nComputador}\n")
