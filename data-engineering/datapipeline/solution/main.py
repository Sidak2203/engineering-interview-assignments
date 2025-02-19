
from data_loader import load_data
from data_transformer import transform_data
from data_writer import save_json

def main():
    """
    Main function to run the data pipeline.
    """
    races, results = load_data()  # Step 1: Load Data
    transformed_data = transform_data(races, results)  # Step 2: Transform Data

    for year, json_data in transformed_data:  # Step 3: Save Output
        save_json(year, json_data)

if __name__ == "__main__":
    main()