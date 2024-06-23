import pandas as pd

# Load the dataset
df = pd.read_csv('titanic_train.csv')

# Display the first few rows
print(df.head())

# Display summary statistics
print(df.describe())

# Display information about the dataset
print(df.info())
