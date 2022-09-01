# Exercício Python #072 - Número por Extenso
# https://www.youtube.com/watch?v=ei2Kr3ccfO0

# Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#  Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print("\n#072 - Número por Extenso")
print("--" * 16)

num_extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
opt = 'S'
while opt not in 'N':
    num = int(input("Digite um número entre 0 e 20: "))
    while num not in range(0,21):
        num = int(input("Tente novamente. O número deve ser inteiro e estar entre 0 e 20: "))    
    print(f"Você digitou o número {num_extenso[num]}")
    opt = input("Você gostaria de continuar [S/N]? " ).upper()           