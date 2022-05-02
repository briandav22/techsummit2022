import dash_bootstrap_components as dbc

from dash import dcc




bosun_form = dbc.Form(
    dbc.Row(
        [

            dbc.Col(
            dcc.Dropdown(['1h', '4h','8h', '12h','24h','48h','72h'], '8h', id='bosun_time')),

            dbc.Col(
                dbc.Input(
                    id='bosun-submit',
                    type="text", 
                    placeholder="Customer ID"),
                    className="me-3",
            
                    
            ),

           
            dbc.Col(dbc.Button("Submit", color="primary", id='bosun-search') ),
        ],
        className="g-2",
    )
)
