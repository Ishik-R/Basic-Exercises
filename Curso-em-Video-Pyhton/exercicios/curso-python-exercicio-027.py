# Exercício Python #027 - Primeiro e último nome de uma pessoa
# https://www.youtube.com/watch?v=SifYYsXhLM8

# Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
print("\n#027 - Primeiro e último nome de uma pessoa")
print("--" * 16)

nome = input("Escreva seu nome completo: ").title().split()

print(f"Olá {nome[0]}, seu último nome é {nome[len(nome)-1]} \n")