import pandas as pd

# Reemplaza 'ruta/al/archivo.csv' con la ruta real a tu archivo CSV
file_path = './data/movies.csv'

# Paso 1: Cargar el archivo CSV
df = pd.read_csv(file_path)

# Paso 2: Inspeccionar los datos
print(df.head())  # Ver las primeras filas
print(df.dtypes)  # Verificar los tipos de datos

# Paso 3: Limpieza de datos (si la columna es de tipo object/string)
# Eliminar el signo de porcentaje y convertir a float

# Paso 4: Comprobar valores anómalos
print(df['Audience score %'].max())  # Encuentra el valor máximo

# Paso 5: Análisis descriptivo
print(df['Audience score %'].describe())  # Resumen estadístico

# Paso 6: Visualización
df['Audience score %'].hist()  # Crea un histograma

# Si estás en un entorno de notebook, como Jupyter, añade esta línea para mostrar la gráfica
# plt.show()

# Paso 7: Manejo de datos faltantes o incorrectos
# Esto reemplazará los valores faltantes con la media de la columna, por ejemplo.
# Puedes elegir otro método si lo prefieres.
df['Audience score %'].fillna(df['Audience score %'].mean(), inplace=True)

# Paso 8: Guardar el DataFrame limpio en un nuevo archivo CSV
df.to_csv('./data/movies2.csv', index=False)
