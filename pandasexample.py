import pandas as pd
from dash import Dash,dash_table, html
import plotly.express as px




pd.set_option('display.max_columns', None)
some_object = {
'device_id': ['9530', '9533', '11028'],
'name': ['device1', 'device2', 'device3'],
'average_utilization': [94.58, 526.85, 410.78],
'max_flows_in': [95.22, 526.17, 409.88], 
'max_flows_out': [94.58, 526.85, 410.78],
'average_flows_in': [44.47, 287.92, 183.23],
'average_out': [44.5, 287.06, 182.47],
'min_flows_in': [25.43, 171.07, 99.18],
}

app = Dash(__name__)
df = pd.DataFrame(some_object)

def make_enriched_table(df):

    fig = html.Div([
        dash_table.DataTable(

            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True, } for i in df.columns
            ],
            data=df.to_dict('records')

        ),
        

    ])
    return fig


fig = make_enriched_table(df)


app.layout = fig

if __name__ == '__main__':
    app.run_server(debug=True)