import pandas as pd

df = pd.read_csv('data.csv')

print(df.head())

#do a bunch of stuff, then make a new CSV
pd.to_csv('new_data.csv')
