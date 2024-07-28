import pandas as pd

# Load the original Excel file
file_path = 'raw_data_inspection.xlsx'
df = pd.read_excel(file_path)

# Inspect the DataFrame structure
print("Raw DataFrame:")
print(df.head(50))  # Print the first 50 rows to understand the structure

# Initialize an empty list to store the structured data
data = []

# Identify the header row (where 'Seasons' appears)
header_row_index = df[df.iloc[:, 1] == 'Seasons'].index[0]
print(f"Header row index: {header_row_index}")

# Loop through each row in the DataFrame starting after the header row
for index, row in df.iloc[header_row_index + 1:].iterrows():
    season = row['Unnamed: 1']
    if pd.notnull(season) and season not in ['Seasons']:
        print(f"Season detected: {season}")  # Debug: Print the current season
        for year in range(2000, 2031):
            year_col = f'Unnamed: {year - 1998}'
            if year_col in row and pd.notnull(row[year_col]):
                print(f"Year: {year}, Releases: {row[year_col]}")  # Debug: Print the current year and releases
                data.append({
                    'Season': season,
                    'Year': year,
                    'Releases': row[year_col]
                })

# Convert to DataFrame for better structure
structured_df = pd.DataFrame(data)

# Inspect the structured DataFrame
print("Structured DataFrame:")
print(structured_df.head())

# Save the structured data to a new JSON file
structured_df.to_json('structured_data.json', orient='records', lines=True)

# Optionally save to a new Excel file
structured_df.to_excel('Structured_Pandora_Catalog.xlsx', index=False)

print("Data restructuring complete. Files saved as 'structured_data.json' and 'Structured_Pandora_Catalog.xlsx'.")
