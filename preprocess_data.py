import json
import pandas as pd

# Load the JSON data
with open('data.json', 'r') as f:
    raw_data = json.load(f)

# Convert JSON to DataFrame
df = pd.DataFrame(raw_data)

# Inspect the DataFrame structure
print(df.head())

# Extract the relevant data and structure it properly
data = []
for index, row in df.iterrows():
    if pd.notnull(row['Pandora Releases']):
        season = row['Unnamed: 1']
        for year in range(2000, 2031):
            year_col = f'Unnamed: {year - 1998}'
            if pd.notnull(row[year_col]):
                data.append({
                    'Season': season,
                    'Year': year,
                    'Releases': row[year_col]
                })

# Convert to DataFrame for better structure
structured_df = pd.DataFrame(data)
print(structured_df.head())

# Save the structured data to a new JSON file
structured_df.to_json('structured_data.json', orient='records', lines=True)

# Optionally save to a new Excel file
structured_df.to_excel('Structured_Pandora_Catalog.xlsx', index=False)

print("Data restructuring complete. Files saved as 'structured_data.json' and 'Structured_Pandora_Catalog.xlsx'.")
