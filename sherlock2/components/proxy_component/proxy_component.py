from dash import  html
#import proxy form

import dash_bootstrap_components as dbc

# from app import proxy_address





current_proxy = dbc.Row(
        [
            

        dbc.Label("Current Proxy:", width="auto"),

        html.Div(children=[],id='proxy-address',className='margin-both')

        ],

    )


example_proxy = dbc.Row(
        [
            

        dbc.Label("Example Proxy:", width="auto"),

         html.P(
                           "socks5h://127.0.0.1:10000"
                        , className='margin-top'),

        ],

    )



