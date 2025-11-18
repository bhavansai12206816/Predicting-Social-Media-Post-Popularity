🌈✨ <div align="center"><span style="font-size:60px;">📈 Predicting Social Media Post Popularity</span></div>
<div align="center">🔥 An interactive ML-powered dashboard to predict engagement rate, analyze platform insights & evaluate model performance — deployed live on Render! 🔥</div>
<p align="center"> <a href="https://predicting-social-media-post-popularity.onrender.com"> <img src="https://img.shields.io/badge/Get%20Started-LIVE%20APP-brightgreen?style=for-the-badge&logo=streamlit" /> </a> <a href="https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity/archive/refs/heads/main.zip"> <img src="https://img.shields.io/badge/Download%20ZIP-blue?style=for-the-badge&logo=github" /> </a> </p>
🌟 Overview

This project predicts how well a social media post will perform using Engagement Rate (ER) and provides:

✨ Manual popularity prediction
✨ Platform-wise insights
✨ Interactive visualizations
✨ ML model evaluation
✨ Fully deployed Streamlit web app
✨ Logging & modular ML pipeline

📌 Engagement Rate Formula
                     Likes + Comments + Shares​
Engagement Rate =   ___________________________
                             Followers
	​

🚀 Key Features
🎯 1. Manual Popularity Prediction

Input fields:

Platform

Media Type

Likes

Comments

Shares

Followers

Caption Length

Outputs:

⭐ Predicted Engagement Rate: 0.1110 (11.10%)

🔥 Popularity Level: HIGH

📊 2. Dataset Insights by Platform

Filter by: Instagram / Twitter / LinkedIn / TikTok / All

Engagement rate distribution

Statistics for each platform

10,000+ posts analyzed

📉 3. Model Evaluation

Metrics from live app:

Metric	Value
📊 R² Score	0.987
📉 RMSE	0.00358
⚖️ MAE	0.00232

Extremely strong performance (almost perfect fit).

🤖 Machine Learning Model
🌲 Random Forest Regressor

Used because it:

Captures non-linear relationships

Handles numeric features without scaling

Avoids overfitting using many trees

Provides high accuracy and stability

Works well on large datasets

🔬 This model produced very high R² score (0.987) on evaluation.

📊 What You See in the App
🎨 💡 Social Media Post Popularity — Manual Input & Platform Insights
🔮 Manual Popularity Prediction
Platform: instagram  
Media Type: image  
Likes: 100  
Comments: 10  
Shares: 1  
Followers: 1000  
Caption Length: 100  

⭐ Predicted Engagement Rate (formula): 0.1110 (11.10%)
🔥 Popularity Level: HIGH
📊 Dataset Insights by Platform
Selected Platform: All  
Posts: 10000  

Engagement Rate Distribution (Histogram shown in app)
⚖️ Model Evaluation — Actual vs Predicted Engagement Rate
📊 R² Score → 0.987
📉 RMSE → 0.00358
⚖️ MAE → 0.00232
📥 How to Run the Project Locally
1️⃣ Clone the project
git clone https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity.git
cd Predicting-Social-Media-Post-Popularity

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

☁️ Deployment (Render)

App is deployed using this config:

services:
  - type: web
    name: social-media-post-popularity
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"


Live App:
👉 https://predicting-social-media-post-popularity.onrender.com

🛠 Technologies Used

Python

Streamlit

Pandas, NumPy

Scikit-learn

Plotly

Random Forest Regressor

Joblib

PyArrow / Parquet

Logging (custom logger)

🙌 Contributing

Feel free to submit issues or pull requests!

📜 License

MIT License — open for anyone to use, modify, improve.