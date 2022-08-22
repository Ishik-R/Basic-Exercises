# Curso Python #10 - Condições (Parte 1)
# https://www.youtube.com/watch?v=K10u3XIf1-Q

print("\nAULA 010 - Condições (Parte 1)")
print("--" * 16)

n = int(input("Insira um valor inteiro: "))

if n > 9:
    print(f"Condição verdadeira: o número n ({n}) é maior que 9.")
else:
    print(f"Condição falsa: o número n ({n}) não é maior que 9.")
print("Condição verdadeira em uma sentença\n" if n > 9 else "Condição falsa em uma sentença\n")