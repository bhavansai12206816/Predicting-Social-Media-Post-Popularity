import argparse, pandas as pd
from src.Utils import load_joblib, write_parquet
from src.components.data_transformation import coerce_and_engineer, get_feature_sets
from src.logger import get_logger

log = get_logger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='Notebook/sample_posts.csv')
    parser.add_argument('--model', default='artifacts/model.joblib')
    parser.add_argument('--output', default='artifacts/predictions.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df_fe = coerce_and_engineer(df)
    model = load_joblib(args.model)
    cat_cols, num_cols = get_feature_sets(df_fe)
    X = pd.get_dummies(df_fe[cat_cols + num_cols], columns=cat_cols, drop_first=True)
    preds = model.predict(X)
    df_fe['engagement_rate_pred'] = preds
    df_fe.to_csv(args.output, index=False)
    log.info(f'Wrote predictions to {args.output}')

if __name__ == '__main__':
    main()
