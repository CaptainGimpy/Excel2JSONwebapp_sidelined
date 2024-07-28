import pandas as pd

# Load the Excel file
file_path = 'raw_data_inspection.xlsx'
df = pd.read_excel(file_path)

# Inspect the DataFrame structure
print("Raw DataFrame:")
print(df.head(50))  # Print the first 50 rows to understand the structure
