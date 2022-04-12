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



10.131.1.133/32, 
10.136.86.21/32, 
10.38.33.56/32, 
10.48.33.15/32, 
10.66.0.31/32, 
10.68.0.20/32, 
10.7.0.5/32, 
172.28.0.99/32, 
172.28.28.24/32, 
172.28.4.36/32, 
172.28.8.29/32


10.34.10.4 - 172.28.8.29