# Exercício Python #105 - Analisando e gerando Dicionários
# https://www.youtube.com/watch?v=Kbs97l38vVQ

# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
#  e vai retornar um dicionário com as seguintes informações:
#   - Quantidade de notas
#   - A maior nota
#   - A menor nota
#   - A média da turma
#   - A situação (opcional)
#  Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

print("\n#105 - Analisando e gerando Dicionários")
print("--" * 16)

def notas(*numbers, situation=False):
    """
    -> notas: 
    :param *numbers: recebe um número variável de argumentos das notas dos alunos.
    :param situation: parâmetro opcional, indica se a situação do aluno deve ser incorporada ao dicionário. Valor padrão: False
    :return: os dados num formato de dicionário (dados), contendo a maior nota, a menor nota, a média da turma e a situação da turma (opcional).
    """
    dados = {
        'quantidade': len(numbers),
        'maior_nota': max(numbers),
        'menor_nota': min(numbers),
        'media': round(sum(numbers)/len(numbers),2)
    }
    if situation:
        if dados.get('media') <= 4:
            dados['situation'] = "RUIM"
        elif dados.get('media') <= 7:
            dados['situation'] = "ABAIXO DA MÉDIA"
        elif dados.get('media') < 9:
            dados['situation'] = "ADEQUADO"
        else:
            dados['situation'] = "EXCELENTE"
    return dados
    
#Programa principal:
dados = notas(10 ,9.9, 9.9, 9.9, 9.9, 10, 10, 7.6, situation=True)
print(dados)