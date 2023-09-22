#Data Structures
import numpy as np
import pandas as pd

# Create a DataFrame from a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 25},
    {'Name': 'Bob', 'Age': 30},
    {'Name': 'Charlie', 'Age': 35}
]
df = pd.DataFrame(data)

print(df)

######################################################################################

#Data exploration

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'Salary': [50000, 60000, 75000, 52000, 80000]}
df = pd.DataFrame(data)

# Slicing: Select specific rows and columns
slice_df = df.loc[1:3, ['Name', 'Age']]

# Filtering: Select rows based on a condition (e.g., Age > 30)
filtered_df = df[df['Age'] > 30]

# Aggregation: Calculate statistics (e.g., mean and max)
age_mean = df['Age'].mean()
max_salary = df['Salary'].max()

print("Original dataframe:")
print(df)

print("Sliced DataFrame:")
print(slice_df)
print("\nFiltered DataFrame:")
print(filtered_df)
print("\nAge Mean:", age_mean)
print("Max Salary:", max_salary)

###################################################################################

#Data Cleaning

# Create a DataFrame with missing values
data = {'A': [1, 2, None, 4]}
df = pd.DataFrame(data)

# Fill missing values with a specific value (e.g., 0)
df['A'].fillna(0, inplace=True)

print(df)

##########################################################################

#Data Import/Export

# Read data from a CSV file
csv_file = '/home/ali.zaidi/PycharmProjects/python_training/important_libraries/data.csv'
df = pd.read_csv(csv_file)

# Write data to an Excel file
excel_file = '/home/ali.zaidi/PycharmProjects/python_training/important_libraries/data.xlsx'
df.to_excel(excel_file, index=False)

# Display the imported data
print(df)




