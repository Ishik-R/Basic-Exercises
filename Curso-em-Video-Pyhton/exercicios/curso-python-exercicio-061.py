# Exercício Python #061 - Progressão Aritmética v2.0
# https://www.youtube.com/watch?v=vu5ehetQGe8

# Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("\n#061 - Progressão Aritmética v2.0")
print("--" * 16)
a1 = float(input("Insira o valor do termo inicial: "))
r = float(input("Insia o valor da razão desta PA: "))
n = 1
while n <= 10: 
    print(f"a{n} = {a1} + {(n-1)*r} = {a1+(n-1)*r}")
    n += 1