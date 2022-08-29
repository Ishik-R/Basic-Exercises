# Exercício Python #060 - Cálculo do Fatorial
# https://www.youtube.com/watch?v=9dlBZlkvvxY

# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#  Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

print("\n#060 - Cálculo do Fatorial")
print("--" * 16)

num = int(input("Insira um valor natural para calcularmos seu fatorial: "))
result = 1
if num < 0:
    print("Entrada inválida. Um número natural deve ser não negativo.")
elif num == 0:
    print(f"0! = {result} (por definição matemática)")
else:
    print(f"{num}! = ", end="")
    while num > 0:
        if num != 1:
            print(f"{num} x ", end="")
        else:
            print(f"{num} = ", end="")
        result = result * num
        num = num - 1
    print(f"{result}")