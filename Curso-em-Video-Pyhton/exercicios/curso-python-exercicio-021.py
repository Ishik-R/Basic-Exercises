# Exercício Python #021 - Tocando um MP3
# https://www.youtube.com/watch?v=9FiEji_fzvk

# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# DOCUMENTAÇÃO EXTRA:
# PIP documentation: https://pip.pypa.io/en/stable/installation/
# Instalando e importando o módulo Pygame no VSCode: https://pt.stackoverflow.com/questions/451412/instalando-e-importando-o-m%C3%B3dulo-pygame-no-vscode

# Foi necessária a configuração do PIP para então a devida instalação do pygame. 
# O arquivo de música encontra-se na mesma pasta deste programa, com o nome 'music021.mp3'
# Ele somente reproduz a música, sem métodos adicionais.

import pygame

print('\nEXERCÍCIO 21 - Tocando um MP3')
print('--' * 16)

pygame.init()
pygame.mixer.music.load('music021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()