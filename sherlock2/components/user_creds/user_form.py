
import dash_bootstrap_components as dbc


user_creds = dbc.Row(
        [

        dbc.Label("Enter Credentials:", width="auto"),

            dbc.Col(
                dbc.Input(
                    id='user_email',
                    type="text", 
                    placeholder="Enter Email"),
                    className="me-3",
                    
            ),

            dbc.Col(
                dbc.Input(
                    id='user_token',
                    type="text", 
                    placeholder="Enter Api-Key"),
                    className="me-3",
                    

            )
           
        ],
        className="g-2",
    )
