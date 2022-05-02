import dash_bootstrap_components as dbc
from components.proxy_component.proxy_form import proxy_form
from components.cookie_component.cookie_form import cookie_form
from components.config_component.config_submit import config_submit
from components.user_creds.user_form import user_creds
config_form = dbc.Form([
        proxy_form,
        cookie_form,
        user_creds,
        config_submit

           ])
