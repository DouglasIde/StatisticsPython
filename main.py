import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/estatistica-r-frequencias-medidas/refs/heads/main/dados' \
      '/vendas_ecommerce.csv '

df = pd.read_csv(url)

df_head = df.head()
df_shape = df.shape
df_info = df.info()


print(df_shape)
print(df_info)
print(df_head)