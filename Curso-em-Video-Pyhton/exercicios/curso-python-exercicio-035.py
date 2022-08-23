# Exercício Python #035 - Analisando Triângulo v1.0
# https://www.youtube.com/watch?v=NZiNphKkxhg

# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("\n#035 - Analisando Triângulo v1.0")
print("--" * 16)
print("Insira o valor de três segmentos de reta para verificarmos se é possível construir um triângulo com elas.")

r1 = float(input("R1: "))
r2 = float(input("R2: "))
r3 = float(input("R3: "))
tri = sorted([r1, r2, r3])

if tri[2] < tri[0]+tri[1]:
    print("É possível construir um triângulo.")
else:
    print("Não é possível construir um triângulo.")