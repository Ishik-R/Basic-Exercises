# Curso Python #013 - Estrutura de repetição for
# https://www.youtube.com/watch?v=cL4YDtFnCt4

# Apresentação da estrutura de repetição 'for'

print("\nAULA #013 - Estrutura de repetição for")
print("--" * 16)

for x in range(0,5):
    print('Essa mensagem será exibida 5 vezes')
print('Fim do for\n')

for c in range(6,3,-1):
    print(f'O número da vez é {c}')
    print('Podemos inserir vários comandos dentro do laço!')
print('Fim do for\n')

start = 1
finish = 5
step = 1
for c in range(start, finish, step):
    print(f'Número atual: {c}. Vamos até {finish-1}')
print('Fim do for\n')