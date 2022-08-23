# Exercício Python #032 - Ano Bissexto
# https://www.youtube.com/watch?v=cyGY_83m4Xw

# Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print("\n#032 - Ano Bissexto")
print("--" * 16)

ano = int(input("Insira um ano para ser verificado como bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')