
import dash_bootstrap_components as dbc

proxy_form =dbc.Row(
        [
            

            dbc.Label("Add Proxy:", width="auto"),
            dbc.Col(
                dbc.Input(
                    id='proxy_address',
                    type="text", 
                    placeholder="socks5h://127.0.0.1:10000"),
                    className="me-3",
                    
            ),


            
        ],
        className="g-2",
    
)


