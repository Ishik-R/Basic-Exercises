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

#   OBS: exercício resolvido em três partes!
#
#   Aqui temos a parte principal do nosso sistema! Este programa necessita das funções presentes nos módulos 'manipulacao115.py' e
# 'interface115.py' para ser executado corretamente. O menu lê um arquivo txt (com nome padrão definido como 'lista115.txt'),
# que contem uma lista de nomes pessoas com suas respectivas idades. O programa é capaz de ler os nomes presentes e adicionar novos
# nomes ao arquivo. Toda a navegação das funcionalidades é feita no terminal.
#   Caso não exista um arquivo 'lista115.txt' o programa se encarregará de criar um arquivo vazio para armazenar os dados.

print("\n#115 - Criando um menu em Python")
print("--" * 16)
    
#Programa principal:
from interface115 import *
from manipulacao115 import *
from time import sleep

nomeArquivo = 'lista115.txt'
if not verificaArquivo(nomeArquivo):
    arq = open(nomeArquivo, 'wt+')
    arq.close
    print(f"Arquivo {nomeArquivo} criado com sucesso!")

while True:
    opcao = menu_principal(["Ver pessoas cadastradas: ","Cadastrar nova pessoa: ","Sair do sistema: "])
    sleep(1)
    if opcao == 1:
        mostrarNomes(nomeArquivo)
    elif opcao == 2:
        adicionarNomes(nomeArquivo)
    elif opcao == 3:
        print("Saindo do sistema... até logo!")
        break
    else:
        print("Por favor, insira uma opção válida!")
    sleep(1)