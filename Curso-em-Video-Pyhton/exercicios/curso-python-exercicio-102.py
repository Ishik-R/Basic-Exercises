# Exercício Python #102 - Função para Fatorial
# https://www.youtube.com/watch?v=84jUX96cs7Q

# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
#  indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

print("\n#102 - Função para Fatorial")
print("--" * 16)

def fatorial(num, show=False):
    """
    -> fatorial: calcula o fatorial do número recebido
    :param num: número a ser calculado
    :param show: indica se o cálculo do fatorial deve ser exibido (opcional). Valor padrão: False
    :return: o resultado do fatorial (int)
    """
    r = 1
    for i in range(num, 0, -1):
        if show:
            if i > 1:
                print(f"{i} x ", end="")
            else:
                print(f"{i} = ", end="")                
        r = r * i
    return r

n1 = 3
n2 = 4
n3 = 5
print(fatorial(3))
print(fatorial(n2, False))
print(fatorial(n3, True))
