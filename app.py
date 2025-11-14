# app.py — Manual Prediction + Dataset Insights + Platform Filtering + Full Logging
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from src.Utils import load_joblib, read_parquet
from src.components.data_transformation import coerce_and_engineer, get_feature_sets
from src.logger import get_logger
import numpy as np
import math

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(page_title="Social Media Post Popularity — Insights Dashboard", layout="wide")
st.title("📈 Social Media Post Popularity — Manual Input & Platform Insights")

log = get_logger(__name__)
log.info("🚀 Streamlit app started")

processed_path = Path("artifacts/processed.parquet")
model_path = Path("artifacts/model.joblib")

# ---------------------------------------------------------
# LOAD PROCESSED DATA
# ---------------------------------------------------------
df = None
if processed_path.exists():
    try:
        df = read_parquet(str(processed_path))
        # normalize platform column for filtering
        if "platform" in df.columns:
            df["platform"] = df["platform"].astype(str).str.strip().str.lower()
        log.info(f"✅ Loaded dataset from {processed_path} with shape {df.shape}")
    except Exception as e:
        log.exception(f"❌ Failed to read parquet file: {e}")
        st.error("Failed to load processed dataset — check logs.")
else:
    log.warning("⚠️ Processed dataset not found at artifacts/processed.parquet")
    st.warning("⚠️ Processed dataset not found. Run training pipeline first to generate artifacts/processed.parquet.")

# ---------------------------------------------------------
# MANUAL INPUT FORM (uses exact formula ER = (likes+comments+shares)/followers)
# ---------------------------------------------------------
st.header("🔮 Manual Popularity Prediction")

with st.form("manual_form"):
    c1, c2, c3 = st.columns(3)
    with c1:
        platform = st.selectbox("Platform", ["instagram", "twitter", "linkedin", "tiktok"])
        media_type = st.selectbox("Media Type", ["image", "video", "carousel", "text", "reel"])
    with c2:
        likes = st.number_input("Likes", min_value=0, value=100)
        comments = st.number_input("Comments", min_value=0, value=10)
        shares = st.number_input("Shares", min_value=0, value=1)
    with c3:
        followers = st.number_input("Followers", min_value=1, value=1000)
        caption_length = st.number_input("Caption Length (chars)", min_value=0, value=100)

    submitted = st.form_submit_button("Predict Now")

if submitted:
    log.info(
        f"🧾 Manual input: platform={platform}, media_type={media_type}, likes={likes}, "
        f"comments={comments}, shares={shares}, followers={followers}, caption_len={caption_length}"
    )

    try:
        # compute exact engagement and engagement rate
        engagement = int(likes) + int(comments) + int(shares)
        # avoid division by zero
        followers_safe = max(int(followers), 1)
        er = engagement / followers_safe  # fraction, e.g. 0.05
        er_pct = er * 100.0  # show as percentage

        # define label thresholds (2% and 5%) but shown as percentages
        T_LOW = 0.02
        T_HIGH = 0.05
        label = "LOW" if er < T_LOW else ("MEDIUM" if er < T_HIGH else "HIGH")

        # show results
        st.success(f"⭐ Predicted Engagement Rate (formula): **{er:.4f} ({er_pct:.2f}%)**")
        st.info(f"🔥 Popularity Level: **{label}**")

        # Engagement Rate Meter (percentage bar)
        color = "#ef4444" if label == "LOW" else ("#facc15" if label == "MEDIUM" else "#22c55e")
        fig = px.bar(x=["Engagement Rate"], y=[er_pct],
                     color_discrete_sequence=[color],
                     text=[f"{er_pct:.2f}%"])
        fig.update_traces(textposition="inside")
        fig.update_layout(yaxis_range=[0, max(20, math.ceil(er_pct/5)*5)], showlegend=False,
                          height=180, plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)

        log.info(f"✅ Manual formula prediction computed: engagement={engagement}, ER={er:.4f} ({er_pct:.2f}%), label={label}")

    except Exception as e:
        st.error(f"Prediction failed: {e}")
        log.exception("❌ Manual prediction error")

