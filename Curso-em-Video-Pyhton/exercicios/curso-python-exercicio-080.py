# Exercício Python #080 - Lista ordenada sem repetições
# https://www.youtube.com/watch?v=QDpwjBYRcVE

# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela.

print("\n#080 - Lista ordenada sem repetições")
print("--" * 16)
num = []
for n in range(0, 5):
    aux = int(input("Digite um valor: "))
    if len(num) == 0 or aux > num[-1]:
        num.append(aux)
        print("Valor adicionado ao final da lista.")
    else:
        c = 0
        while c < len(num):
            if aux <= num[c]:
                num.insert(c, aux)
                print(f"Valor adicionado no índice {c}")
                break
            c += 1
print("=-" * 16)        
print(f"Valores digitados em ordem crescente: {num}")        