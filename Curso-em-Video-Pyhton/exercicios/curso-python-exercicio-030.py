# Exercício Python #030 - Par ou Ímpar?
# https://www.youtube.com/watch?v=4vFCzKuHOn4

# Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
print("\n#030 - Par ou Ímpar?")
print("--" * 16)

n = int(input("Insira um número inteiro: "))

if n % 2 == 0:
    print(f"{n} é PAR.\n")
else:
    print(f"{n} é ÍMPAR.\n")