import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

from dash import dcc,html, dash, Input,Output

import pandas as pd

from fig_maker import make_fig

df = pd.read_csv('data.csv')




app = dash.Dash()

fig = make_fig(df,'Line Graph')

app.layout = html.Div([
    dcc.Graph(id='example_fig',figure=fig),
    dcc.Dropdown(['Pie Chart', 'Line Graph', 'Bar Chart'], 'Line Graph', id='demo-dropdown'),
])


@app.callback(
    Output('example_fig','figure'),
    Input('demo-dropdown','value')
    )

def swap_figure(graph_type):
    fig = make_fig(df,graph_type)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)


