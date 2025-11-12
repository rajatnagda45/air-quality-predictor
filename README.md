🌫️ AirSense – AI Air Quality Predictor
🧠 A Machine Learning + Flask web app that predicts the Air Quality Index (AQI) based on real-world pollutant data.

With a beautiful glassmorphism UI, live AQI categorization, and responsive design — this project merges AI + web elegantly.


🚀 Features

✅ Predicts AQI from pollutant inputs (PM2.5, PM10, NO₂, SO₂, CO, Ozone)
✅ Displays AQI Category (Good, Moderate, Poor, etc.) with color coding & emoji 😷
✅ Real-time bar chart visualization using Chart.js 📊
✅ Fully responsive, glass-effect dark UI 🌌
✅ Dynamic AQI-based recommendations
✅ Built using Flask backend and a trained ML regression model
✅ Ready for deployment (Render/Heroku compatible)


🧠 How It Works

1️⃣ User enters pollutant levels (PM2.5, PM10, NO₂, SO₂, CO, O₃).
2️⃣ The trained ML model (Random Forest Regressor) predicts the AQI value.
3️⃣ Flask backend passes the prediction to frontend.
4️⃣ Frontend shows category + color indicator + emoji + advice message.
5️⃣ Chart.js renders pollutant levels visually.


🧾 Sample Input
PM2.5	PM10	NO₂	SO₂	CO	O₃
65	110	42	16	0.8	28

Predicted AQI → 152 (Poor 😷)

