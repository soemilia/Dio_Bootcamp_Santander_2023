# Importe as bibliotecas necessárias
import pandas as pd

# Etapa de Extração: Extraia dados de vendas de um arquivo CSV
df = pd.read_csv('vendas.csv')

# Etapa de Transformação: Calcule o total de vendas para cada produto
df['Total de Vendas'] = df['Quantidade'] * df['Preço Unitário']

# Etapa de Carregamento: Salve os dados transformados em um novo arquivo CSV
df.to_csv('vendas_transformadas.csv', index=False)

print("Processo ETL concluído com sucesso! Os dados transformados foram salvos em 'vendas_transformadas.csv'.")

