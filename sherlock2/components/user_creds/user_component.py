from dash import  html
#import proxy form

import dash_bootstrap_components as dbc

# from app import proxy_address





current_creds = dbc.Row(
        [
            

        dbc.Label("Current Email:", width="auto"),

        html.Div(children=[],id='user-settings',className='margin-both'),

        dbc.Label("Current Token:", width="auto"),
        html.Div(children=[],id='api-settings',className='margin-both')
        ],

    )


