
import pytest
import pandas as pd
import json
from pathlib import Path
from data_loader import load_data, load_csv
from data_transformer import transform_data
from data_writer import save_json


def test_load_data(mocker):
    """Test loading races and results."""
    mock_races = pd.DataFrame(
        {"raceId": [1], "year": [2024], "name": ["British Grand Prix"], "round": [12], "date": ["2024-07-07"], "time": ["14:00:00"]}
    )
    mock_results = pd.DataFrame({"raceId": [1], "driverId": [44], "position": [1], "fastestLapTime": ["01:29.4"]})

    mocker.patch("data_loader.load_csv", side_effect=[mock_races, mock_results])
    races, results = load_data()

    assert not races.empty
    assert not results.empty
    assert "name" in races.columns
    assert "driverId" in results.columns

def test_transform_data():
    """Test transformation logic"""
    races = pd.DataFrame({
        "raceId": [1], "year": [2024], "name": ["British Grand Prix"], "round": [12], "date": ["2024-07-07"], "time": ["14:00:00"]
    })
    results = pd.DataFrame({
        "raceId": [1, 1, 1], "driverId": [44, 77, 33], "position": [1, 2, 3], "fastestLapTime": ["01:29.4", "01:29.0", "01:28.3"]
    })
    transformed = transform_data(races, results)
    assert len(transformed) == 1
    year, races_data = transformed[0]
    assert year == 2024
    assert races_data[0]["Race Winning driverId"] == 44
    assert races_data[0]["Race Fastest Lap"] == "01:28.3"

def test_save_json(tmp_path):
    """Test saving JSON output with correct path."""
    test_output_dir = tmp_path / "results"
    data = [{"Race Name": "British Grand Prix", "Race Round": 12, "Race Datetime": "2024-07-07T14:00:00", "Race Winning driverId": 44, "Race Fastest Lap": "01:28.3"}]
    save_json(2024, data, output_folder=test_output_dir)
    file_path = test_output_dir / "stats_2024.json"
    assert file_path.exists()
    with open(file_path, "r") as f:
        json_data = json.load(f)
    assert isinstance(json_data, list)
    assert json_data[0]["Race Name"] == "British Grand Prix"

if __name__ == "__main__":
    pytest.main()
