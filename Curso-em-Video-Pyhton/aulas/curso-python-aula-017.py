# Curso Python #17 - Listas (Parte 1)
# https://www.youtube.com/watch?v=N1hTsbW50eM

# Apresentação do funcionamento das listas, listas com capacidade de ter seus valores alterados.

print("\nAULA #17 - Listas (Parte 1)")
print("--" * 16)

comidas = ['sanduíche','macarrão','sorvete','bolo','pudim']

print(f"Exibir a lista: {comidas}")
print(f"Acessar o elemento no índice 2: {comidas[2]}")
print(f"Acessar os elementos entre os índices especificados: {comidas[0:2]}")
print(f"Acessar todos os elementos além do índice especificado: {comidas[1:]}")
print(f"Acessar o último elemento: {comidas[-1]}")

print(f"\nExibir a quantidade de elementos presentes na lista: {len(comidas)}")
print(f"Exibir os elementos em ordem (no caso de String, em ordem alfabética): {sorted(comidas)}")
print(f"Procurar pela primeira ocorrência de um elemento e retornar o índice: {comidas.index('bolo')} ")

comidas.append('arroz')
print(f"\nInserindo um novo elemento no final da lista - APPEND: {comidas[-1]}")
comidas.insert(0,'feijão')
print(f"Inserindo um novo elemento na lista em um índice específico - INSERT: {comidas}")
del comidas[2]
print(f"Removendo um elemento de um índice específico - DEL: {comidas}")
comidas.pop()
print(f"Removendo o último elemento de uma lista - POP: {comidas}")
comidas.remove('feijão')
print(f"Removendo um elemento específico dentro da lista - REMOVE: {comidas}")

valores = list(range(4,15,2))
print(f"\nCriação de uma lista em ordem: {valores}")

print("É possível acessar os elementos de uma lista por meio de loops: ", end="")
for c in range(0, len(comidas)):
    print(comidas[c], end =' ')

print("\nO loop pode conter uma nova variável para receber cada elemento da lista: ", end="")
for snack in comidas:
    print(snack, end=' ')

print("\nOutra técnica para acessar os elementos em um loop é pelo enumerate: ", end="")
for position, comida in enumerate(comidas):
    print(f"{position}: {comida}, ", end=' ')
