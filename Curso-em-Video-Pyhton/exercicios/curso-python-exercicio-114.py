# Exercício Python #114 - Site está acessível?
# https://www.youtube.com/watch?v=8jAykqxIeqw

# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

print("\n#114 - Site está acessível?")
print("--" * 16)

def verificador(text):
    """
    -> leiaInt: esta função recebe uma entrada por parte do usuário e a retorna se o valor for um número inteiro.
     Enquanto o valor repassado não for um número inteiro a função deverá solicitar uma nova entrada.
    :param msg: mensagem padrão de solicitação de entrada.
    :return: n, se n for um número inteiro. Caso contrário, a função deve solicitar uma nova entrada.
    """
    import urllib
    import urllib.request

    try:
        site = urllib.request.urlopen(text)
    except urllib.error.URLError:
        print(f"O site {text} não está acessível no momento")
    else:
        print("O site foi acessado com sucesso")

    
#Programa principal:
site = "http://www.pudim.com.br"
verificador(site)