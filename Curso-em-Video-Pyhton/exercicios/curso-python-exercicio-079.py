# Exercício Python #079 - Valores únicos em uma Lista
# https://www.youtube.com/watch?v=LkAzRnc_GPk

# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado.
#  No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

print("\n#079 - Valores únicos em uma Lista")
print("--" * 16)
num = []
while True:
    num.append(int(input("Digite um valor: ")))
    if num[-1] in num[:-1]:
        print("Este valor já está na lista e não será adicionado!")
        num.pop()
    else:
        print("Valor adicionado com sucesso.")
    ver = input("Você deseja continuar inserindo valores? [S/N] ").upper()
    while ver not in 'SN':
        ver = input("Entrada inválida. Responda com S para sim ou N para não: ").upper()
    if ver == 'N':
        break
print(f"Valores digitados em ordem crescente: {sorted(num)}")        