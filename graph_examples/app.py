
from dash import Dash,dash_table, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('data.csv')

fig = px.line(df, x="name", y="average_utilization", title='Line Graph')

#shows the figure to the browser
fig.show()