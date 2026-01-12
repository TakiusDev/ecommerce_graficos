import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('C:/Users/sidne/Documents/EBAC/Exercícios/ecommerce_preparados.csv')
print(df.head(20).to_string())

# Tratamento
print('Qtd: ', df.shape)
print('Tipagem:\n', df.dtypes)
print('Valores nulos:\n', df.isnull().sum())


# Gráfico de barras
plt.figure(figsize = (10, 6))
df['Material'].value_counts().head(10).plot(kind = 'bar', color = '#90ee70')
plt.title('Top 10 Materiais Vendidos')
plt.xlabel('Tipo')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)
plt.show()

#Gráfico Dispersão e Histograma
sns.pairplot(df[['Preço', 'Material_Cod']])
plt.show()

x = df['Marca'].value_counts().head(10).index
y = df['Nota'].value_counts().head(10).values

# Gráfico de pizza
plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)  # Porcentagem para Marcas com melhores Avaliações
plt.title('Marcas com Melhores Avaliações')
plt.show()

#Mapa de Calor
corr = df[['Qtd_Vendidos_Cod', 'N_Avaliações']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação Quantidade de Vendas e Avaliações')
plt.show()

# Gráfico de Densidade
plt.figure(figsize = (10, 6))
sns.kdeplot(df['N_Avaliações'], fill = True, color = '#863e9c')
plt.title('Densidade de Quantidade de Avaliações')
plt.xlabel('Qtd de Avaliações')
plt.show()

# Gráfico de Regressão
sns.regplot(x = 'Nota', y = 'N_Avaliações', data = df, color = '#278f65', scatter_kws = {'alpha' : 0.5, 'color': '#34c289'})
plt.title('Regressão Notas por Avaliações')
plt.xlabel('Nota')
plt.ylabel('Quantidade de Avaliações')
plt.show()