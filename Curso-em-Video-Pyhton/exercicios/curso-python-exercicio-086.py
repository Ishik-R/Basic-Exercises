# Exercício Python #086 - Matriz em Python
# https://www.youtube.com/watch?v=EGmlFdwD4C4

# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com a formatação correta.

print("\n#086 - Matriz em Python")
print("--" * 16)
m = [[],[],[]]
for x in range(0,3):
    for y in range(0,3):
        m[x].append(int(input(f"Digite um valor para [{x}, {y}]: ")))
print("=-" * 16)
for x in range(0,3):
    for num in m[x]:
        print(f"[{num:^5}]", end="")
    print()