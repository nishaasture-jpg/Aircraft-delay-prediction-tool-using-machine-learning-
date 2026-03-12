import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
data = pd.read_csv("aircraft_delay_dataset.csv")

# Features and target
X = data[['DISTANCE','TEMP','WIND','WEATHER_DELAY']]
y = data['DEP_DELAY']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100)
model.fit(X_train,y_train)

# Prediction test
predictions = model.predict(X_test)

# Model accuracy
mse = mean_squared_error(y_test,predictions)

print("Model trained successfully")
print("Mean Squared Error:",mse)

# Save model
joblib.dump(model,"aircraft_delay_model.pkl")

print("Model saved as aircraft_delay_model.pkl")

# User prediction input
print("\n---- Aircraft Delay Prediction ----")

distance = float(input("Enter Flight Distance: "))
temp = float(input("Enter Temperature: "))
wind = float(input("Enter Wind Speed: "))
weather = float(input("Enter Weather Delay: "))

input_data = np.array([[distance,temp,wind,weather]])

prediction = model.predict(input_data)

print("Predicted Aircraft Delay:",prediction[0],"minutes")