# Exercício Python #085 - Listas com pares e ímpares
# https://www.youtube.com/watch?v=2-fy24bbMJ4

# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos.
#  Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

print("\n#085 - Listas com pares e ímpares")
print("--" * 16)
num = [[],[]]
for n in range(0,7):
    aux = int(input(f"Valor {n+1}: "))
    if aux % 2 == 0:
        num[0].append(aux)
    else:
        num[1].append(aux)
num[0].sort()
num[1].sort()
print(f"Valores pares digitados: {num[0]}")
print(f"Valores pares digitados: {num[1]}")