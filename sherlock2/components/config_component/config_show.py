import dash_bootstrap_components as dbc
from dash import html


config_div = html.Div(id='config_show')

config_show = html.Div(
    [
        dbc.Button(
            "Show Config",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            dbc.Card(dbc.CardBody(config_div)),
            id="collapse",
            is_open=False,
        ),
    ]
)