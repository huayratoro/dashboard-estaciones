from dash import dcc, html
import dash
from layout.layout import create_layout
from callbacks.callbacks import register_callbacks

app = dash.Dash(__name__)

# Configuramos el layout de la aplicación
app.layout = create_layout()

# Registramos los callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
