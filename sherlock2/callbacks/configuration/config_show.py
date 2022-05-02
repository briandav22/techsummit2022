
from index import app

from dash import dash, dcc, html, Input, Output, State
from dash.exceptions import PreventUpdate

@app.callback(
    Output('config_show', 'children'),
    [
    
    Input('config_details', 'modified_timestamp'),
    ],
    State('config_details', 'data')


)
def show_config(ts, config_details):

    conf = config_details['config_details']

    if ts is None:
        raise PreventUpdate


    return (html.Div(children=[ 
            html.P('Current Proxy: ' +  str(conf['proxy'])),
            html.P('Current Email:  ' +  str(conf['email'])),
            html.P('Current Token:  ' +  str(conf['token'])),
            html.P('Current Cookie:  ' +  str(conf['cookie'])),
        ])
        
        )

