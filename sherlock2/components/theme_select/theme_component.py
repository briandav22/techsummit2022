from dash import  html
#import proxy form
from components.theme_select.theme_selector import theme_select
import dash_bootstrap_components as dbc
# from app import proxy_address

theme_component = dbc.Row(
        [
            

        dbc.Label("Choose Theme:", width="auto"),


        theme_select
        ],

    )
