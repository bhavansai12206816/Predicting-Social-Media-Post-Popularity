import joblib, pandas as pd
from pathlib import Path

def save_joblib(obj, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(obj, path)

def load_joblib(path: str):
    return joblib.load(path)

def write_parquet(df: pd.DataFrame, path: str):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)

def read_parquet(path: str):
    return pd.read_parquet(path)
