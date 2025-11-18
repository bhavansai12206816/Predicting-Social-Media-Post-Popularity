🌈📈 Predicting Social Media Post Popularity
<div align="center">

🔥 An ML-powered interactive dashboard to predict engagement, analyze platform insights & evaluate model performance — deployed on Render! 🔥
<br>

<a href="https://predicting-social-media-post-popularity.onrender.com"> <img src="https://img.shields.io/badge/🚀 Live App-Click%20Here-brightgreen?style=for-the-badge&logo=streamlit" /> </a> <a href="https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity/archive/refs/heads/main.zip"> <img src="https://img.shields.io/badge/⬇️ Download ZIP-Project-blue?style=for-the-badge&logo=github" /> </a> </div>
🌟 Overview

This project predicts social media post popularity using Engagement Rate (ER) and provides:

✨ Manual engagement prediction
✨ Platform-wise analytics
✨ Interactive visualizations
✨ Random Forest–based ML model
✨ Fully deployed Streamlit web app
✨ Modular pipeline + logging

📌 Engagement Rate Formula
Engagement
 
Rate
=
Likes + Comments + Shares
Followers
Engagement Rate=
Followers
Likes + Comments + Shares
	​

🚀✨ Key Features
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

Filter by:
Instagram / Twitter / LinkedIn / TikTok / All

Includes:
📌 Engagement rate distribution (plots)
📌 Summary statistics
📌 10,000+ posts analyzed

📉 3. Model Evaluation
Metric	Value
📊 R² Score	0.987
📉 RMSE	0.00358
⚖️ MAE	0.00232

✨ Extremely strong performance — almost perfect fit.

🤖 Machine Learning Model
🌲 Random Forest Regressor

Chosen because it:

✔ Captures non-linear relationships
✔ Works well on large datasets
✔ Stable + robust
✔ Avoids overfitting
✔ Does not require feature scaling

📌 Achieved R² score of 0.987.

🎨📊 What the App Shows
🔮 Manual Popularity Prediction (Example Input)
Platform: Instagram
Media Type: Image
Likes: 100
Comments: 10
Shares: 1
Followers: 1000
Caption Length: 100


⭐ Predicted ER: 0.1110
🔥 Popularity: HIGH

📊 Platform Insights

Selected Platform: All

Posts analyzed: 10000

Histogram of engagement rate

Summary statistics

⚖️ Model Evaluation (Live App)

📊 R² Score → 0.987
📉 RMSE → 0.00358
⚖️ MAE → 0.00232

🛠️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity.git
cd Predicting-Social-Media-Post-Popularity

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit app
streamlit run app.py

☁️ Deployment (Render)

Using this config:

services:
  - type: web
    name: social-media-post-popularity
    env: python
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"

Live App

👉 https://predicting-social-media-post-popularity.onrender.com

🧰 Technologies Used

🐍 Python
🎨 Streamlit
📊 Pandas, NumPy
📈 Scikit-learn
🌲 Random Forest Regressor
📦 Joblib
⚡ Plotly
🪶 PyArrow (Parquet)
📝 Custom Logging

🤝 Contributing

Pull requests and issues are welcome!
Feel free to improve models, UI, dataset, or deployment.

📜 License

📝 MIT License — free to use, modify, and share.