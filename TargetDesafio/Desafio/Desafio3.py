import json

# Leitura dos dados de faturamento de um arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Lista para armazenar os valores de faturamento diário
faturamento_diario = []

# Filtra os dias com faturamento
for item in dados:
    if item['valor'] > 0:  # Ignorar dias sem faturamento
        faturamento_diario.append(item['valor'])

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calcula a média mensal de faturamento
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Contar o número de dias com faturamento acima da média mensal
dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

# Exibe os resultados
print(f"Menor valor de faturamento diário: {menor_faturamento}")
print(f"Maior valor de faturamento diário: {maior_faturamento}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_media}")
