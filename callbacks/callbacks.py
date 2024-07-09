from dash.dependencies import Input, Output, State
from data.data_loader import obtener_datos
import plotly.express as px

def register_callbacks(app):
    @app.callback(
        Output('grafico-primero', 'figure'),
        Input('boton-generar-grafico', 'n_clicks'),
        State('dropdown-nom-var', 'value'),
        State('dropdown-nom-estacion', 'value')
    )
    def actualizar_grafico(n_clicks, var, nombre_estacion):
        if n_clicks > 0:
            serie = obtener_datos(var, nombre_estacion)
            fig = px.line(
                serie, title=f'Variacion de {var} para la estacion de {nombre_estacion}'
            )
            fig.update_traces(connectgaps=False)
            return fig
        return {}