# ---------------------------------------------------------
# DATASET VISUAL SECTION — Dynamic Platform Filter
# ---------------------------------------------------------
st.markdown("---")
st.subheader("📊 Dataset Insights by Platform")

if df is not None and len(df):
    if "platform" in df.columns:
        platforms = sorted(df["platform"].dropna().unique())
        selected_platform = st.selectbox("🔍 Select Platform for Analysis", options=["All"] + platforms, index=0)
        log.info(f"📊 User selected platform filter: {selected_platform}")
    else:
        st.warning("⚠️ No 'platform' column found — showing all data.")
        selected_platform = "All"

    # Filter df for platform
    if selected_platform != "All" and "platform" in df.columns:
        df_filtered = df[df["platform"] == selected_platform].copy()
        st.info(f"📊 Showing data for **{selected_platform.capitalize()}** — {len(df_filtered)} posts")
    else:
        df_filtered = df.copy()
        st.info(f"📊 Showing data for **All Platforms** — {len(df_filtered)} posts")

    # Engagement Rate Distribution (shown as fraction axis but labels are percentage)
    if "engagement_rate" in df_filtered.columns:
        st.subheader("Engagement Rate Distribution")
        h = px.histogram(df_filtered, x="engagement_rate", nbins=50,
                         title=f"Engagement Rate Distribution ({selected_platform.capitalize()})",
                         color_discrete_sequence=["#60a5fa"])
        h.update_layout(xaxis_title="Engagement Rate (fraction)", yaxis_title="Count",
                        plot_bgcolor="rgba(0,0,0,0)")
        # change x tick labels to show percent in hover and axis doesn't change numeric data
        st.plotly_chart(h, use_container_width=True)
        log.info(f"📈 Rendered engagement histogram for {selected_platform}")
    else:
        st.warning("⚠️ 'engagement_rate' column missing in dataset.")

# ---------------------------------------------------------
# MODEL EVALUATION — Platform Filtered (uses RandomForest model if available)
# ---------------------------------------------------------
st.markdown("### ⚖️ Model Evaluation — Actual vs Predicted Engagement Rate")

