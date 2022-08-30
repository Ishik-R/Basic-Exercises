# Exercício Python #070 - Estatísticas em produtos
# https://www.youtube.com/watch?v=hS8QdW-1HTo

# Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos.
#  O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#   A) qual é o total gasto na compra.
#   B) quantos produtos custam mais de R$1000.
#   C) qual é o nome do produto mais barato.  

print("\n#070 - Estatísticas em produtos")
print("--" * 16)
products = []
prices = []
cond_b = 0
while True:
    products.append(str(input("Nome do produto: ")))
    prices.append(float(input("Preço (em R$): ")))
    if prices[-1] > 1000:
        cond_b += 1   
    opt = input("Você quer continuar? [S/N] ").upper().strip()
    while opt not in 'SN':
        print("Entrada inválida. Tente novamente.")
        opt = input("Você quer continuar? [S/N] ").upper().strip()
    print("=-" * 16)
    if opt == 'N':
        break
cond_c = products[prices.index(min(prices))]
print(f"Total gasto na compra: {sum(prices):.2f}")
print(f"Quantos produtos custam mais de R$1000: {cond_b}")
print(f"Nome do produto mais barato: {cond_c}")
print("=-" * 16)