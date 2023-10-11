"""
Script permettant de merge plusieurs json en un seul, afin de créer un config.json pour Webservices
Enercoop
"""

# import
import json
import os
import argparse
from datetime import datetime
import locale


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


def merge_json_files(output_file: json,
                     *input_files: json) -> json:
    """
    Merge multiple JSON files as children into a single parent JSON.

    Args:
        output_file (json): The parent JSON file where the merged content will be stored.
        *input_files (json): Multiple JSON files to be merged as children.

    Returns:
        json: The merged JSON content.

    Example:
    python3 merge_json.py config.json *.json
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

        with open(file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
                merged_data["children"].append(data)
            except json.JSONDecodeError as e:
                print(f"ERROR: invalid json file {file_path}: {e}")

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(merged_data, outfile, indent=2, ensure_ascii=False)

    print(f"End of merge. Result path file: {output_file}")


if __name__ == "__main__":

    cwd = str(os.getcwd())

    parser = argparse.ArgumentParser(description="Merge multiples .json files into one")
    parser.add_argument("outfile", help="Output merged .json file")
    parser.add_argument("input_files", nargs="+", help="Input .json files to merge")
    parser.add_argument("--input-dir", default=cwd, help="input dir by default: %(default)s)")
    args = parser.parse_args()

    INPUT_DIRECTORY = os.path.abspath(args.input_dir)
    merge_json_files(args.outfile, *args.input_files)
