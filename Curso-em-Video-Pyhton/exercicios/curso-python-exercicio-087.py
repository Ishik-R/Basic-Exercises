# Exercício Python #087 - Mais sobre Matriz em Python
# https://www.youtube.com/watch?v=QhS829x6up4

# Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.

print("\n#087 - Mais sobre Matriz em Python")
print("--" * 16)
m = [[],[],[]]
sum_par = 0
sum_third = 0
biggest_sec = 0
for x in range(0,3):
    for y in range(0,3):
        m[x].append(int(input(f"Digite um valor para [{x}, {y}]: ")))
print("=-" * 16)
for x in range(0,3):
    for y in range(0,3):
        print(f"[{m[x][y]:^5}]", end="")
        if m[x][y] % 2 == 0:
            sum_par += m[x][y]
        if x == 1:
            if y == 0:
                biggest_sec = m[x][y]
            elif m[x][y] > biggest_sec:
                biggest_sec = m[x][y]
        if x == 2:
            sum_third += m[x][y] 
    print()
print("=-" * 16)    
print(f"A soma de todos os valores pares digitados: {sum_par}")
print(f"A soma dos valores da terceira coluna: {sum_third}")
print(f"O maior valor da segunda linha: {biggest_sec}")
