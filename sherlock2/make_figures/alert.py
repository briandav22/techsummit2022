import dash_bootstrap_components as dbc
from dash import html


def make_alert(alert_message):
    alert = html.Div(
        [
            dbc.Alert(
                f"{alert_message}",
                id="alert-fade",
                dismissable=True,
                is_open=True,
            ),

        ]
    )

    return alert