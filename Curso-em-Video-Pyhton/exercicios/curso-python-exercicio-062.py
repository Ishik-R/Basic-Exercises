# EExercício Python #062 - Super Progressão Aritmética v3.0
# https://www.youtube.com/watch?v=BWAWq7n6PCk

# Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.

print("\n#062 - Super Progressão Aritmética v3.0")
print("--" * 16)
a1 = float(input("Insira o valor do termo inicial: "))
r = float(input("Insia o valor da razão desta PA: "))
n = 1
terms = 10
extra = 0
while n <= terms: 
    print(f"a{n} = {a1} + {(n-1)*r} = {a1+(n-1)*r}")
    if n == terms:
        extra = int(input("Você gostaria de ver mais quantos termos? "))
        terms += extra
    n += 1
print(f"Programa encerrado no termo {terms} da PA.")    