# Exercício Python #078 - Maior e Menor valores na Lista
# https://www.youtube.com/watch?v=q8Z1cRdJnfk

# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

print("\n#078 - Maior e Menor valores na Lista")
print("--" * 16)
num = []
for n in range(0,4):
    num.append(int(input(f"Valor {n+1}: ")))
print(f"Maior valor digitado: {max(num)}. índice da primeira aparição: {num.index(max(num))}")
print(f"Menor valor digitado: {min(num)}. índice da primeira aparição: {num.index(min(num))}")