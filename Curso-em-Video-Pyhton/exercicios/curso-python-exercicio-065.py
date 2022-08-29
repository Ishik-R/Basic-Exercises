# Exercício Python #065 - Maior e Menor valores
# https://www.youtube.com/watch?v=QNPuPlPM--0

# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
#  No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
#  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

print("\n#065 - Maior e Menor valores")
print("--" * 16)
confirm = 'S'
count = 0
list_num = []
while confirm != 'N': 
    if confirm in 'S':
        list_num.append(int(input("Insira um número inteiro: ")))
        count += 1
    else:
        print("Desculpe. Não entendi o comando. Tente novamente.")
    confirm = input("Você deseja continuar [S/N]? ").upper().strip()
if count == 1:
    print(f"\nFoi inserido {count} valor.")
else:
    print(f"\nForam inseridos {count} valores.")
print(f"Menor valor digitado: {min(list_num)}")
print(f"Maior valor digitado: {max(list_num)}")
print(f"Média dos valores: {sum(list_num)/len(list_num)}")