# Exercício Python #076 - Lista de Preços com Tupla
# https://www.youtube.com/watch?v=Qp2cXfCHk2I

# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#  No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print("\n#076 - Lista de Preços com Tupla")
print("--" * 16)
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20,
"Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for n in range(0, len(produtos), 2):
    print(f"{produtos[n]:-<20} R$ {produtos[n+1]:>.2f}")
print("--" * 16)