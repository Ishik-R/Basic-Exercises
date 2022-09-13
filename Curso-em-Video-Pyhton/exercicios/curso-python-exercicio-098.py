# Exercício Python #098 - Função de Contador
# https://www.youtube.com/watch?v=DCBlt_z2UOE

# Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
#  a) de 1 até 10, de 1 em 1
#  b) de 10 até 0, de 2 em 2
#  c) uma contagem personalizada

print("\n#098 - Função de Contador")
print("--" * 16)

def contador(inicio, final, passo):
    if passo > 0:
        final += 1
    else:
        final -= 1
    for n in range(inicio, final, passo):
        print(f"{n} ", end="")
    print("FIM")
    print("=-" * 16)

print(f"Contagem de 1 até 10, de 1 em 1:")
contador(1,10,1)
print(f"Contagem de 10 até 0, de 2 em 2:")
contador(10,2,-2)

print(f"Valores personalizados: ")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
print(f"Contagem de {i} até {f}, de {p} em {p}")
contador(i,f,p)