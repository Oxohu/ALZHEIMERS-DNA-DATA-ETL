import pandas as pd

df = pd.read_csv('genes_result.txt', delimiter='\t')
print(df.head())
