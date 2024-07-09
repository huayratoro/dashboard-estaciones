from dash.dependencies import Input, Output, State
from data.data_loader import obtener_datos, obtener_posicion_estacion
import plotly.express as px
import plotly.graph_objects as go

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
            # fig_map = px.scatter(posicion, x="longitud", y="latitud")
            fig_map = px.scatter_geo(
                posicion, 
                lat="latitud", lon="longitud",
                title=f'Posicion de la estacion {nombre_estacion}',
                scope="south america",
                center={
                    'lat': posicion['latitud'].iloc[0],
                    'lon': posicion['longitud'].iloc[0]
                }
            )
            # fig_map = go.Figure(
            #     go.Scattermapbox(
            #         lat=float(posicion['latitud'].iloc[0]),
            #         lon=float(posicion['longitud'].iloc[0]),
            #         mode='markers',
            #         marker=go.scattermapbox.Marker(size = 14),
            #         text=[nombre_estacion]
            #     )
            # )

            # fig_map.update_layout(
            #     mapbox_style = 'satellite-streets',
            #     mapbox=dict(
            #         center=go.layout.mapbox.Center(
            #             lat = float(posicion['latitud'].iloc[0]),
            #             lon = float(posicion['longitud'].iloc[0])
            #         ),
            #         zoom = 15
            #     ),
            #     margin={"r":0, "t":0, "l":0, "b":0}
            # )

            return fig_line, fig_box, fig_hist, fig_map
        
        # en el caso que no se hayan hecho clicks, no se retorna graficos
        return {}, {}, {}, {}
