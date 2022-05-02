
import dash_bootstrap_components as dbc

cookie_form = dbc.Row(
        [
            

            dbc.Label("Add Cookie:", width="auto"),
            dbc.Col(
                dbc.Input(
                    id='kentik_cookie',
                    type="text", 
                    placeholder="cookie monster hungry"),
                    className="me-3",
                    
            ),


           
        ],
        className="g-2",
    )
