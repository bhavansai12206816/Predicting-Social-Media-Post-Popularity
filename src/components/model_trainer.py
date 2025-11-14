# src/components/model_trainer.py
from __future__ import annotations
import logging
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from typing import Dict, Any, List

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error

log = logging.getLogger(__name__)


def _numeric_feature_candidates(df: pd.DataFrame) -> List[str]:
    """
    Pick a safe list of numeric features present in dataset.
    """
    candidates = [
        "followers", "views", "likes", "comments", "shares",
        "saves", "weekday", "caption_length"
    ]
    return [c for c in candidates if c in df.columns]


def train_and_save(df: pd.DataFrame, model_out: str | Path, processed_out: str | Path) -> Dict[str, Any]:
    """
    Train a RandomForestRegressor on numeric features and save model + processed data.
    Ensures 'platform' and 'media_type' columns are preserved for visualization.
    Returns training statistics with RMSE for model evaluation.
    """
    model_out = Path(model_out)
    processed_out = Path(processed_out)

    df = df.copy()

    # --- Ensure engagement_rate exists ---
    if "engagement_rate" not in df.columns:
        raise ValueError("Dataset must contain 'engagement_rate' column")

    # --- Identify usable numeric features ---
    features = _numeric_feature_candidates(df)
    if not features:
        raise ValueError(f"No numeric features found for training. Found columns: {', '.join(df.columns)}")

    # --- Keep platform/media_type for downstream visualization ---
    extra_cols = [c for c in ["platform", "media_type"] if c in df.columns]

    # --- Clean data ---
    required_cols = features + ["engagement_rate"]
    df_clean = df[required_cols + extra_cols].dropna(subset=required_cols)
    if df_clean.empty:
        raise ValueError("No data available after dropping NaNs from target/features")

    # --- Prepare features/target ---
    X = df_clean[features]
    y = df_clean["engagement_rate"]

    # --- Split data ---
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, shuffle=True
    )

    # --- Initialize model ---
    model = RandomForestRegressor(
        n_estimators=200, max_depth=10, random_state=42, n_jobs=-1
    )

    # --- Cross-validation RMSE ---
    try:
        neg_mse_scores = cross_val_score(
            model, X_train, y_train, cv=5, scoring="neg_mean_squared_error", n_jobs=-1
        )
        rmse_cv = float(np.sqrt(-neg_mse_scores.mean()))
    except Exception as e:
        log.warning(f"Cross-validation failed: {e}")
        rmse_cv = float("nan")

    # --- Train model ---
    model.fit(X_train, y_train)

    # --- Evaluate model ---
    y_pred = model.predict(X_test)
    mse_test = mean_squared_error(y_test, y_pred)
    rmse_test = float(np.sqrt(mse_test))

    # --- Save model ---
    model_out.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, str(model_out))

    # --- Save processed dataset ---
    processed_out.parent.mkdir(parents=True, exist_ok=True)
    try:
        if str(processed_out).lower().endswith(".parquet"):
            df_clean.to_parquet(processed_out, index=False)
        else:
            df_clean.to_csv(processed_out, index=False)
    except Exception as e:
        log.warning(f"Failed to write processed file {processed_out}: {e}")

    # --- Logging ---
    log.info(f"✅ Model trained successfully — RMSE={rmse_test:.6f}, Features used: {features}")
    log.info(f"📁 Model saved at: {model_out}")
    log.info(f"📊 Processed dataset saved at: {processed_out}")

    # --- Return statistics ---
    stats = {
        "rmse_cv": rmse_cv,
        "rmse_test": rmse_test,
        "model": str(model_out),
        "processed": str(processed_out),
        "features_used": features,
        "extra_cols": extra_cols,
        "n_train": len(X_train),
        "n_test": len(X_test),
    }

    return stats
