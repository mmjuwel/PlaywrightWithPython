import json
from pathlib import Path

def load_test_data(filename: str):
    project_root = Path(__file__).parent.parent
    test_data_file = project_root / "test_data" / filename
    
    with open(test_data_file, "r") as f:
        return json.load(f)

def get_login_test_data():
    return load_test_data("login_data.json")

def get_trip_test_data():
    return load_test_data("trip_data.json")
