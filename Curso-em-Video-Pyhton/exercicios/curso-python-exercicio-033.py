# Exercício Python #033 - Maior e menor valores
# https://www.youtube.com/watch?v=a_8FbW5oH6I

# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
print("\n#033 - Maior e menor valores")
print("--" * 16)

print("\nInsira três números inteiros distintos:")
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))
num = [n1, n2, n3]

print(f"\nMaior número: {max(num)}")
print(f"Menor número: {min(num)}\n")