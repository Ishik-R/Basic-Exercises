# Exercício Python #029 - Radar eletrônico
# https://www.youtube.com/watch?v=hgJ_ETNGSj8

# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
#  Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
#  A multa vai custar R$7,00 por cada Km acima do limite.
print("\n#029 - Radar eletrônico")
print("--" * 16)

n = int(input("Insira a velocidade do carro ao passar pelo radar (em km/h): "))

if n <= 80:
    print("Tudo certo! Sem multa para você.\n")
else:
    print(f"VOCÊ FOI MULTADO EM R${(n-80)*7} POR ULTRAPASSAR O LIMITE DE VELOCIDADE (80 km/h).\n")