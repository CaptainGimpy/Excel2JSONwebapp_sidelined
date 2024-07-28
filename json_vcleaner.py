import json

# Load and validate the JSON file
input_file_path = 'structured_data.json'
output_file_path = 'cleaned_structured_data.json'

try:
    with open(input_file_path, 'r') as file:
        data = json.load(file)
        print("JSON is valid")

    # Reformat the JSON and save to a new file
    with open(output_file_path, 'w') as file:
        json.dump(data, file, indent=4)
        print(f"JSON has been cleaned and saved to {output_file_path}")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
