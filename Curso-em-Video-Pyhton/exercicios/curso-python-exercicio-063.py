# Exercício Python #063 - Sequência de Fibonacci v1.0
# https://www.youtube.com/watch?v=w7yn1_Mfu0E

# Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
#  Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print("\n#063 - Sequência de Fibonacci v1.0")
print("--" * 16)
n = int(input("Quantos termos da sequência de Fibbonacci devem ser exibidos? "))
c = 1
fib = 0
fib_next = 1
while c <= n: 
    print(f"{fib}", end=" - ")
    aux = fib_next + fib
    fib = fib_next
    fib_next = aux
    c += 1
print("Fim")