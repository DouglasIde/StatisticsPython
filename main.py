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

# Manipulando dados qualitativos ordinais
sorted(df['avaliacao'].unique())

df['avaliacao_indicador'] = pd.Categorical(
    df['avaliacao'],
    categories=[1, 2, 3, 4, 5],
    ordered=True
)

avaliacao_labels = {1: 'Péssimo', 2: 'Ruim', 3: 'Regular', 4: 'Bom', 5: 'Ótimo'}
df['avaliacao_indicador'] = df['avaliacao_indicador'].map(avaliacao_labels)

# Remoção dos valores duplicados de Avaliação e Avaliação Indicador
df_unico = df[['avaliacao', 'avaliacao_indicador']].drop_duplicates()
print(df_unico)

# Cria um gráfico na horizontal
plt.barh(produtos['categoria_produto'], produtos['count'])
# plt.show()

# print(produtos)
# print(df_shape)
# print(df_info)
# print(df_head)
