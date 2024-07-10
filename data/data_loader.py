import pandas as pd
from utils.db_utils import get_db_connection

def obtener_datos(var, nombre_estacion):
    conn = get_db_connection()
    estaciones_disponibles = pd.read_sql('estaciones', conn)
    codeEst = estaciones_disponibles.loc[estaciones_disponibles.nombre == nombre_estacion]["code"].iloc[0]
    query = f"select {var}, fecha from smn where code = {codeEst}"
    df = pd.read_sql_query(query, conn, index_col="fecha")
    return df

def obtener_posicion_estacion(nombre_estacion):
    conn = get_db_connection()
    estaciones_disponibles = pd.read_sql('estaciones', conn)
    posicion = estaciones_disponibles.loc[estaciones_disponibles.nombre == nombre_estacion][["longitud", "latitud"]]
    return posicion