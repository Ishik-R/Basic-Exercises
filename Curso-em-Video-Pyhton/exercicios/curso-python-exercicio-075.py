# Exercício Python #075 - Análise de dados em uma Tupla
# https://www.youtube.com/watch?v=1u7oA8ckjAc

# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#  No final, mostre:
#   A) Quantas vezes apareceu o valor 9.
#   B) Em que posição foi digitado o primeiro valor 3.
#   C) Quais foram os números pares.

print("\#075 - Análise de dados em uma Tupla")
print("--" * 16)
print("Insira quatro valores inteiros: ")
lista = tuple(int(input(f"Valor {c}: ")) for c in range(0,4))
print("=-" * 16)
if not lista.count(9):
    print("O número 9 não aparece nesta tupla.")
else:
    print(f"O número 9 aparece {lista.count(9)} nesta tupla.") 
if lista.index(3) < 0:
    print("O número 3 não aparece nesta tupla.")
else:
    print(f"Índice da primeira ocorrência do número 3: {lista.index(3)}")
print("Números pares presentes na tupla: ", end="")
for n in lista: 
    if n % 2 == 0:
        print(n, end=" ")        