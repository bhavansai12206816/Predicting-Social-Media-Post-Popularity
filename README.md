<h1 align="center"><span style="font-size: 50px;">🌈📈 Predicting Social Media Post Popularity</span></h1>

<div align="center">
🔥 An ML-powered interactive dashboard to predict engagement, analyze platform insights & evaluate model performance — deployed on Render! 🔥
<br><br>

<a href="https://predicting-social-media-post-popularity.onrender.com">
  <img src="https://img.shields.io/badge/🚀 Live App-Click%20Here-brightgreen?style=for-the-badge&logo=streamlit" />
</a>

<a href="https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity/archive/refs/heads/main.zip">
  <img src="https://img.shields.io/badge/⬇️ Download ZIP-Project-blue?style=for-the-badge&logo=github" />
</a>
</div>

<br><br>

<h1><span style="font-size: 18px;">🌟 Overview</span></h1>

This project predicts social media post popularity using Engagement Rate (ER) and provides:
<br><br>
✨ Manual engagement prediction<br>
✨ Platform-wise analytics<br>
✨ Interactive visualizations<br>
✨ Random Forest–based ML model<br>
✨ Fully deployed Streamlit web app<br>
✨ Modular pipeline + logging<br>

<br>

<h1><span style="font-size: 18px;">🚀✨ Key Features</span></h1>

🎯 <b>1. Manual Popularity Prediction</b><br><br>

Input fields:<br>
Platform<br>
Media Type<br>
Likes<br>
Comments<br>
Shares<br>
Followers<br>
Caption Length<br><br>

Outputs:<br>
⭐ Predicted Engagement Rate: 0.1110 (11.10%)<br>
🔥 Popularity Level: HIGH<br>

<br>

📊 <b>2. Dataset Insights by Platform</b><br><br>

Filter by:<br>
Instagram / Twitter / LinkedIn / TikTok / All<br><br>

Includes:<br>
📌 Engagement rate distribution (plots)<br>
📌 Summary statistics<br>
📌 10,000+ posts analyzed<br>

<br>

📉 <b>3. Model Evaluation</b><br><br>

📊 R² Score — 0.987<br>
📉 RMSE — 0.00358<br>
⚖️ MAE — 0.00232<br>

✨ Extremely strong performance — almost perfect fit.<br>

<br>

<h1><span style="font-size: 18px;">🤖 Machine Learning Model</span></h1>

🌲 <b>Random Forest Regressor</b><br><br>

Chosen because it:<br>
✔ Captures non-linear relationships<br>
✔ Works well on large datasets<br>
✔ Stable + robust<br>
✔ Avoids overfitting<br>
✔ Does not require feature scaling<br><br>

📌 Achieved R² score of 0.987.<br>

<br>

<h1><span style="font-size: 18px;">🎨📊 What the App Shows</span></h1>

🔮 <b>Manual Popularity Prediction (Example Input)</b><br><br>

Platform: Instagram<br>
Media Type: Image<br>
Likes: 100<br>
Comments: 10<br>
Shares: 1<br>
Followers: 1000<br>
Caption Length: 100<br><br>

⭐ Predicted ER: 0.1110<br>
🔥 Popularity: HIGH<br>

<br>

<h1><span style="font-size: 18px;">📊 Platform Insights</span></h1>

Selected Platform: All<br>
Posts analyzed: 10000<br>
Histogram of engagement rate<br>
Summary statistics<br>

<br>

<h1><span style="font-size: 18px;">⚖️ Model Evaluation (Live App)</span></h1>

📊 R² Score → 0.987<br>
📉 RMSE → 0.00358<br>
⚖️ MAE → 0.00232<br>

<br>

<h1><span style="font-size: 18px;">🛠️ How to Run Locally</span></h1>

1️⃣ Clone the repository<br>
git clone https://github.com/bhavansai12206816/Predicting-Social-Media-Post-Popularity.git<br>
cd Predicting-Social-Media-Post-Popularity<br><br>

2️⃣ Install dependencies<br>
pip install -r requirements.txt<br><br>

3️⃣ Run the Streamlit app<br>
streamlit run app.py<br>

<br>

<h1><span style="font-size: 18px;">☁️ Deployment (Render)</span></h1>

Using this config:<br><br>

services:<br>
&nbsp;&nbsp;- type: web<br>
&nbsp;&nbsp;&nbsp;&nbsp;name: social-media-post-popularity<br>
&nbsp;&nbsp;&nbsp;&nbsp;env: python<br>
&nbsp;&nbsp;&nbsp;&nbsp;plan: free<br>
&nbsp;&nbsp;&nbsp;&nbsp;buildCommand: "pip install -r requirements.txt"<br>
&nbsp;&nbsp;&nbsp;&nbsp;startCommand: "streamlit run app.py --server.port=$PORT --server.address=0.0.0.0"<br>

<br>

<h1><span style="font-size: 18px;">📡 Live App</span></h1>

👉 https://predicting-social-media-post-popularity.onrender.com<br>

<br>

<h1><span style="font-size: 18px;">🧰 Technologies Used</span></h1>

🐍 Python<br>
🎨 Streamlit<br>
📊 Pandas, NumPy<br>
📈 Scikit-learn<br>
🌲 Random Forest Regressor<br>
📦 Joblib<br>
⚡ Plotly<br>
🪶 PyArrow (Parquet)<br>
📝 Custom Logging<br>

<br>

<h1><span style="font-size: 18px;">🤝 Contributing</span></h1>

Pull requests and issues are welcome!<br>
Feel free to improve models, UI, dataset, or deployment.<br>

<br>

📜 License<br>
📝 MIT License — free to use, modify, and share.<br>
