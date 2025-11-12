import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# 1️⃣ Load dataset
data = pd.read_csv('data/air_quality.csv', on_bad_lines='skip')
print("✅ Dataset loaded successfully")
print("📊 Columns in your dataset:")
print(data.columns)

# 2️⃣ Clean and select only the columns we need
data = data.dropna(subset=['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone', 'AQI'])

# 3️⃣ Define features (X) and target (y)
X = data[['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'Ozone']]
y = data['AQI']

# 4️⃣ Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5️⃣ Train the machine learning model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6️⃣ Evaluate the model
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))

# 7️⃣ Save the trained model
pickle.dump(model, open('model/model.pkl', 'wb'))
print("✅ Model trained & saved successfully at model/model.pkl")
