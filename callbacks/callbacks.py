from dash.dependencies import Input, Output, State
from data.data_loader import obtener_datos, obtener_posicion_estacion
import plotly.express as px
import os; from dotenv import load_dotenv
import pandas as pd

# Cargo el token de Mapbox 
load_dotenv()
px.set_mapbox_access_token(os.getenv('MAPBOX_TOKEN'))

def register_callbacks(app):
    @app.callback(
        [Output('grafico-primero', 'figure'),
        Output('boxplot-general', 'figure'),
        Output('histplot-general', 'figure'),
        Output('mapa-estacion', 'figure'),
        Output('boxplot-mensual', 'figure')],
        Input('boton-generar-grafico', 'n_clicks'),
        State('dropdown-nom-var', 'value'),
        State('dropdown-nom-estacion', 'value')
    )
    def actualizar_grafico(n_clicks, var, nombre_estacion):
        if n_clicks > 0:
            
            # traemos los datos desde la base
            serie = obtener_datos(var, nombre_estacion)
            posicion = obtener_posicion_estacion(nombre_estacion)

            # pongo como indice las fechas
            serie = serie.set_index(pd.to_datetime(serie.index))

            # agrego una columna con los meses
            serie['mes'] = serie.index.month
            meses_dict = {10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre', 1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril'}
            serie['mes_nombre'] = serie['mes'].map(meses_dict)

            # Grafico de lineas
            fig_line = px.line(
                serie, y=var, title=f'Variacion de {var} para la estacion {nombre_estacion}'
            )

            # Boxplot de la variable total
            fig_box = px.box(
                serie, y=var, title=f'Boxplot de {var} para la estacion {nombre_estacion}'
            )

            # Histograma
            fig_hist = px.histogram(
                serie, x=var, title=f'Histograma de {var} para la estacion {nombre_estacion}',
                nbins=12
            )

            # Mapa de la estacion
            fig_map = px.scatter_mapbox(
                posicion, 
                lat="latitud", lon="longitud",
                title=f'Posicion de la estacion {nombre_estacion}',
                center={
                    'lat': posicion['latitud'].iloc[0],
                    'lon': posicion['longitud'].iloc[0]
                },
                zoom=10, mapbox_style="stamen-terrain",
            )

            # Boxplot de la variable mensual
            fig_box_mensual = px.box(serie, y = var, x="mes_nombre", title=f"Boxplot de {var} para la estacion {nombre_estacion}")

            fig_box_mensual.update_xaxes(categoryorder='array', categoryarray=['Octubre', 'Noviembre', 'Diciembre', 'Enero', 'Febrero', 'Marzo', 'Abril'])

            # retornamos los outputs
            return fig_line, fig_box, fig_hist, fig_map, fig_box_mensual
        
        # en el caso que no se hayan hecho clicks, no se retorna graficos
        return {}, {}, {}, {}, {}
