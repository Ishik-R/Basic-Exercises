# Exercício Python #082 - Dividindo valores em várias listas
# https://www.youtube.com/watch?v=uk0gDFQEo_I

# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas

print("\n#082 - Dividindo valores em várias listas")
print("--" * 16)
num = []
pares = []
impares =[]
while True:
    num.append(int(input("Digite um valor: ")))
    if num[-1] % 2 == 0:
        pares.append(num[-1])
    else:
        impares.append(num[-1])
    ver = input("Quer continuar [S/N]? ").upper()
    while ver not in 'SN':
        ver = input("Entrada inválida. As opções reconhecidas são S pra sim e N para não. Tente novamente: ").upper()
    if ver == 'N':
        break   
print("=-" * 16)        
print(f"Quantidade de números digitados: {len(num)}")
print(f"Números digitados: {num}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")