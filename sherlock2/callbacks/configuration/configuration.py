from index import app

from dash import  html, Input, Output,State, callback_context


@app.callback(Output('config_details', 'data'),
                [
                    Input('kentik_cookie','value'),
                    Input('proxy_address','value'),
                    Input('user_email','value'),
                    Input('user_token','value'),
                    Input('config_submit','n_clicks')
                    ],
                State('config_details', 'data'))
def submit_credentials(cookie,proxy,email,token,n_clicks,config_data):
    
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]


    if changed_id == 'config_submit.n_clicks':



        config_data = config_data or {'config_details':{'cookie': 'NO_COOKIE','proxy':'NO_PROXY','email':'NO_EMAIL','token':"NO_TOKEN"}}
        if proxy == None:
            proxy = config_data['config_details']['proxy']
        if cookie == None:
            cookie = config_data['config_details']['cookie']
        if email == None:
            email = config_data['config_details']['email']
        if token == None:
            token = config_data['config_details']['token']


        config_data['config_details'] = {
            "cookie":cookie,
            "proxy":proxy,
            "email":email,
            "token":token
        }


        return config_data
    

    return  config_data or {'config_details':{'cookie': 'NO_COOKIE','proxy':'NO_PROXY','email':'NO_EMAIL','token':"NO_TOKEN"}}



        

