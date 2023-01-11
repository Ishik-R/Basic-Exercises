# Curso Python #22 - Módulos e Pacotes
# https://www.youtube.com/watch?v=s3r8_Aug4y8

# Criação de módulos e agrupamento de módulos em pacotes. Reutilização e modularização de código.

print("\n#22 - Módulos e Pacotes")
print("--" * 16)

# MODULARIZAÇÃO: criação de funções em locais separados do arquivo principal, que são posteriormente importados conforme o necessário.
import uteis22

# É possível também importar funcionalidades específicas de outros arquivos:
# from uteis import fatorial, dobro

n = int(input("Digite um valor inteiro: "))
print(f"O fatorial de {n} vale {uteis22.fatorial(n)}")
print(f"O dobro de {n} vale {uteis22.dobro(n)}")

# É interessante especificar a chamada de funções já que diferentes imports podem ter funções de mesmo nome.
#  - uteis.fatorial(n) ao invés de fatorial(n)

# O agrupamento de diversos conjuntos de módulos são considerados PACOTES.
# Por exemplo: Dentro do pacote UTEIS podemos ter diversos diretórios, contendo diferentes MÓDULOS.
#  - para a criação de pacotes, é necessária a presença de um arquivo '__init__.py', acompanhando a presença de outros pacotes e módulos.
#  - este recurso é interessante para projetos cuja escala de funções específicas seja gigantesca, otimizando a organização do projeto.