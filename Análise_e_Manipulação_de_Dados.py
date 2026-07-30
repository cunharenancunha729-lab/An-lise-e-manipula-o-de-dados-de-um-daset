

import pandas as pd
df = pd.read_csv('/content/Vendasloja - Vendasloja.csv')
print(df)

df.head()   #mostrar as  1 linhas
df.tail()   #mostra as ultimas linhas
df.shape    #mostar tamanho da tabela
df.columns   #mostar nome das colunas
df.info()    #informacao da tabela,numero de linhas, colunas, qual tipo de dados

# mostar as  1 linhas
df.head(10)
df.head(8)

df.sample(3)

#mostar colunas
df["Produto"]
df[["Produto", "Categoria"]]
df[["Produto", "Categoria","Preço"]]

#FILTRANDO DADOS

df["Preço"] > 1000

#Valores ausentes

df.isna()

#conta valor ausentes

df.isna().sum()

#tratar valores ausentes

df["Preço"] = df["Preço"].fillna(0)

#valores duplicados

df.duplicated().sum()

#removendo dados duplicados

df = df.drop_duplicates()

#criar coluna total
df["Total de vendas"] = df["Qtd"] * df["Preço"]

total_geral_vendas = df["Total de vendas"].sum()
print(f"Total Geral das Vendas: {total_geral_vendas:.2f}")

media_vendas = df["Total de vendas"].mean()
print(f"Média das Vendas: {media_vendas:.2f}")


maior_venda = df["Total de vendas"].max()
print(f"Maior Venda: {maior_venda:.2f}")


menor_venda = df["Total de vendas"].min()
print(f"Menor Venda: {menor_venda:.2f}")

#agrupar os dados

print('Total vendido por categoria:')
print(df.groupby('Categoria')['Total de vendas'].sum())

print('\nPreço médio por categoria:')
print(df.groupby('Categoria')['Preço'].mean())

print('\nQuantidade média por categoria:')
print(df.groupby('Categoria')['Qtd'].mean())

#Estatísticas

print(f"Maior Preço: {df['Preço'].max()}")
print(f"Menor Preço: {df['Preço'].min()}")
print(f"Soma de Preços: {df['Preço'].sum()}")
print(f"Média de Preços: {df['Preço'].mean()}")

#ordenar dados

df.sort_values("Preço") #ordem crescente
df.sort_values("Preço", ascending=False)

#criar nova coluna

df["Desconto"] = df["Preço"] * 0.10

#salvando as alterações
df.to_csv("Vendasloja_novo.csv", index=False)