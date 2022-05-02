from dash import  html
from components.enriched_component.enriched_form import enriched_form
from components.query_collapse.enriched_show import enriched_collapse

enriched_component = html.Div(
    [
        html.H2("Enriched Data Search", className="display-4"),
        html.Hr(),
        html.P(
            "Use this if you want additional metada from customer portal"
        ),

        enriched_form,
        enriched_collapse,

        html.Div(id='swap-me')


    ],
    
    id = "page-content")