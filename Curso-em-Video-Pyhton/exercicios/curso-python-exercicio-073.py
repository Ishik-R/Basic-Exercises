# Exercício Python #073 - Tuplas com Times de Futebol
# https://www.youtube.com/watch?v=RexybLcGewA

# Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
#  Depois mostre:
#  a) Os 5 primeiros times.
#  b) Os últimos 4 colocados.
#  c) Times em ordem alfabética. 
#  d) Em que posição está o time da Chapecoense.

print("\n#073 - Tuplas com Times de Futebol")
print("--" * 16)

brasileirao_2022 = ('Palmeiras','Flamengo','Fluminense','Corinthians','Internacional',
'Atlethico-PR','Atlético-MG','Santos','América-MG','Goiás','Bragantino','Fortaleza','São Paulo',
'Botafogo','Ceará','Coritiba','Cuiabá','Avaí','Atlético-GO','Juventude')
print(f"Classificação do Brasileirão 2022 neste momento: {brasileirao_2022}")
print(f"Os quatro primeiros: {brasileirao_2022[0:5]}")
print(f"Os quatro últimos: {brasileirao_2022[-4:]}")
print(f"Times em ordem alfabética: {sorted(brasileirao_2022)}")
print(f"O Botafogo está na {brasileirao_2022.index('Botafogo')} posição.")