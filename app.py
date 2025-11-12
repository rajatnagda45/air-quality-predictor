from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the model
MODEL_PATH = os.path.join('model', 'model.pkl')
model = pickle.load(open(MODEL_PATH, 'rb'))

# AQI Category Function
def get_aqi_category(aqi):
    aqi = float(aqi)
    if aqi <= 50:
        return ("Good", "#16a34a", "😄")
    elif aqi <= 100:
        return ("Moderate", "#facc15", "🙂")
    elif aqi <= 200:
        return ("Poor", "#fb923c", "😷")
    elif aqi <= 300:
        return ("Very Poor", "#ef4444", "🤒")
    else:
        return ("Severe", "#7c2d12", "☠️")

@app.route('/')
def home():
    return render_template('index.html', prediction=None, inputs=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        pm25 = float(request.form.get('pm25', 0))
        pm10 = float(request.form.get('pm10', 0))
        no2 = float(request.form.get('no2', 0))
        so2 = float(request.form.get('so2', 0))
        co = float(request.form.get('co', 0))
        ozone = float(request.form.get('ozone', 0))

        features = np.array([[pm25, pm10, no2, so2, co, ozone]])
        pred = model.predict(features)[0]
        pred_rounded = round(float(pred), 2)

        category, color, emoji = get_aqi_category(pred_rounded)

        inputs = {
            'PM2.5': pm25,
            'PM10': pm10,
            'NO2': no2,
            'SO2': so2,
            'CO': co,
            'Ozone': ozone
        }

        result = {
            'aqi': pred_rounded,
            'category': category,
            'color': color,
            'emoji': emoji
        }

        return render_template('index.html', prediction=result, inputs=inputs)
    except Exception as e:
        return render_template('index.html', prediction=None, error=str(e))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')
        return render_template('contact.html', success=True, name=name)
    return render_template('contact.html', success=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5005, debug=True)
