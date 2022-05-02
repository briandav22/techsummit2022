
from dash import dcc
from assets.themes import themes_list, themes
import dash_bootstrap_components as dbc

theme_select = dcc.Dropdown(
    id="themes",
    options=[{"label": str(i), "value": i} for i in themes_list],
    value="BOOTSTRAP",
    clearable=False,
    className="nav-right"
    
)

