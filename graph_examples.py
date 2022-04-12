import pandas as pd
from dash import Dash,dash_table, html
import plotly.express as px



df = pd.read_csv('data.csv')


df = df[['name','max_flows_in']]

print(df.head())

# fig = px.line(df, x="name", y="average_utilization", title='Line Graph')

# fig.show()

# fig = px.pie(df, values='max_flows_in', names='name')



# fig.show()