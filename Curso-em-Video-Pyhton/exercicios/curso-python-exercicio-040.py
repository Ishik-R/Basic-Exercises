# Exercício Python #040 - Aquele clássico da Média
# https://www.youtube.com/watch?v=QuWDyUeoaJs

# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

print('\n#040 - Aquele clássico da Média')
print('--' * 16)
print('Insira a nota de duas provas de um aluno:')
p1 = float(input('Nota da prova 1: '))
p2 = float(input('Nota da prova 2: '))
media = (p1+p2)/2

if media >= 7:
    print(f'APROVADO. Média: {media:.2f}\n')
elif media >= 5:
    print(f'RECUPERAÇÃO. Média: {media:.2f}\n')
else:
    print(f'REPROVADO. Média: {media:.2f}\n')