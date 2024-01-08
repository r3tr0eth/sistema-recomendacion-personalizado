import pandas as pd

def load_data(filepath):
    """
    Carga los datos desde un archivo CSV.

    Args:
    filepath (str): Ruta al archivo CSV.

    Returns:
    pandas.DataFrame: Datos cargados en un DataFrame.
    """
    # Cargar datos usando pandas
    data = pd.read_csv(filepath)
    
    # Aquí puedes agregar más procesamiento si es necesario, como:
    # - Limpieza de datos
    # - Transformación de columnas
    # - Manejo de valores faltantes
    # - etc.

    return data

def preprocess_data(data):
    """
    Preprocesa los datos para su uso en el sistema de recomendación.

    Args:
    data (pandas.DataFrame): Datos originales.

    Returns:
    pandas.DataFrame: Datos preprocesados.
    """
    # Realizar preprocesamiento, como:
    # - Normalización
    # - Codificación de categorías (si es necesario)
    # - Reducción de dimensionalidad (opcional)
    # - etc.

    return data

# Aquí puedes agregar más funciones según sea necesario, por ejemplo:
# - División en conjuntos de entrenamiento y prueba
# - Generación de matrices de usuario-ítem
# - etc.

if __name__ == "__main__":
    # Ejemplo de cómo usar estas funciones
    filepath = 'ruta/a/tu/dataset.csv'  # Actualiza esto con la ruta real a tu archivo de datos
    data = load_data(filepath)
    preprocessed_data = preprocess_data(data)

    # Aquí puedes añadir código para visualizar los datos,
    # hacer pruebas básicas, etc.
