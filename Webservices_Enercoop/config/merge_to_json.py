# import
import json
import os
import argparse
from datetime import datetime
import locale
import yaml


def get_current_date():
    """
    Get the current date as a formatted string.

    Returns:
    str: The current date in the format "day month year".

    Example:
    current_date = get_current_date()
    print("Today's date:", current_date)
    """
    # Permet de mettre la date en français
    locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')

    return datetime.now().strftime("%d %B %Y")


def yaml_to_json(yaml_file):
    """
    Convert YAML file to JSON format.

    Args:
        yaml_file (str): Path to the YAML file.

    Returns:
        dict: The content of the YAML file as a Python dictionary.
    """
    with open(yaml_file, 'r', encoding='utf-8') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as e:
            print(f"ERROR: invalid YAML file {yaml_file}: {e}")
            return {}


def merge_yaml_files(output_file: str, *input_files: str):
    """
    Merge multiple YAML files into a single JSON file.

    Args:
        output_file (str): The output JSON file.
        *input_files (str): Multiple YAML files to merge.

    Returns:
        None
    """
    merged_data = {
        "title": f"Webservices_Enercoop - version du {get_current_date()}",
        "ident": "316522f0-d2ef-4422-b935-e333815b4f7e",
        "description": "",
        "type": "folder",
        "children": []
    }

    for file_name in input_files:
        file_path = os.path.join(INPUT_DIRECTORY, file_name)
        if not os.path.isfile(file_path):
            print(f"WARNING: File '{file_path}' does not exist, skip")
            continue

        if file_name.endswith('.yaml'):
            data = yaml_to_json(file_path)
            merged_data["children"].append(data)
        else:
            print(f"WARNING: Unsupported file format for '{file_path}', only YAML files are supported.")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(merged_data, outfile, indent=2, ensure_ascii=False)

    print(f"End of merge. Result path file: {output_file}")


if __name__ == "__main__":

    cwd = str(os.getcwd())

    parser = argparse.ArgumentParser(description="Merge multiples .yaml files into one")
    parser.add_argument("outfile", help="Output merged .json file")
    parser.add_argument("input_files", nargs="+", help="Input .yaml files to merge")
    parser.add_argument("--input-dir", default=cwd, help="input dir by default: %(default)s)")
    args = parser.parse_args()

    INPUT_DIRECTORY = os.path.abspath(args.input_dir)
    merge_yaml_files(args.outfile, *args.input_files)
