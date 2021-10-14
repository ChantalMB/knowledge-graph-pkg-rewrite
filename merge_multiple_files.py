import os, glob
import pandas as pd

path = "/home/cbrou/Desktop/knowledge-graph/data/result"

all_files = glob.glob(os.path.join(path, "*.csv"))
print(all_files)

df_convert = (pd.read_csv(f) for f in all_files)

df_merged = pd.concat(df_convert, ignore_index=True)

df_merged.to_csv( "merged.csv")
