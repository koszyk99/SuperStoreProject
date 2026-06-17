import pandas as pd
import numpy as np

df = pd.read_csv('Global_Superstore2.csv', encoding='cp1250')

# Checking table size
# print(df.shape)

# Display a list of columns, the number of non-null values and data types
# print(df.info())

# Display first 5 rows to investigate values
print(df.head(5))