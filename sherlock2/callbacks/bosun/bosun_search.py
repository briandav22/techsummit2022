#callback that swaps out empty div in boson component with table and graph after 'submit' is clicked and query returns results
from index import app

from dash import  Input, Output, State, callback_context
from dash.exceptions import PreventUpdate


from api_calls.bosun_search import get_customer_data
from make_figures.bosun_fig import make_table


@app.callback(
    Output('boson-swap', 'children'),
    [
    
    Input('bosun-search', 'n_clicks'),
    Input('bosun_time','value'),
    Input('bosun-submit','value')
    ],
    State('config_details', 'data')

)
def bosun_search(n_clicks, bosun_time,value,config_details):

    changed_id = [p['prop_id'] for p in callback_context.triggered][0]

    if n_clicks == 0 or n_clicks == None:
        raise PreventUpdate
    else:

        config_details = config_details['config_details']
        proxy = {
                    'http':config_details['proxy'],
                    'https':config_details['proxy']
                }
        if changed_id == 'bosun-search.n_clicks':
            custom_data = get_customer_data(value, time_range=bosun_time,proxies=proxy)
            fig = make_table(custom_data)
            return fig
        else:
            pass







