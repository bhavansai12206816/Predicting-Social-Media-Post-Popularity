# src/pipeline/train_pipeline.py
from __future__ import annotations
import argparse
from pathlib import Path
from src.components.data_ingestion import load_csv
from src.components.model_trainer import train_and_save
from src.logger import get_logger

log = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Train model for Social Media Post Popularity Prediction")
    parser.add_argument("--input", default="Notebook/sample_posts.csv", help="Path to input CSV dataset")
    parser.add_argument("--model", default="artifacts/model.joblib", help="Path to save trained model")
    parser.add_argument("--processed", default="artifacts/processed.parquet", help="Path to save processed data")
    args = parser.parse_args()

    log.info("🚀 Train pipeline started")

    # Step 1: Validate input path
    input_path = Path(args.input)
    if not input_path.exists():
        log.error(f"❌ Input file not found: {input_path.resolve()}")
        raise FileNotFoundError(f"Input CSV not found: {input_path.resolve()}")

    # Step 2: Load data
    try:
        df = load_csv(str(input_path))
        log.info(f"✅ Data loaded: shape={df.shape}")
    except Exception as e:
        log.exception(f"❌ Failed to load data: {e}")
        raise

    # Step 3: Train and Save
    try:
        stats = train_and_save(df, args.model, args.processed)
        log.info("✅ Training completed successfully")
        log.info(f"📊 Training summary:\n{stats}")
    except Exception as e:
        log.exception(f"❌ Training pipeline failed: {e}")
        raise


if __name__ == "__main__":
    main()
