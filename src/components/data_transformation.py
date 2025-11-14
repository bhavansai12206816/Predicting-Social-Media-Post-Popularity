import pandas as pd
from datetime import datetime

def coerce_and_engineer(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform safe feature engineering, preserving platform/media_type columns.
    Ensures numeric conversions, engagement metrics, and temporal features.
    """
    df = df.copy()

    # --- Preserve and normalize platform/media_type ---
    if 'platform' not in df.columns:
        df['platform'] = 'unknown'
    if 'media_type' not in df.columns:
        df['media_type'] = 'unknown'

    df['platform'] = df['platform'].astype(str).str.strip().str.lower()
    df['media_type'] = df['media_type'].astype(str).str.strip().str.lower()

    # --- Coerce numeric columns ---
    for col in ['likes', 'comments', 'shares', 'followers', 'views', 'saves', 'caption_length']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        else:
            df[col] = 0

    # --- Compute engagement & engagement rate ---
    if 'engagement' not in df.columns:
        df['engagement'] = df['likes'] + df['comments'] + df['shares']

    if 'engagement_rate' not in df.columns:
        df['engagement_rate'] = df['engagement'] / df['followers'].replace(0, 1)
        df['engagement_rate'] = df['engagement_rate'].fillna(0)

    # --- Temporal features ---
    if 'posted_at' in df.columns:
        try:
            df['posted_at'] = pd.to_datetime(df['posted_at'], errors='coerce')
            df['hour'] = df['posted_at'].dt.hour.fillna(19).astype(int)
        except Exception:
            df['hour'] = 19
    else:
        df['hour'] = 19

    # --- Day of week and weekend flag ---
    if 'weekday' not in df.columns:
        df['weekday'] = df['posted_at'].dt.weekday.fillna(2).astype(int) if 'posted_at' in df.columns else 2
    df['is_weekend'] = df['weekday'].isin([5, 6]).astype(int)

    return df


def get_feature_sets(df=None):
    """
    Returns categorical and numeric feature column lists for modeling.
    """
    cat_cols = ['platform', 'media_type']
    num_cols = [
        'likes', 'comments', 'shares', 'followers',
        'views', 'saves', 'caption_length', 'hour', 'is_weekend'
    ]
    return cat_cols, num_cols
