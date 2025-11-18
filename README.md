<h1 align="center"><span style="font-size: 50px;">🌈📈 Predicting Social Media Post Popularity</span></h1>
<div align="center">

🔥 An ML-powered interactive dashboard to predict engagement, analyze platform insights & evaluate model performance — deployed on Render! 🔥
<br>

<a href="https://predicting-social-media-post-popularity.onrender.com"> <img src="https://img.shields.io/badge/🚀 Live App-Click%20Here-brightgreen?style=for-the-badge&logo=streamlit" /> </a> <a href="https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity/archive/refs/heads/main.zip"> <img src="https://img.shields.io/badge/⬇️ Download ZIP-Project-blue?style=for-the-badge&logo=github" /> </a> </div>
🌟 Overview

This project predicts social media post popularity using Engagement Rate (ER) and provides:

✨ Manual engagement prediction<br>
✨ Platform-wise analytics<br>
✨ Interactive visualizations<br>
✨ Random Forest–based ML model<br>
✨ Fully deployed Streamlit web app<br>
✨ Modular pipeline + logging<br>


🚀✨ Key Features<br>

🎯 1. Manual Popularity Prediction

Input fields:

Platform

Media Type

Likes

Comments

Shares

Followers

Caption Length

Outputs:<br>
⭐ Predicted Engagement Rate: 0.1110 (11.10%)<br>
🔥 Popularity Level: HIGH<br>

📊 2. Dataset Insights by Platform

Filter by:
Instagram / Twitter / LinkedIn / TikTok / All

Includes:<br>
📌 Engagement rate distribution (plots)<br>
📌 Summary statistics<br>
📌 10,000+ posts analyzed<br>

📉 3. Model Evaluation<br>
Metric	Value<br>
📊 R² Score	0.987<br>
📉 RMSE	0.00358<br>
⚖️ MAE	0.00232<br>

✨ Extremely strong performance — almost perfect fit.<br>

🤖 Machine Learning Model
🌲 Random Forest Regressor

Chosen because it:<br>

✔ Captures non-linear relationships<br>
✔ Works well on large datasets<br>
✔ Stable + robust<br>
✔ Avoids overfitting<br>
✔ Does not require feature scaling<br>

📌 Achieved R² score of 0.987.

🎨📊 What the App Shows<br>
🔮 Manual Popularity Prediction (Example Input)<br>
Platform: Instagram<br>
Media Type: Image<br>
Likes: 100<br>
Comments: 10<br>
Shares: 1<br>
Followers: 1000<br>
Caption Length: 100<br>


⭐ Predicted ER: 0.1110<br>
🔥 Popularity: HIGH<br>

📊 Platform Insights

Selected Platform: All

Posts analyzed: 10000

Histogram of engagement rate

Summary statistics

⚖️ Model Evaluation (Live App)

📊 R² Score → 0.987
📉 RMSE → 0.00358
⚖️ MAE → 0.00232

🛠️ How to Run Locally<br>
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

🐍 Python<br>
🎨 Streamlit<br>
📊 Pandas, NumPy<br>
📈 Scikit-learn<br>
🌲 Random Forest Regressor<br>
📦 Joblib<br>
⚡ Plotly<br>
🪶 PyArrow (Parquet)<br>
📝 Custom Logging<br>

🤝 Contributing

Pull requests and issues are welcome!
Feel free to improve models, UI, dataset, or deployment.

📜 License

📝 MIT License — free to use, modify, and share.