from index import app
from components.home_component.homepage import homepage
from components.bosun_component.bosun_component import bosun_component 
from components.config_component.config_component import config_component
from components.enriched_component.enriched_component import enriched_component

from dash import  html, Input, Output
import dash_bootstrap_components as dbc

#callbacks that swap pages from when you click navbar links.
@app.callback(Output("content", "children"), [Input("url", "pathname")])
def navigation(pathname):
    if pathname == "/":
        return homepage
    elif pathname == "/bosun":
        return bosun_component
    elif pathname == "/meta":
        return enriched_component
    elif pathname == "/config":
        return config_component
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )