from dash import Dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.BOOTSTRAP, "./assets/style.css"]
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
)
app_title = "Sherlock"
app.title = app_title


