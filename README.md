# PREDICTING_SOCIAL_MEDIA_POST_POPULARITY

This project scaffold includes:
- Notebook/sample_posts.csv (your dataset)
- src/ modules for ingestion, transformation, training
- app.py (Streamlit) — manual input only (likes/comments/shares/followers + media_type)
- pipeline scripts to train and predict
- logs/app.log produced by logger.py (TimedRotatingFileHandler, dd/mm/YYYY HH:MM:SS)

Quickstart (Windows PowerShell)
1. python -m venv venv
2. .\venv\Scripts\activate
3. pip install -r requirements.txt
4. python -m src.pipeline.train_pipeline
5. streamlit run app.py

