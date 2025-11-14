import pandas as pd
from pathlib import Path
from src.logger import get_logger

log = get_logger(__name__)

def load_csv(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(path)
    df = pd.read_csv(p)
    log.info(f"Loaded {path} shape={df.shape}")
    return df
