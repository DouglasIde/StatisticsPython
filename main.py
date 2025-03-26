import pandas as pd
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/alura-cursos/estatistica-r-frequencias-medidas/refs/heads/main/dados' \
      '/vendas_ecommerce.csv '

# Le o arquivo CSV
df = pd.read_csv(url)

# Exibe as 5 primeiras linhas do DataFrame
df_head = df.head()

# Obtém as dimensões do DataFrame
df_shape = df.shape

# Exibe um resumo do DataFrame, incluindo os tipos de dados
df_info = df.info()

# Filtra os valores únicos da coluna "categoria_produto"
df_filtro_colunas = df['categoria_produto'].unique()
produtos = df['categoria_produto'].value_counts().reset_index()

# Cria um gráfico na horizontal
plt.barh(produtos['categoria_produto'], produtos['count'])
plt.show()

print(produtos)
# print(df_shape)
# print(df_info)
# print(df_head)