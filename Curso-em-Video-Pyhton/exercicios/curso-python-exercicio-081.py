# Exercício Python #081 - Extraindo dados de uma Lista
# https://www.youtube.com/watch?v=SXJKAVVlvGA

# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, mostre:
#   A) Quantos números foram digitados.
#   B) A lista de valores, ordenada de forma decrescente.
#   C) Se o valor 5 foi digitado e está ou não na lista.

print("\n#081 - Extraindo dados de uma Lista")
print("--" * 16)
num = []
while True:
    num.append(int(input("Digite um valor: ")))
    ver = input("Quer continuar [S/N]? ").upper()
    while ver not in 'SN':
        ver = input("Entrada inválida. As opções reconhecidas são S pra sim e N para não. Tente novamente: ").upper()
    if ver == 'N':
        break   
print("=-" * 16)        
print(f"Quantidade de números digitados: {len(num)}")
num.sort(reverse=True)
print(f"Valores digitados em ordem decrescente: {num}")
if 5 in num:
    print("O valor 5 faz parte da lista!")       
else:
    print("O valor 5 não faz parte da lista.") 