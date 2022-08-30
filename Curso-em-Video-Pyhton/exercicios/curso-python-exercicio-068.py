# Exercício Python #068 - Jogo do Par ou Ímpar
# https://www.youtube.com/watch?v=EIzgKCCDdc0

# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

print("\n#068 - Jogo do Par ou Ímpar")
print("--" * 16)
print("OBS: o jogo persistirá até que o jogador perca.")
from random import randint
wins = 0
while True:
    print("-=" * 16) 
    num_jogador = int(input("Escolha seu valor: "))
    num_comp = randint(0, 11)
    guess = input("Par (P) ou ímpar (I): ").upper().strip()
    while guess not in 'PI':
        guess = input("Opção não compreendida. Escolha entre P e I (para par e ímpar respectivamente): ").upper().strip()
    print(f"Você escolheu {num_jogador} e o computador escolheu {num_comp}. ", end="")
    if (num_jogador+num_comp) % 2 == 0:
        even_or_odd = 'P'
        print("O resultado final é PAR. ", end="")
    else:
        even_or_odd = 'I'
        print("O resultado final é ÍMPAR. ", end="") 
    if guess == even_or_odd:
        print("Você VENCEU!")
        wins += 1
    else:
        print("Você PERDEU :(")
        break
print(f"Programa encerrado. Você venceu {wins} vez(es).")                