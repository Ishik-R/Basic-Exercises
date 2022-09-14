# Exercício Python #100 - Funções para sortear e somar
# https://www.youtube.com/watch?v=MEs-41JcuhM

# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


print("\n#100 - Funções para sortear e somar")
print("--" * 16)

from time import sleep
from random import randint

def sorteia(nums):
    print("Sorteando 5 números: ", end="")
    for i in range(0,5):
        nums.append(randint(1,10))
        print(f"{nums[i]}", end=" ", flush=True)
        sleep(0.4)
    print()

def somaPar(nums):
    s = 0
    for n in nums:
        if n % 2 == 0:
            s += n
    print(f"Somando os números pares da lista: {nums} - a soma vale {s}\n")
    
numeros = list()
sorteia(numeros)
somaPar(numeros)