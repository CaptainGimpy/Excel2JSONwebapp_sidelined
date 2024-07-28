import pandas as pd

# Load the Excel file
file_path = 'Structured_Pandora_Catalog.xlsx'
df = pd.read_excel(file_path)

# Inspect the DataFrame structure
print("Structured DataFrame:")
print(df.head(50))  # Print the first 50 rows to understand the structure

# Further analysis and adjustments can be made here based on the observed structure
