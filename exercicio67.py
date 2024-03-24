#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#A) Apenas os 5 primeiros colocados.
#B) Os Últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) em que posição na tabela está o time do Palmeiras.

clubes = (
    "Athletico-PR",
    "Atlético-GO",
    "Atlético-MG",
    "Bahia",
    "Botafogo",
    "Bragantino",
    "Corinthians",
    "Criciúma",
    "Cruzeiro",
    "Cuiabá",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Palmeiras",
    "São Paulo",
    "Vasco",
    "Vitória"
)

print('OS 5 PRIMEIROS COLOCADOS')
for c in range (0, 5):
    print(f'{c+1}° {clubes[c]}')
print('-=-'*10)

print('OS 4 ULTIMOS COLOCADOS')
for c in range (16, len(clubes)):
    print(f'{c}° {clubes[c]}')
print('-=-'*10)

print('LISTA ORDENADA')
print(sorted(clubes))
print('-=-'*10)

print(f'E O PALMEIRAS ESTA NA {clubes.index('Palmeiras')}° POSIÇÃO')