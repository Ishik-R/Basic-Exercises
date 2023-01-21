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
#   Aqui estão agrupadas as funções responsáveis pelo carregamento e leitura do arquivo de pessoas cadastradas.
#   Vale ressaltar que o nome padrão do arquivo é definido no programa principal. 
#   O arquivo deve agrupar os dados da pessoa do seguinte modo: 'nome';'idade'
#   Outras formatações resultarão em erros de leitura!

def linha(t=30):
    return '--' * t

def verificaArquivo(name):
    try:
        arquivo = open(f'{name}','r')
        arquivo.close()
    except FileNotFoundError:
        return False
    except:
        print("Ocorreu um erro inesperado!")
        return False
    else:
        return True

def mostrarNomes(name):
    print("Lista de pessoas cadastradas:")
    arq = open(name,'r')
    listaPessoas = []
    for linha in arq:
        listaPessoas.append(linha.rstrip('\n').strip())
    arq.close()
    for dados in listaPessoas:
        nome,idade = dados.split(";")
        print(f"Nome: {nome:15}Idade: {idade}")

def adicionarNomes(name):
    print(f"Adicionando nomes em {name}:")
    arq = open(name,'a')
    nome = input("Insira um nome: ")
    idade = leiaInt(f"Insira a idade de {nome}: ")
    arq.write(f'\n{nome};{idade}')
    arq.close()
    print(linha())
    print("DADOS INSERIDOS COM SUCESSO!")

def leiaInt(texto):
    while True:
        valor = input(texto)
        if valor.isnumeric():
            return int(valor)
        else:
            print(linha())
            print("ERRO! Digite um número válido")