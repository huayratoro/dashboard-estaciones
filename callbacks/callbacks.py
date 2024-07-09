from dash.dependencies import Input, Output, State
from data.data_loader import obtener_datos
import plotly.express as px

def register_callbacks(app):
    @app.callback(
        [Output('grafico-primero', 'figure'),
        Output('boxplot-general', 'figure'),
        Output('histplot-general', 'figure')],
        Input('boton-generar-grafico', 'n_clicks'),
        State('dropdown-nom-var', 'value'),
        State('dropdown-nom-estacion', 'value')
    )
    def actualizar_grafico(n_clicks, var, nombre_estacion):
        if n_clicks > 0:
            serie = obtener_datos(var, nombre_estacion)

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

            return fig_line, fig_box, fig_hist
        
        # en el caso que no se hayan hecho clicks, no se retorna graficos
        return {}, {}, {}