if model_path.exists() and df_filtered is not None and "engagement_rate" in df_filtered.columns:
    try:
        model = load_joblib(str(model_path))
        df_eval = coerce_and_engineer(df_filtered.copy())

        # create model-ready feature set (only keep overlapping features)
        model_features = list(getattr(model, "feature_names_in_", []))
        available = [c for c in model_features if c in df_eval.columns]
        missing = [c for c in model_features if c not in df_eval.columns]

        if len(available) == 0 and len(model_features) > 0:
            raise ValueError("No overlapping features between dataset and model.")

        # prepare X: use available features, fill missing with zeros, reorder to model_features
        if model_features:
            X = df_eval.reindex(columns=model_features, fill_value=0)
        else:
            # fallback: use numeric columns chosen earlier
            cat_cols, num_cols = get_feature_sets(df_eval)
            X = pd.get_dummies(df_eval[cat_cols + num_cols], columns=cat_cols, drop_first=True)
            for f in getattr(model, "feature_names_in_", []):
                if f not in X.columns:
                    X[f] = 0
            X = X[model.feature_names_in_]

        y_true = df_eval["engagement_rate"]
        y_pred = model.predict(X)

        # scatter with regression line
        fig_scatter = px.scatter(df_eval, x=y_true, y=y_pred, trendline="ols",
                                 title=f"Actual vs Predicted Engagement Rate ({selected_platform.capitalize()})",
                                 labels={"x": "Actual ER", "y": "Predicted ER"},
                                 color_discrete_sequence=["#22c55e"])
        fig_scatter.update_traces(marker=dict(size=5, opacity=0.6))
        st.plotly_chart(fig_scatter, use_container_width=True)

        # metrics
        mse = mean_squared_error(y_true, y_pred)
        rmse = float(np.sqrt(mse))
        mae = float(mean_absolute_error(y_true, y_pred))
        r2 = float(r2_score(y_true, y_pred))

        log.info(f"⚖️ Model evaluation: {selected_platform} | R²={r2:.3f} | RMSE={rmse:.5f} | MAE={mae:.5f}")

        # -------- Metric cards like your screenshot --------
        st.markdown("## ")
        col_r2, col_rmse, col_mae = st.columns(3)

        with col_r2:
            st.markdown("### 📊 R² Score")
            st.markdown(f"<h2 style='margin-top:-10px;font-size:40px;'>{r2:.3f}</h2>", unsafe_allow_html=True)

        with col_rmse:
            st.markdown("### 📉 RMSE")
            st.markdown(f"<h2 style='margin-top:-10px;font-size:40px;'>{rmse:.5f}</h2>", unsafe_allow_html=True)

        with col_mae:
            st.markdown("### ⚖️ MAE")
            st.markdown(f"<h2 style='margin-top:-10px;font-size:40px;'>{mae:.5f}</h2>", unsafe_allow_html=True)

        st.markdown("---")

        # -------- Detailed insights (concise) --------
        st.markdown("### 💬 Detailed Model Fit Insights")
        fit_quality = "Excellent" if r2 > 0.9 else "Good" if r2 > 0.75 else "Moderate" if r2 > 0.5 else "Weak"

        st.markdown(f"**🧾 Model Performance Summary ({selected_platform.capitalize() if selected_platform != 'All' else 'All Platforms'})**")
        st.markdown(f"""
• **Fit Quality:** {fit_quality} ({r2:.3f} R²)  
• **Prediction Error (RMSE):** {rmse:.5f}  
• **Average Absolute Error (MAE):** {mae:.5f}
""")

        st.markdown("**🧠 Interpretation (short):**")
        st.markdown(f"""
- Model explains **{r2*100:.1f}%** of engagement variance for this platform.  
- Typical prediction deviation (MAE) ≈ **{mae*100:.2f}%** engagement rate.  
- RMSE ≈ **{rmse*100:.2f}%** (typical root-mean error).
""")

        # highlight fit message
        if r2 > 0.9:
            st.success(f"✅ Excellent fit for {selected_platform.capitalize()} — highly reliable predictions.")
        elif r2 > 0.75:
            st.info(f"🟢 Good fit — strong predictive performance for {selected_platform.capitalize()}.")
        elif r2 > 0.5:
            st.warning(f"🟠 Moderate fit — captures main patterns but can improve for {selected_platform.capitalize()}.")
        else:
            st.error(f"🔴 Weak fit — retraining recommended for {selected_platform.capitalize()} data.")

        # -------- Platform Engagement Stats (as in your screenshot) --------
        st.markdown("### 💡 Platform Engagement Insights")
        avg_er = df_filtered["engagement_rate"].mean()
        med_er = df_filtered["engagement_rate"].median()
        max_er = df_filtered["engagement_rate"].max()
        min_er = df_filtered["engagement_rate"].min()

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("📈 Avg Engagement", f"{avg_er*100:.2f}%")
        c2.metric("📊 Median Engagement", f"{med_er*100:.2f}%")
        c3.metric("🔥 Max Engagement", f"{max_er*100:.2f}%")
        c4.metric("⚖️ Min Engagement", f"{min_er*100:.2f}%")

        st.markdown(f"""
**🔍 Insights for {selected_platform.capitalize() if selected_platform != 'All' else 'All Platforms'}**
- Average engagement: **{avg_er*100:.2f}%**
- Median engagement: **{med_er*100:.2f}%**
- Highest post ER: **{max_er*100:.2f}%**
- Lowest post ER: **{min_er*100:.2f}%**
""")

    except Exception as e:
        st.error(f"Error evaluating model on dataset: {e}")
        log.exception(f"❌ Evaluation error: {e}")
else:
    st.info("Model or dataset not available for evaluation (ensure artifacts/model.joblib and artifacts/processed.parquet exist).")
