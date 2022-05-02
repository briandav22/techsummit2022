import dash_bootstrap_components as dbc
from dash import html


query_div = html.Div(id='enriched_show')

enriched_collapse = html.Div(
    [
        dbc.Button(
            "Show Queries",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(query_div)),
            id="collapse",
            is_open=False,
        ),
    ]
)