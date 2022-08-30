# Exercício Python #067 - Tabuada v3.0
# https://www.youtube.com/watch?v=X0a5aZg93Uc

# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#  O programa será interrompido quando o número solicitado for negativo. 

print("\n#067 - Tabuada v3.0")
print("--" * 16)
print("OBS: o laço será interrompido quando o número solicitado for negativo.")
while True:
    print("-=" * 16) 
    num = int(input("Você gostaria de ver a tabuada de qual valor? "))
    if num < 0:
        break
    c = 1
    while c <= 10:
        print(f"{c:2} * {num} = {c*num}")
        c += 1
print("Programa encerrado.")                