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
        # titulo general
        html.H1('Visualizador de datos de estaciones meteorologicas', className='text-center my-4'),
        html.H2('Solo hay datos entre los meses de Octubre a Abril', className='text-center my-4'),
        # formularios
        html.Div([
            html.H4("Elija una estacion del listado: ", className='mt-4'),
            create_dropdown('dropdown-nom-estacion', estaciones, estaciones[0]),
        ], className='col-md-6'),
        html.Div([
            html.H4("Elija una variable del listado: ", className='mt-4'),
            create_dropdown('dropdown-nom-var', variables, 'temp'),
        ], className='col-md-6'),
        # boton de generar grafico
        html.Div([
            html.Button('Generar Graficos', id='boton-generar-grafico', n_clicks=0, className='btn btn-primary my-4'),
        ], style={'padding': "10px", 'display': 'flex', 'text-align': 'center'}),
        # contenedor de los graficos
        html.Div([
            html.H3("Gráficos", className='text-center my-4'),
            # info general de la estacion
            html.Div([
                # Mapa de la estacion
                dcc.Graph(id='mapa-estacion', style={'width': '35%'}),
                # Serie temporal de la variable para todo el periodo
                dcc.Graph(id="grafico-primero", style={'width': '65%'}),
            ], className='row'),
            html.Div([
                # Boxplot
                dcc.Graph(id="boxplot-general", style={"width" : "40%"}),
                # Histplot
                dcc.Graph(id="histplot-general", style={"width" : "60%"})
            ], style={"display": "flex"}),
            html.Div([
                # Boxplots con la distribucion de la variable por cada mes
                dcc.Graph(id="boxplot-mensual")
            ])
        ]),
    ])