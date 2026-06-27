import pandas as pd
import numpy as np

df = pd.read_csv('Global_Superstore2.csv', encoding='cp1250')

# Convert date columns to datetime objects
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d-%m-%Y')

# Create new column "Shipment Time"
df['Shipment Time'] = (df['Ship Date'] - df['Order Date']).dt.days

print("[TEST] Checking negative shipping times")
print("Number of orders with negative shipping times:", (df['Shipment Time'] < 0).sum())

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

print('-' * 48)
print("[TEST] Negative financial values test - verify Sales and Quantity columns and check any duplicated data")
print('Negative Sales number:', (df['Sales'] <= 0).sum())
print('Negative Quantity number:', (df['Quantity'] <= 0).sum())
print("Number of duplicated data:", df.duplicated().sum())
print('-' * 48)

# If the above test returns negative values, this line of code will clear them - we overwrite DataFrame
df = df[(df['Sales'] > 0) & (df['Quantity'] > 0)]

# Remove duplicated data
df = df.drop_duplicates()

# print(df.head(5))

# Checking table size
# print(df.shape)

# Display a list of columns, the number of non-null values and data types
# print(df.info())

# print(df.dtypes)

# print(df[['Shipment Time', 'Order Date', 'Ship Date']].describe())

df.to_excel('Global_Superstore_CLEANED.xlsx', index=False, sheet_name='Cleaned_Data')
print('Success! The cleaned file has been saved.')