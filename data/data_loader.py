import pandas as pd

# Reemplaza 'ruta/al/archivo.csv' con la ruta real a tu archivo CSV
file_path = 'data/movies.csv'

# Leer el archivo CSV
data = pd.read_csv(file_path)

# Ver las primeras filas
print("Primeras filas:")
print(data.head())

# Ver las últimas filas
print("\nÚltimas filas:")
print(data.tail())

# Comprobar los tipos de datos
print("\nTipos de datos:")
print(data.dtypes)

# Buscar valores faltantes
print("\nValores faltantes por columna:")
print(data.isnull().sum())

# Resumen estadístico
print("\nResumen estadístico:")
print(data.describe())
