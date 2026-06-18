import pandas as pd
import numpy as np

df = pd.read_csv('Global_Superstore2.csv', encoding='cp1250')

# Checking table size
# print(df.shape)

# Display a list of columns, the number of non-null values and data types
# print(df.info())

# Display first 5 rows to investigate values
# print(df.head(5))

# Convert date columns to datetime objects
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')

# Create new column "Shipment Time"
df['Shipment Time'] = df['Ship Date'] - df['Order Date']

"""
Convert selected columns to 'category' dtype to reduce memory usage
and improve performance (especially for groupby operations).
"""

category_type = [
    'Ship Mode', 'Segment', 'Category', 'Sub-Category', 
    'Market', 'Region', 'Country', 'Order Priority'
]

for col in category_type:
    df[col] = df[col].astype('category')

# Convert to string and remove trailing '.0' from nunmeric imports
df['Postal Code'] = df['Postal Code'].astype(str).str.replace('.0', '', regex=False)

# Replace text placeholder for missing values with actual NaN
df['Postal Code'] = df['Postal Code'].replace(['nan', 'NaN', 'NAN', 'None', ''], np.nan)

print(df['Postal Code'].head(5))
# print(df.dtypes)
# print(df[['Shipment Time', 'Order Date', 'Ship Date']].describe())