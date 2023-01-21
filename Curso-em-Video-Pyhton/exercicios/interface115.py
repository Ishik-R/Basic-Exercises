# Exercício Python #115a - Criando um menu em Python
# https://www.youtube.com/watch?v=pog8YmHkGMs
#
# Exercício Python 115a: Vamos criar um menu em Python, usando modularização.

# Exercício Python #115b - Arquivos com Python
# https://www.youtube.com/watch?v=bfTFe6bKLXk
#
# Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python. 

# Exercício Python #115c - Finalizando o projeto
# https://www.youtube.com/watch?v=-WZ1ddZK7Tc
#
# Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
#
#   OBS: exercício resolvido em três partes!
#   
#   Aqui estão agrupadas as funções para a navegação do menu do exercício 115

def linha(t=30):
    return '--' * t

def menu_principal(opcoes):
    print(linha())
    print("MENU PRINCIPAL".center(30))
    print(linha())
    c = 1
    for opcao in opcoes:
        print(f"{c} - {opcao}")
        c += 1
    print(linha())
    escolha = selecionar("Sua opção: ")
    print(linha())
    return escolha

def selecionar(texto):
    while True:
        try:
            entrada = int(input(texto))
        except:
            print("Por favor, insira um valor como entrada!")
            print(linha())
        else:
            return entrada
