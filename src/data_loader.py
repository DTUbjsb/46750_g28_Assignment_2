""""
Data Loader
CSV formats:
1. prices.csv: columns = [month, coal, gas, oil]
2. storage.csv: columns = [fuel, capacity]
3. plant_capacity.csv: columns = [fuel, capacity]
4. demand.csv: columns = [month, demand]
"""

import pandas as pd

def load_prices(file_path: str) -> pd.DataFrame:
    """Load monthly fuel prices from CSV."""
    df = pd.read_csv(file_path)
    required_cols = {"month", "coal", "gas", "oil"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"prices.csv must contain columns: {required_cols}")
    return df

def load_storage(file_path: str) -> dict:
    """Load storage capacities from CSV and return as dictionary."""
    df = pd.read_csv(file_path)
    required_cols = {"fuel", "capacity"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"storage.csv must contain columns: {required_cols}")
    return dict(zip(df["fuel"], df["capacity"]))

def load_conversion(file_path: str) -> dict:
    """Load conversion rates from CSV and return as dictionary."""
    df = pd.read_csv(file_path)
    required_cols = {"fuel", "conversion_rate"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"conversion.csv must contain columns: {required_cols}")
    return dict(zip(df["fuel"], df["conversion_rate"]))

def load_plant_capacity(file_path: str) -> dict:
    """Load plant capacities from CSV and return as dictionary."""
    df = pd.read_csv(file_path)
    required_cols = {"fuel", "capacity"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"plant_capacity.csv must contain columns: {required_cols}")
    return dict(zip(df["fuel"], df["capacity"]))

def load_demand(file_path: str) -> pd.DataFrame:
    """Load monthly electricity demand from CSV."""
    df = pd.read_csv(file_path)
    required_cols = {"month", "demand"}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"demand.csv must contain columns: {required_cols}")
    return df

# Example usage
if __name__ == "__main__":
    # Replace with actual file paths
    prices = load_prices("data/prices.csv")
    storage = load_storage("data/storage.csv")
    plant_capacity = load_plant_capacity("data/plant_capacity.csv")
    demand = load_demand("data/demand.csv")

    print("Prices:\n", prices.head())
    print("Storage:\n", storage)
    print("Plant Capacity:\n", plant_capacity)
    print("Demand:\n", demand.head())

