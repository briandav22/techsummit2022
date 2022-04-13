from dash import Dash,dash_table, html
import plotly.express as px

def make_fig(df,graph_type):
    if graph_type == 'Line Graph':
        fig = px.line(df, x="name", y="average_utilization", title='Line Graph')
        return fig
    elif graph_type == 'Pie Chart':
        fig = px.pie(df, values='max_flows_in', names='name')
        return fig
        
    elif graph_type == 'Bar Chart':
        fig = px.bar(df, x='name', y='total_flows_in')
        return fig



