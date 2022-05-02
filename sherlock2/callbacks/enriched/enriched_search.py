from index import app

from dash import  Input, Output,State
import pandas as pd
from api_calls.data_search import DeviceSearch
from api_calls.bosun_search import get_customer_data
from dash.exceptions import PreventUpdate
from make_figures.enriched_fig import enriched_fig
from make_figures.make_enriched_table import make_enriched_table
from make_figures.alert import make_alert

@app.callback(
    Output('swap-me', 'children'),
    [
        Input('enriched_search', 'n_clicks'),
        Input('enriched_time','value'),
        Input('customer_id', 'value'),

    ],
    [State('config_details','data')]
)
def enriched_search(n_clicks, enriched_time,customer_id,config_details ):


    if n_clicks == 0 or n_clicks == None:

        raise PreventUpdate
    else:
        config_details = config_details['config_details']
        email = config_details['email']
        token = config_details['token']
        cooke = config_details['cookie']    
        proxy = {
                'http':config_details['proxy'],
                'https':config_details['proxy']
            }
        

        api_call = DeviceSearch(email,token, customer_id, cooke)
        data_back = api_call.get_device_data()

        if data_back == 'Access Denied':
            return make_alert(f'Received "Access Denied" from Kentik, Most common reason is your cookie has expired. Your current cooke is "{cooke}"')

        plan_object = api_call.create_plan_object(data_back)
        kentik_data = api_call.create_device_objects(plan_object, data_back)
        bosun_data = get_customer_data(customer_id, time_range=enriched_time, proxies=proxy)

        df_enriched = enriched_fig(bosun_data,kentik_data,enriched_time)

        fig = make_enriched_table(df_enriched)

        return fig


        