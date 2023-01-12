# Curso Python #23 - Tratamento de Erros e Exceções
# https://www.youtube.com/watch?v=xz2B3bfNjEk

# Análise das exceções retornadas pelo Python e dos possíveis tratamentos para estas exceções por meio do try/except.

print("\n#23 - Tratamento de Erros e Exceções")
print("--" * 16)

# EXCEÇÕES
#   Muitas vezes podemos nos deparar com cenários nos quais o programa encontra alguma dificuldade em prosseguir. 
#   Vamos observar alguns dos possíveis retornos por parte de nosso compilador.

# NameError
#   print(x) sem declarar a variável 'x' retorna este erro

# ValueError
#   Ao repassar uma string para uma variável que espera um int, temos este erro:
#   n = int(input('Insira um número')) - e o usuário digita 'oito'

# ZeroDivisionError
#   r = a/b retorna um erro se 'b' for zero, já que a divisão por zero não é determinada nos números reais.

# TypeError
#   r = 2/'2' retorna este erro já que o numerador recebe uma string, que não é manipulável para uma operação matemática.

# IndexError
#   Considerando as seguintes linhas de código:
#       lst=[3,4,1]
#       print(lst[3])
#   É notável que nossa lista não possui nenhum elemento no índice 3, o que é indicado pelo nome do erro.

# ModuleNotFoundError
#   Ocorre quando tentamos realizar o import de um módulo que por algum motivo não é encontrado.

# TRY/EXCEPT
#   Para o tratamento de erros podemos utilizar o recurso try/except/else/finally.
#       - try: seção do código que tenta ser executada.
#       - except: seção do código que é executada quando ocorre um problema na seção 'try'. 
#       - else: seção do código que é executada quando a seção 'try' é executada sem nenhuma exceção comprometedora. Opcional.
#       - finally: seção do código que é executada sempre, independente da ocorrência do erro ou não. Opcional.
#
#   A seção contendo 'except' pode retornar o erro passando-a para uma variável através de:
#       - except Exception as nome_da_variavel
#
#   É possível também criar diversos 'except's para diferentes tipos de erro:
#       - except ZeroDivisionError
#       = except KeyboardInterrupt
#       - except (ValueError, TypeError)

print('Vamos realizar uma divisão. Se você quiser pode inserir o valor 0 no denominador e ver o que acontece.')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro:
    print(f'HOUVE UM PROBLEMA! A EXCEÇÃO ENCONTRADA FOI {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Fim do programa')