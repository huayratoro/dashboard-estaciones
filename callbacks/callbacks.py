from dash.dependencies import Input, Output, State
from data.data_loader import obtener_datos, obtener_posicion_estacion
import plotly.express as px
import plotly.graph_objects as go
import os; from dotenv import load_dotenv

# Cargo el token de Mapbox 
load_dotenv()
px.set_mapbox_access_token(os.getenv('MAPBOX_TOKEN'))

def register_callbacks(app):
    @app.callback(
        [Output('grafico-primero', 'figure'),
        Output('boxplot-general', 'figure'),
        Output('histplot-general', 'figure'),
        Output('mapa-estacion', 'figure')],
        Input('boton-generar-grafico', 'n_clicks'),
        State('dropdown-nom-var', 'value'),
        State('dropdown-nom-estacion', 'value')
    )
    def actualizar_grafico(n_clicks, var, nombre_estacion):
        if n_clicks > 0:
            
            # traemos los datos desde la base
            serie = obtener_datos(var, nombre_estacion)
            posicion = obtener_posicion_estacion(nombre_estacion)

            # Grafico de lineas
            fig_line = px.line(
                serie, title=f'Variacion de {var} para la estacion {nombre_estacion}'
            )

            # Boxplot
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

            # retornamos los outputs
            return fig_line, fig_box, fig_hist, fig_map
        
        # en el caso que no se hayan hecho clicks, no se retorna graficos
        return {}, {}, {}, {}
