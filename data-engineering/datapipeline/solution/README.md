Formula 1 Data Pipeline

Overview
This project implements an automated Formula 1 race data pipeline that processes race results and generates structured JSON files. The pipeline reads from CSV files (races.csv, results.csv), transforms the data, and outputs one JSON file per year inside the results/ folder.

Project Structure

solution/  
│── source-data/        # Contains input CSV files (races.csv, results.csv)  
│── results/            # Stores generated JSON output files  
│── main.py             # Main script to run the pipeline  
│── data_loader.py      # Loads CSV files into DataFrames  
│── data_transformer.py # Transforms data to required JSON format  
│── data_writer.py      # Writes output JSON files to the results folder  
│── test_main.py        # Unit tests for the pipeline  
│── cloud_deploy_stretch.txt # Explanation of cloud deployment considerations  
│── README.md           # Project documentation  
How to Run the Pipeline

Prerequisites

Ensure Python 3.x is installed.
Install required dependencies using:
pip install pandas pytest

Running the Pipeline
To execute the pipeline and generate JSON output files:
python main.py
This will process data from source-data/ and save JSON results inside the results/ folder.

Output JSON files follow the format:
results/stats_YYYY.json  # Example: stats_2024.json


Stretch Goals Implemented
1. Unit Testing
A unit testing script (test_main.py) was created to validate pipeline functionality.
The test suite ensures correctness of:

Data loading
Data transformation logic
JSON file writing
To run tests:
pytest test_main.py

**2. Cloud Deployment Considerations**

Cloud deployment considerations have been documented in cloud_deploy_stretch.txt.
This includes details on how AWS Glue and S3 can be used to automate the pipeline in a cloud environment.
