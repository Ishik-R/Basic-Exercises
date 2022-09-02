# Exercício Python #077 - Contando vogais em Tupla
# https://www.youtube.com/watch?v=8BgSqrOpKvU

# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#  Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print("\n#077 - Contando vogais em Tupla")
print("--" * 16)
palavras = ('Aqui','temos','uma','tupla','com','varias','palavras','sem','acento')
vogais = ('a','e','i','o','u')

for palavra in palavras:
    print(f"\nNa palavra '{palavra.upper()}' temos as vogais: ", end="")
    palavra.lower()
    for letra in palavra:
        if letra in vogais:
            print(letra, end=" ")