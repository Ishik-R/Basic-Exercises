# Exercício Python #031 - Custo da Viagem
# https://www.youtube.com/watch?v=PGqHyzWoagc

# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#  Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
print("\n#031 - Custo da Viagem")
print("--" * 16)

distancia = int(input("Insira a distância de sua viagem (em km): "))

if distancia <= 200:
    print(f"O valor da passagem é de R${distancia*0.50:.2f}\n")
else:
    print(f"O valor da passagem é de R${distancia*0.45:.2f}\n")