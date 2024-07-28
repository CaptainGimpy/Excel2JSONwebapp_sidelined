import pandas as pd
import json

# Load the Excel file
file_path = 'Pandora Catalog.xlsx'
spreadsheet = pd.read_excel(file_path, sheet_name='Pandora Releases')  # Adjust the sheet name as needed

# Preview the first few rows
print(spreadsheet.head())

# Convert to JSON
json_data = spreadsheet.head().to_json(orient='records')
print(json_data)

# Save JSON data to a file (optional)
with open('data.json', 'w') as f:
    f.write(json_data)
