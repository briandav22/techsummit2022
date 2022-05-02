
import dash_bootstrap_components as dbc
from dash import  html
from css_styles.sidebar.sidebar_styles import SIDEBAR_STYLE
# from components.theme_select.theme_component import theme_select



sidebar = html.Div(
    [
        html.H2("Sherlock", className="display-4"),

        html.P(
            "Flow Rates are Elementary"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact",id="page-1-link"),
                dbc.NavLink("Bosun Search", href="/bosun", active="exact",id="page-2-link"),
                dbc.NavLink("Enriched Search", href="/meta", active="exact",id="page-3-link"),
                dbc.NavLink("Configuration", href="/config", active="exact",id="page-4-link"),
                # theme_select
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)



# sidebar = html.Div(
#     [
        
        

        
#         dbc.Nav(
#             [
#                 html.Img(src="../../assets/sherlock.png", className="app-header"),
#                 html.Hr(),
#                 dbc.Button("Sidebar", outline=True, color="secondary", className="mr-1", id="btn_sidebar"),
                # dbc.NavLink("Home", href="/", active="exact"),
                # dbc.NavLink("Bosun Search", href="/bosun", active="exact"),
                # dbc.NavLink("Enriched Search", href="/meta", active="exact"),
#             ],
#             vertical=True,
#             pills=True,
#         ),
#     ],
#     style=SIDEBAR_STYLE,
# )
