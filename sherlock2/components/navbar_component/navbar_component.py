import dash_bootstrap_components as dbc


navbar = dbc.NavbarSimple(
    children=[


        dbc.Button("Sidebar",  id="btn_sidebar"),
    ],
    brand="Sherlock",
    brand_href="/",
    color="primary",
    dark=True,
    className='no-margin'
 
)


#




