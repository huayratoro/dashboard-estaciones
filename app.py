from dash import dcc, html
import dash
from layout.layout import create_layout
from callbacks.callbacks import register_callbacks

# incluyo el CSS de Bootstrap
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Configuramos el layout de la aplicación
app.layout = create_layout()

# Registramos los callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)