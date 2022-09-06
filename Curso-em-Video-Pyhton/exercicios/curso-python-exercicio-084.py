# Exercício Python #084 - Lista composta e análise de dados
# https://www.youtube.com/watch?v=zPtvuLiEdKk

# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#  No final, mostre:
#   A) Quantas pessoas foram cadastradas.
#   B) Uma listagem com as pessoas mais pesadas.
#   C) Uma listagem com as pessoas mais leves.

print("\n#084 - Lista composta e análise de dados")
print("--" * 16)
pessoas = list() 
individual = list()
leve = list()
pesado = list()
men_peso = 0
mai_peso = 0
while True:
    individual.append(str(input("Nome: ")))
    individual.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        men_peso = individual[1]
        leve.append(individual[0])
        mai_peso = individual[1]
        pesado.append(individual[0])
    else:
        if individual[1] >= mai_peso:
            if mai_peso != individual[1]:
                pesado.clear()
            pesado.append(individual[0])
            mai_peso = individual[1]
        if individual[1] <= men_peso:
            if men_peso != individual[1]:
                leve.clear()
            leve.append(individual[0])
            men_peso = individual[1]    
    pessoas.append(individual[:])
    individual.clear()
    confirm = str(input("Deseja continuar [S/N]? ")).upper()
    while confirm not in 'SN':
        confirm = str(input("Entrada inválida. Insira S para continuar ou N para parar. ")).upper()
    if confirm == 'N':
        break
print("=-" * 16)
print(f"Número de pessoas cadastradas: {len(pessoas)}")
print(f"Menor peso: {men_peso}kg. ", end="")
if len(leve) == 1:
    print("Pessoa com esse peso: ", end="")
else:
    print("Pessoas com esse peso: ", end="")
for ent in leve:
    print(f"{ent}  ", end="")
print(f"\nMaior peso: {mai_peso}kg. ", end="")
if len(pesado) == 1:
    print("Pessoa com esse peso: ", end="")
else:
    print("Pessoas com esse peso: ", end="")
for ent in pesado:
    print(f"{ent} ", end="")
print()    
