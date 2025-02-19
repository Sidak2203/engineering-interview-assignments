import os
import pandas as pd
from pathlib import Path

# Dynamically find the project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Moves up to the 'datapipeline' folder
DATA_DIR = PROJECT_ROOT / "source-data"  # Path to locate source-data


def load_csv(file_name):
    """
    Loads a CSV file from the source-data directory.

    Args:
        file_name (str): The name of the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist in the directory.
    """
    file_path = DATA_DIR / file_name  # Construct the full path to the file
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return pd.read_csv(file_path)


def load_data():
    """
    Loads both races and results data from CSV files.

    Returns:
        tuple: (races DataFrame, results DataFrame)
    """
    races = load_csv("races.csv")  # Load race data
    results = load_csv("results.csv")  # Load results data
    return races, results
