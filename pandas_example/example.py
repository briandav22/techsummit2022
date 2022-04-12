import pandas as pd


# some object that we have a need to make a dataframe out of. 
some_object = {
'device_id': ['9530', '9533', '11028'],
'name': ['device1', 'device2', 'device3'],
'average_utilization': [94.58, 526.85, 410.78],
'max_flows_in': [95.22, 526.17, 409.88], 
'max_flows_out': [94.58, 526.85, 410.78],
'average_flows_in': [44.47, 287.92, 183.23],
'average_out': [44.5, 287.06, 182.47],
'min_flows_in': [25.43, 171.07, 99.18],
}

df = pd.DataFrame(some_object)

print(df.head())


