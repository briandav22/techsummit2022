from plotly import graph_objs as go
import pandas as pd
from dash import Dash, dash_table, dcc, html


def make_enriched_table(df):
    fig = html.Div([
        dash_table.DataTable(
            id='bosun-interactivity',
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": True, "type":"numeric"} for i in df.columns
            ],
            data=df.to_dict('records'),

            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="single",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 10,
            style_table={'overflowX': 'auto','overflowY':'auto'},
            export_format="csv",
            style_data={
                'color': 'black',
                'backgroundColor': 'white'
            }
        ),
        
        html.Div(id='bosun-interactivity-container')
    ])
    return fig


def round_num(num):
    num = str(round(num,2))
    return num

def dropnested(alist):
    outputdict = {}
    for dic in alist:
        for key, value in dic.items():
            if isinstance(value, dict):
                for k2, v2, in value.items():
                    outputdict[k2] = outputdict.get(k2, []) + [v2]
            else:
                outputdict[key] = outputdict.get(key, []) + [value]
    return outputdict    



def make_table(bosun_data):
    devices = list(bosun_data.keys())
    final_data = []

    for device in devices:
        #queries stored here, don't parse them as part of metadata parse
        if device != 'bosun_queries':
            device_id = device
            #flows in 
            max_flows_in = bosun_data[device_id]['max_flows'] 
            min_flows = bosun_data[device_id]['min_flows'] 
            average_flows = bosun_data[device_id]['average']  
            total_in = bosun_data[device_id]['total_flows'] 

            #flows out
            max_flows_out = bosun_data[device_id]['max_flows_out'] 
            min_out = bosun_data[device_id]['min_flows_out'] 
            average_out = bosun_data[device_id]['average_out']
            total_out = bosun_data[device_id]['total_out'] 



            device_for_graph = {device_id:{
            "device_id":'id_' + str(device_id),
            'max_flows_in' : max_flows_in,
            'max_flows_out' : max_flows_out,
            'average_flows_in' : average_flows,
            'average_flows_out' : average_out,
            'min_flows_in' : min_flows,
            'min_flows_out' : min_out,
            'total_flows_in' : total_in,        
            'total_flows_out' : total_out,
            'total_dropped' : round_num(float(total_in) - float(total_out))
            }}
            final_data.append(device_for_graph)


    final = dropnested(final_data)

    
    df = pd.DataFrame(final)

    
    fig = make_enriched_table(df)

    
    return fig




