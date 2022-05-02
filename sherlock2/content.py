# content.py
from index import app
from callbacks.navigation.navigation import navigation
from callbacks.sidebar.collapse_sidebar import toggle_sidebar

from callbacks.bosun.bosun_search import bosun_search
from callbacks.bosun.bosun_table import update_boson_graph, update_boson_styles
from callbacks.enriched.enriched_table import enriched_styles,enriched_table
from callbacks.enriched.enriched_search import enriched_search

from callbacks.configuration.configuration import submit_credentials
from callbacks.configuration.config_show import show_config
from callbacks.collapse.collapse import toggle_collapse

from components.content_component.content_component import content
from components.navbar_component.navbar_component import navbar
from components.sidebar_component.sidebar_component import sidebar
from dash import dcc, html


app.layout = html.Div(
    [
    html.Div(id="blank_output"),
    dcc.Store(id='side_click'),

    dcc.Store(id="config_details",storage_type='local'),
    dcc.Location(id="url"), 
    navbar,
    sidebar, 
    content
    ])