# Curso Python #11 - Cores no Terminal
# https://www.youtube.com/watch?v=0hBIhkcA8O8

print("\nAULA 011 - Cores no Terminal")
print("--" * 16)

# coloração pelo padrão ANSI
# Primeira informação: STYLE
#   0 - none
#   1 - bold
#   4 - underline
#   7 - negative
# Segunda informação: TEXT - numeração referente as cores
#   30 - black
#   31 - red
#   32 - green
#   33 - yellow
#   34 - blue
#   35 - magenta
#   36 - cyan
#   37 - grey
#   97 - white
# Terceira informação: BACKGROUND - numeração referente as cores
#   40 - black
#   41 - red
#   42 - green
#   43 - yellow
#   44 - blue
#   45 - magenta
#   46 - cyan
#   47 - grey
#   107 - white

print('\033[0;97;41m - Nenhum estilo, texto branco e fundo vermelho\033[m')
#print('\033[4;33;44m - Sublinhado, texto amarelo e fundo azul\033[m')
#print("\033[1;35;43m Negrito, texto roxo e fundo amarelo")
#print("\033[30;42m Nenhum estilo, texto preto e fundo verde")
#print("\033[m Nenhum estilo, texto cinza e fundo preto - retornar a configuração padrão do terminal")