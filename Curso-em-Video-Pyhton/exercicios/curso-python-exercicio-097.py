# Exercício Python #097 - Um print especial
# https://www.youtube.com/watch?v=Q6basnSo7r0

# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

print("\n#097 - Um print especial")
print("--" * 16)

def specialPrint(txt):
    n = len(txt) + 4
    print("~" * n)
    print(f"  {txt}  ")
    print("~" * n)

specialPrint("Olá mundo!")
specialPrint("Temos aqui um print diferenciado!")