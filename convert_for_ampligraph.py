import pandas as pd

df = pd.read_csv("merged.csv")

df_formatted = df[['Entity 1','Relationship','Entity2']]

df_formatted['Relationship'] = df_formatted['Relationship'].str.strip().str.replace(' ', '_').str.upper()

df_formatted.to_csv("ampligraph_format.csv", header=None, index=None)
