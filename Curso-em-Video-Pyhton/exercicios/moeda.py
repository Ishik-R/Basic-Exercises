# Exercício Python #107 - Exercitando módulos em Python
# https://www.youtube.com/watch?v=y8pI8YBphQI

#Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas:
#  - aumentar()
#  - diminuir()
#  - dobro()
#  - metade()

def aumentar(n, tax):
    return n + (n*tax/100)

def diminuir(n, tax):
    return n - (n*tax/100)

def dobro(n):
    return 2*n

def metade(n):
    return n/2
    