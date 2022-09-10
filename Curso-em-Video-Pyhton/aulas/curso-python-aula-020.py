# Curso Python #20 - Funções (Parte 1)
# https://www.youtube.com/watch?v=ezfr9d7wd_k

# Explicação da criação de funções, rotinas personalizadas de comandos.

print("\n#20 - Funções (Parte 1)")
print("--" * 16)

def mensagemPadrao():
    print("=-" * 16)
    print("Podemos inserir comandos que precisaremos chamar em um programa várias vezes em uma função.")
    print("-=" * 16)
mensagemPadrao()
mensagemPadrao()

def somarTirandoUm(a,b):
    print(f"As funções podem receber e retornar parâmetros. Esta função recebeu {a} e {b}")
    return a+b-1
num1 = 5
num2 = 4
print(f"Chamando a função: {somarTirandoUm(num1,num2)}")

def exibeNumeros(*num):
    print("Uma função pode receber um número não previamente estabalecido de elementos, desde que isso seja indicado.")
    print(f"Vamos exibir esta lista com {len(num)} números: ", end="")
    for valor in num:
        print(valor, end=" ")
    print("\n")
exibeNumeros(0,2,3)
exibeNumeros(5,1)
exibeNumeros(6,1,2,3,8,1)

def dobra(lst):
    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i += 1
valores = [2, 3, 4, 8, -2, 0]
dobra(valores)
print(f"Funções podem modificar valores de variáveis: {valores}")