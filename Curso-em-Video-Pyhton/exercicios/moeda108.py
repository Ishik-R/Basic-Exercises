#  Python #108 - Formatando Moedas em Python
# https://www.youtube.com/watch?v=KtRkGEeUdqE

# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda()
#  que consiga mostrar os números como um valor monetário formatado.

def monetario(n):
    value = f'R${n:.2f}'.replace('.',',')
    return value

def aumentar(n,tax,change=True):
    value =  n + (n*tax/100) 
    if change:
        value = f'R${n:.2f}'.replace('.',',')
    return value

def diminuir(n,tax,change=True):
    value = n - (n*tax/100)
    if change:
        value = f'R${n:.2f}'.replace('.',',')
    return value

def dobro(n,change=True):
    value = 2*n
    if change:
        value = f'R${n:.2f}'.replace('.',',')
    return value

def metade(n,change=True):
    value = n/2 
    if change:
        value = f'R${n:.2f}'.replace('.',',')
    return value
