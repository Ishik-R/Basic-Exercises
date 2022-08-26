# Exercício Python #055 - Maior e menor da sequência
# https://www.youtube.com/watch?v=Kjpb_IAOKRQ

# Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. 
#  No final, mostre qual foi o maior e o menor peso lidos.

print("\n#055 - Maior e menor da sequência")
print('--' * 16)

pesos = []
print("Insira o peso de 5 pessoas (em kg):")
for n in range(0, 5):
    pesos.append(float(input(f"Pessoa {n+1}: ")))
pesos.sort()
print(f"Menor peso inserido: {pesos[0]}kg")
print(f"Maior peso inserido: {pesos[4]}kg")