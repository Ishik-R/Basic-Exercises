# Curso Python #21 - Funções (Parte 2)
# https://www.youtube.com/watch?v=etjJ_4Eqrk8

# Utilização de docstrings, argumentos, escopos de variáveis e retorno de resultados.

print("\n#21 - Funções (Parte 2)")
print("--" * 16)

# AJUDA INTERATIVA
#  O Python fornece informações sobre seus recursos por meio da função help, que pode ser acessada de duas maneiras:
#   - utilizando o comando help()
#   - pedindo para o programa printar as informações desejadas 
#
# help(input)
# print(input.__doc__)

# DOCSTRINGS
def ola(s):
    """
    DOCSTRING:
    Esta é uma função que retorna um simples olá com base no nome inserido.

    É possível inserir informações para serem repassadas quando o help() for chamado.
    :param s: String com o nome a ser exibido na tela
    :return: sem retorno
    """
    print(f"Olá {s}!")

ola("Fulano")
help(ola)

# PARÂMETROS OPCIONAIS E RETURN
def somar(a,b,c=0):
    return a+b+c

print(f"A função funciona adequadamente quando os três valores são informados: {somar(1,2,4)}")
print(f"E a função funciona também quando o valor c não é informado: {somar(2,3)}")
print(f"É possível especificar qual variável recebe cada valor: {somar(c=2, a=1, b=3)}\n")

# ESCOPOS LOCAIS E GLOBAIS
def teste(n):
    x = 7
    global y
    y = 3
    print(f"Dentro da função teste, x vale {x}")
    print(f"Dentro da função teste, n vale {n}")
    print(f"Dentro da função teste, y vale {y}")

n = 5
x = 4
y = 2
teste(n)
print(f"Fora da função teste, x vale {x}")
print(f"Fora da função teste, n vale {n}")
print(f"Fora da função teste, y vale {y}\n")