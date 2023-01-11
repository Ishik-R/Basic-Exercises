# Exercício Python #106 - Sistema interativo de ajuda em Python
# https://www.youtube.com/watch?v=BMKYnZoxy88

# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
#  O usuário vai digitar o comando e o manual vai aparecer.
#  Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
#  Importante: use cores.

print("\n#106 - Sistema interativo de ajuda em Python")
print("--" * 16)

class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
        reset = '\033[m'

def message(text, background_color=bg.reset):
    """
    -> message: uma função que imprime a mensagem recebida como parâmetro com bordas de tamanho adequado.
     É possível também customizar a cor de fundo, inserindo-a como parâmetro.
     :param text: string de texto a ser impressa.
     :param background_color: informação em código ANSI sobre a preferência da cor de fundo. Faz uso da classe 'bg'. Valor padrão: bg.reset
    """
    print(background_color)
    print("~"*(len(text)+4))
    print(f"  {text}")
    print("~"*(len(text)+4),bg.reset)

def helper():
    """
    -> helper: uma função que retorna as informações do Interactive Help do Python de um comando selecionado pelo usuário.
     O usuário deve digitar um comando e o respectivo manual será exibido.
     Quando o usuário digitar a palavra 'fim', o programa se encerrará. 
    """
    from time import sleep

    while True:
        message("SISTEMA DE AJUDA PyHELP", bg.lightgrey)
        key = input("Função ou biblioteca: ").lower()
        if key.lower() == 'fim':
            sleep(1)
            message("ATÉ LOGO!", bg.green)
            break
        else:
            message(f"Acessando o manual do comando '{key}'...", bg.red)
            sleep(1.5)
            help(key)
    
#Programa principal:
helper()