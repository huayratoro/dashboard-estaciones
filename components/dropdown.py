from dash import dcc

def create_dropdown(id, options, default_value):
    return dcc.Dropdown(
        id=id,
        options=[{'label': opt, 'value': opt} for opt in options],
        value=default_value,
        multi=False
    )
