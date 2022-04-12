from dash import dcc,html, dash
import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')

app = dash.Dash()

fig = px.line(df, x="name", y="average_utilization", title='Line Graph')

app.layout = html.Div([
    html.Div('Simple Dash App for Tech Summit 2022'),
    dcc.Graph(figure=fig),
    html.Div('Line Graph showing Average Utilization'),

])


if __name__ == '__main__':
    app.run_server(debug=True)


