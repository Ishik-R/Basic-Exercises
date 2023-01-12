# Exercício Python #113 - Funções aprofundadas em Python
# https://www.youtube.com/watch?v=KowQ_UIMuI8

# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
#  incluindo agora a possibilidade da digitação de um número de tipo inválido.
#  Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

print("\n#113 - Funções aprofundadas em Python")
print("--" * 16)

def leiaInt(msg):
    """
    -> leiaInt: esta função recebe uma entrada por parte do usuário e a retorna se o valor for um número inteiro.
     Enquanto o valor repassado não for um número inteiro a função deverá solicitar uma nova entrada.
    :param msg: mensagem padrão de solicitação de entrada.
    :return: n, se n for um número inteiro. Caso contrário, a função deve solicitar uma nova entrada.
    """
    while True:
        try:
            n = int(input(msg))
        except:
            print("ERRO! Digite um número inteiro válido.")
        else:
            return n

def leiaFloat(msg):
    '''
    -> leiaFloat: recebe uma string para ser exibida como mensagem de solicitação para a entrada de um número real válido.
     Enquanto o valor entrado não for válido a função deverá solicitar uma nova entrada.
    :param msg: mensagem para solicitar a entrada.
    :return: n, um valor real.
    '''
    while True:
        try:
            n = float(input(msg).replace(',','.'))
        except:
            print("ERRO! Digite um número real válido.")
        else:
            return n
    
#Programa principal:
n = leiaInt("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}.")
m = leiaFloat("Digite um número real: ")
print(f"Você acabou de digitar o número {m}")