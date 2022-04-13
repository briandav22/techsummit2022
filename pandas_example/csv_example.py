import pandas as pd


df = pd.read_csv('data.csv')

print(df.head())
#do a bunch of stuff, then make a new CSV


#filter for devices dropping more then 1k flows 
df = df[df['total_dropped'] > 1000]

#write to a CSV
df.to_csv('flows_dropped.csv', index=False)
