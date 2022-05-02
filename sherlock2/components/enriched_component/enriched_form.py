from dash import dcc
import dash_bootstrap_components as dbc

enriched_form = dbc.Form(
    dbc.Row(
        [

            dbc.Col(
            dcc.Dropdown(['1h', '4h','8h', '12h','24h','48h','72h'], '8h', id='enriched_time')),

            dbc.Col(
                dbc.Input(
                    id='customer_id',
                    type="text", 
                    placeholder="Customer ID"),
                    className="me-3",
            
                    
            ),
            dbc.Col(dbc.Button("Submit", color="primary", id='enriched_search'), width="auto"),
        ],
        className="g-2",
    )
)