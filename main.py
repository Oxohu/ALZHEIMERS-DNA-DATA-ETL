import pandas as pd

df = pd.read_csv('gene_result.txt', delimiter='\t')
print(df.head())
