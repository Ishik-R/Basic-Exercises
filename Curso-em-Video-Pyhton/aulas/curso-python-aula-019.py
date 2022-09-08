# Curso Python #19 - Dicionários
# https://www.youtube.com/watch?v=ZWj8o692qGY

# Explicação da funcionalidade dos dicionários e da integração dos dicionários com listas.

print("\nAULA #19 - Dicionários")
print("--" * 16)

exemploCriacao = dict()
dados = {'nome':'Pedro', 'idade':25, 'peso':78.9}
filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'George Lucas'
}
outro_filme = {
    'titulo':'O Poderoso Chefão',
    'ano':1972,
    'diretor':'Francis Ford Coppola'
}

dados['genero'] = 'M'
del dados['genero']

print(f"Podemos acessar os elementos de um dicionário ao chamá-lo: {dados['nome']}")
print(f"É possível exibir somente os valores de um dicionário: {filme.values()}")
print(f"É possível exibir somente os identificadores de um dicionário: {filme.keys()}")
print(f"É possível exibir os valores e seus índices simultaneamente: {filme.items()}")

print("\nUso de um loop para exibição dos elementos: ")
for key, value in filme.items():
    print(f"{key}: {value}")

print("\nÉ possível armazenar itens de um dicionário dentro de listas: ")
cinema = []
cinema.append(filme)
cinema.append(outro_filme)
print(f"Podemos acessar os elementos dentro da lista: {cinema[0]['titulo']}")

print("\nÉ possível então combinar os recursos de listas e dicionários para exibição dos elementos: ")
for filme_em_cartaz in cinema:
    print(filme_em_cartaz) 

print("\nUm exemplo de input com lista e dicionário com os estados do Brasil: insira os valores para 3 estados")
estado = dict()
brasil = list()
for n in range(0,3):
    estado['uf'] = str(input(f"Unidade federativa {n+1}: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())

print("\nExibição dos valores: ")
for state in brasil:
    for key,value in state.items():
        print(f"Item: {key:<5} -> {value}")
for state in brasil:    
    print("ESTADO: ", end="")
    for info in state.values():
        print(f"{info} ", end="")
    print()    