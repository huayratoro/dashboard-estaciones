from dash import html, dcc
from components.dropdown import create_dropdown
import pandas as pd
from utils.db_utils import get_db_connection

def create_layout():
    conn = get_db_connection()
    estaciones_disponibles = pd.read_sql('estaciones', conn)
    estaciones = sorted(estaciones_disponibles["nombre"].unique())
    variables = ['temp', 'hr', 'pres']
    
    return html.Div([
        html.H1('Mi segunda aplicación Dash con Plotly'),
        html.H4("Elija una estacion del listado: "),
        create_dropdown('dropdown-nom-estacion', estaciones, estaciones[0]),
        html.H4("Elija una variable del listado: "),
        create_dropdown('dropdown-nom-var', variables, 'temp'),
        html.Button('Generar Grafico', id='boton-generar-grafico', n_clicks=0),
        html.H3("Gráficos"),
        dcc.Graph(id="grafico-primero")
    ])
