# Dashboard de estaciones meteorologicas con Plotly, Dash y PostgreSQL

## Descripción

Esta aplicación web interactiva está diseñada para visualizar datos meteorológicos de diferentes estaciones. Desarrollada con Dash y Plotly, la aplicación permite a los usuarios seleccionar una estación y una variable meteorológica para generar gráficos dinámicos y visualmente atractivos. La interfaz es fácil de usar y permite obtener insights rápidamente a partir de los datos meteorológicos disponibles.

## Características

- **Selección de Estaciones:** Permite seleccionar una estación meteorológica de una lista desplegable.
- **Selección de Variables:** Permite seleccionar una variable meteorológica (temperatura, humedad relativa, presión) de una lista desplegable.
- **Generación de Gráficos:** Al presionar el botón "Generar Gráfico", se crea un gráfico de línea que muestra la variación de la variable seleccionada para la estación elegida.
- **Conexión a Base de Datos:** La aplicación se conecta a una base de datos PostgreSQL para obtener los datos meteorológicos.


## Configuración

### Requisitos Previos

- Python 3.x
- PostgreSQL

### Instalación

1. Clona el repositorio:

2. Crea un entorno virtual e instálalo:
   ```python 
    python -m venv nom_venv
    source nom_venv/bin/activate
    pip install -r requirements.txt

3. Configura las variables de entorno

4. Ejecuta la aplicación:
   ```python
    python app.py

## Uso

Abre tu navegador web y ve a http://127.0.0.1:8050.

Selecciona una estación de la lista desplegable.

Selecciona una variable (temperatura, humedad relativa, presión) de la lista desplegable.

Haz clic en el botón "Generar Gráfico" para visualizar los datos.