# Exercício Python #114 - Site está acessível?
# https://www.youtube.com/watch?v=8jAykqxIeqw

# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

print("\n#114 - Site está acessível?")
print("--" * 16)

def verificador(text):
    """
    -> verificador(str text): verifica se o site passado como parâmetro está online.
    :param text: link para o site a ser analisado.
    :return: nulo, as informações são repassadas por meio do terminal.
    """
    import urllib
    import urllib.request

    try:
        site = urllib.request.urlopen(text)
    except urllib.error.URLError:
        print(f"O site {text} não está acessível no momento")
    else:
        print("O site foi acessado com sucesso")
        #FUNCIONALIDADE EXTRA: print(site.read()) nos mostra todo o conteúdo do site

    
#Programa principal:
site = "http://www.pudim.com.br"
verificador(site)