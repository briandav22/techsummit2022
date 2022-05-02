from dash import  html
import dash_bootstrap_components as dbc
#import proxy form

from components.config_component.config_form import config_form

from components.config_component.config_show import config_show
# from app import proxy_address

config_component = html.Div(
    [
        html.H2("Configuration", className="display-4"),
        html.Hr(),

        config_form,
        config_show
        
        






    ],
    
    id = "proxy-content")


