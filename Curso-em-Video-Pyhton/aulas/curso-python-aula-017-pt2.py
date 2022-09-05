# Curso Python #17 - Listas (Parte 2)
# https://www.youtube.com/watch?v=YV_JQmZNFsk

# Apresentação do funcionamento das listas, listas com capacidade de ter seus valores alterados. 
# Aqui exploramos a capacidade de inserir listas dentro de listas.

print("\nAULA #17 - Listas (Parte 2)")
print("--" * 16)

dados = ['Pedro', 25]
pessoas = list()
pessoas.append(dados[:])
print(f"Vamos exibir a lista de pessoas: {pessoas}")

dados2 = ['Maria', 32]
dados3 = ['Joana', 22]
pessoas.append(dados2[:])
pessoas.append(dados3[:])
print(f"Vamos exibir novamente a lista de pessoas: {pessoas}")
print(f"É possível acessar um dos subelementos: {pessoas[2]}")
print(f"É possível acessar elementos específicos dentro das listas: {pessoas[0][0]}, {pessoas[1][1]}")

print("\nÉ possível acessar os elementos da lista com o uso de uma estrutura for: ")
for individuo in pessoas:
    print(f"{individuo[0]} possui {individuo[1]} anos.")

print("\nÉ possível carregar uma lista com diferentes elementos com uma estrutura de loop:")
galera = list()
dado = list()
for c in range(0,2):
    dado.append(str(input(f"Nome {c+1}: ")))
    dado.append(int(input(f"Idade {c+1}: ")))
    galera.append(dado[:])
    dado.clear()
print(f"Dados carregados: {galera}")