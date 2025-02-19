import json
import os
from pathlib import Path


def save_json(year, json_data, output_folder=None):
    """
    Saves transformed data to JSON files. Supports test paths.

    Args:
        year (int): The year for which the data is saved.
        json_data (list): The transformed data to be stored.
        output_folder (Path, optional): The directory to save the JSON file.
            Defaults to the real "results" directory.
    """
    # Default to the real results directory if no test path is given
    output_folder = output_folder or (Path(__file__).resolve().parent.parent.parent / "results")
    output_folder.mkdir(parents=True, exist_ok=True)  # Ensure directory exists

    file_path = output_folder / f"stats_{year}.json"  # Define JSON file name
    with open(file_path, "w") as f:
        json.dump(json_data, f, indent=4)  # Save JSON with indentation

    print(f"✅ Saved: {file_path}")
