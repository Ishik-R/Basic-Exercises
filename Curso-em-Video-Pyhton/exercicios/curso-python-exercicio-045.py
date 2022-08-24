# Exercício Python #045 - GAME: Pedra Papel e Tesoura
# https://www.youtube.com/watch?v=tapTa6KVG-A

# Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
print('\n#045 - GAME: Pedra Papel e Tesoura')
print('--' * 16)

from random import randint
opt = ['pedra', 'papel', 'tesoura']
print('''Suas opções:
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')
player = int(input('Escolha sua jogada: ')) - 1
comp = randint(0,2)

print('\nJA - KEN - PO')
print(f'Jogador: selecionou {opt[player]}')
print(f'Computador: selecionou {opt[comp]}')

clash = comp - player
if clash == 0:
    print('EMPATE!')
elif clash == 2 or clash == -1:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU :(')