from dash import  dash_table, html



def make_enriched_table(df):

    fig = html.Div([
        dash_table.DataTable(
            id='datatable-interactivity',
            columns=[
                {"name": i, "id": i, "deletable": True, "selectable": True, } for i in df.columns
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
            export_format="csv"

        ),
        
        html.Div(id='datatable-interactivity-container')
    ], id="swap-me")
    return fig

