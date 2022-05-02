from dash import html

from components.bosun_component.bosun_form import bosun_form
# from components.query_collapse.query_show_component import collapse


bosun_component = html.Div(
    [
        html.H2("Bosun Search", className="display-4"),
        html.Hr(),
        html.P(
            "Use this is you do not want additional metada from customer portal"
        ),
        
        bosun_form,
        # collapse,
        html.Div(id='boson-swap')
    ],
    
    id = "page-content")