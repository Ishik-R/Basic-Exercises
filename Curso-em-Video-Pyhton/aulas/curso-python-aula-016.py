# Curso Python #16 - Tuplas
# https://www.youtube.com/watch?v=0LB3FSfjvao

# Apresentação do funcionamento da função 'tuple', listas imutáveis.

print("\nAULA #16 - Tuplas")
print("--" * 16)

bebidas = ('água','refrigerante','chá','suco','refresco')

print(f"Exibir o tuple: {bebidas}")
print(f"Acessar o elemento no índice 2: {bebidas[2]}")
print(f"Acessar os elementos entre os índices especificados: {bebidas[0:2]}")
print(f"Acessar todos os elementos além do índice especificado: {bebidas[1:]}")
print(f"Acessar o último elemento: {bebidas[-1]}")

print(f"Exibir a quantidade de elementos presentes no tuple: {len(bebidas)}")
print(f"Exibir os elementos em ordem (no caso de String, em ordem alfabética): {sorted(bebidas)}")
print(f"Procurar pela primeira ocorrência de um elemento e retornar o índice: {bebidas.index('refrigerante')} ")

print("É possível acessar os elementos de um tuple por meio de loops: ")
for c in range(0, len(bebidas)):
    print(bebidas[c], end =' ')

print("\nO loop pode conter uma nova variável para receber cada elemento da tupla: ")
for bebida in bebidas:
    print(bebida, end=' ')

print("\nOutra técnica para acessar os elementos em um loop é pelo enumerate: ")
for position, bebida in enumerate(bebidas):
    print(f"{position}: {bebida} ", end=' ')