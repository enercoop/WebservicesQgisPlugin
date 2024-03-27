import yaml
import json
import os

# Function to convert YAML to JSON
def yaml_to_json(yaml_file, json_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(yaml_data, f, ensure_ascii=False, indent=2)

# Directory containing YAML files
yaml_dir = 'yaml/'

# Directory to store JSON files
json_dir = 'yaml/'

# Iterate over each YAML file in the directory
for yaml_file in os.listdir(yaml_dir):
    if yaml_file.endswith('.yaml') or yaml_file.endswith('.yml'):
        # Construct paths for YAML and JSON files
        yaml_path = os.path.join(yaml_dir, yaml_file)
        json_file = os.path.splitext(yaml_file)[0] + '.json'
        json_path = os.path.join(json_dir, json_file)
        
        # Convert YAML to JSON
        yaml_to_json(yaml_path, json_path)

print("Conversion complete.")
