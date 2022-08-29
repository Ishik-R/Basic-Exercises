# Exercício Python #058 - Jogo da Adivinhação v2.0
# https://www.youtube.com/watch?v=-QkOIHJ1Chw

# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

print("\n#058 - Jogo da Adivinhação v2.0")
print("--" * 16)
from random import randint
num = randint(0,10)
tries = 1
guess = int(input("O computador escolheu um número entre 0 a 10. Tente adivinhá-lo: "))
while guess != num:
    print("Tente novamente!")
    guess = int(input("Nova tentativa: "))
    tries += 1
if tries == 1:
    print(f"Você acertou! E só precisou de {tries} tentativa!")
else:
    print(f"Você acertou! Foram necessárias {tries} tentativas.")