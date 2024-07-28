import json
import pandas as pd

# Load the JSON data
with open('data.json', 'r') as f:
    raw_data = json.load(f)

# Convert JSON to DataFrame
df = pd.DataFrame(raw_data)

# Inspect the DataFrame structure
print("Complete DataFrame:")
print(df.head(50))  # Print the first 50 rows to understand the structure

# Save the DataFrame to a CSV file for easier inspection
df.to_csv('raw_data_inspection.csv', index=False)

print("Data saved to 'raw_data_inspection.csv' for inspection.")
