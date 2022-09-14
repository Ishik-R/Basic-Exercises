# Exercício Python #099 - Função que descobre o maior
# https://www.youtube.com/watch?v=vp9UX7wr92o

# Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

print("\n#099 - Função que descobre o maior")
print("--" * 16)

def maior(*lst):
    print(f"Analisando a lista com {len(lst)} elementos... ", end="")
    if len(lst) == 0:
        print(f"\nNão há um maior valor a ser informado.")
    else:
        mai = lst[0]
        for num in lst:
            print(num, end=" ")
            if num > mai:
                mai = num
        print(f"\nO maior valor informado foi {mai}.")
        print("-=" * 16)

maior(1,8,3,2,5,6,-1)
maior(6,3,4)
maior(2,3)
maior(9)
maior()