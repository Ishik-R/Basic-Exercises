# Exercício Python #096 - Função que calcula área
# https://www.youtube.com/watch?v=oV1s53YGtvE

# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

print("\n#096 - Função que calcula área")
print("--" * 16)

def calculaArea(x, y):
    return x*y
wid = float(input("Largura (m): "))
hei = float(input("Comprimento (m): "))
print(f"A área de um terreno de {wid:.2f}m x {hei:.2f}m é de {calculaArea(wid,hei):.2f}m^2")