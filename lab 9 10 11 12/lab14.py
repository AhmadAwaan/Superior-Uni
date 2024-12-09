import pandas as pd

# Load the dataset
df = pd.read_csv('suicide-rates.csv')

# Display the first few rows
print(df.head())

# Get a concise summary of the dataset
df.info()

# Identify missing values
print(df.isnull().sum())

# Get column names
print(df.columns)

# Summary of numerical columns
print(df.describe())

# Check how many countries are in the dataset
print(df['Country'].nunique())
