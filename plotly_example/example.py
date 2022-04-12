import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')

print(df.head())

fig = px.pie(df, values='max_flows_in', names='name')

fig.show()