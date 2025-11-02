from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, 
           use_pages=True, 
           external_stylesheets=[dbc.themes.CYBORG, dbc.icons.FONT_AWESOME],
           suppress_callback_exceptions=True)

server = app.server
