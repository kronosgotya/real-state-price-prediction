import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    here = os.path.dirname(os.path.abspath(__file__))
    artifacts = os.path.join(here, "artifacts")
    columns_path = os.path.join(artifacts, "columns.json")
    model_path = os.path.join(artifacts, "bangalore_home_prices_model_pickle")
    with open(columns_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        __data_columns = data["data_columns"] if isinstance(data, dict) else data

        __locations = __data_columns[3:] if len(__data_columns) > 3 else []

    with open("./artifacts/bangalore_home_prices_model_pickle", "rb") as f:
        __model = pickle.load(f)

    print(f"Loaded {len(__data_columns)} data_columns, {len(__locations)} locations.")
    print("Loading saved artifacts...done")

def get_location_names():
    global __locations
    if __locations is None:
        load_saved_artifacts()
    return list(__locations)

def get_estimated_price(location, sqft, broom, bath):
    global __data_columns, __model

    if __data_columns is None or __model is None:
        load_saved_artifacts()

    loc_norm = str(location).strip().lower()

    try:
        loc_index = __data_columns.index(loc_norm)
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = float(sqft)
    x[1] = float(bath)
    x[2] = float(broom)

    if loc_index >= 0:
        x[loc_index] = 1.0

    pred = __model.predict([x])[0]
    return round(float(pred), 2)

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar", 800, 1, 2))
    print(get_estimated_price("1st Phase JP Nagar", 1000, 2, 2))
    print(get_estimated_price("Kalhalli", 1000, 2, 2))
    print(get_estimated_price("Ejipura", 1000, 2, 2))