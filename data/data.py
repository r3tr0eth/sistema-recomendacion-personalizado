import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar tus datos
df = pd.read_csv('data/movies2.csv')

# Distribución de Géneros
print(df['Genre'].value_counts())

# Relación entre Rentabilidad y Puntuación de la Audiencia
sns.scatterplot(x='Audience score %', y='Profitability', data=df)

# Histograma de Puntuaciones de Rotten Tomatoes
df['Rotten Tomatoes %'].hist(bins=20)

# Tendencias a lo largo del tiempo
sns.lineplot(x='Year', y='Profitability', data=df)

plt.show()
