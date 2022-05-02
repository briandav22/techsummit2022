from dash import  html
#import proxy form

import dash_bootstrap_components as dbc

# from app import proxy_address





cookie_component = dbc.Row(
        [
            

        dbc.Label("Current Cookie:", width="auto"),

        html.Div(children=[],id='current-cookie',className='margin-both')

        ],

    )



