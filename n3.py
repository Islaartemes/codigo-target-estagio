import json

# Carregar dados de faturamento do arquivo JSON
with open("dados.json", "r") as file:
    faturamento_mensal = json.load(file)

# Extraindo os valores de faturamento (ignorando dias com faturamento igual a 0)
faturamento_diario = [dia["valor"] for dia in faturamento_mensal if dia["valor"] > 0]

# Calculando o menor e o maior valor de faturamento
menor_faturamento = min(faturamento_diario)
maior_faturamento = max(faturamento_diario)

# Calculando a média mensal (ignorando dias sem faturamento)
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Contando o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for valor in faturamento_diario if valor > media_mensal)

# Exibindo os resultados
print(f"Menor valor de faturamento ocorrido em um dia do mês: {menor_faturamento}")
print(f"Maior valor de faturamento ocorrido em um dia do mês: {maior_faturamento}")
print(f"Número de dias no mês com faturamento superior à média mensal: {dias_acima_da_media}")
