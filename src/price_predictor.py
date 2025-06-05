import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# Announce our epic quest
print("Embarking on a data adventure at", os.path.abspath(__file__))

# Seek the data treasure
data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'maize_prices.csv')
print("Searching for data at", os.path.abspath(data_path))
try:
    data = pd.read_csv(data_path)
    print("Treasure found! Data shape:", data.shape)
except FileNotFoundError:
    print("Alas! The data treasure 'maize_prices.csv' eludes us!")
    exit(1)
except Exception as e:
    print(f"A dragon blocks our path: {e}")
    exit(1)

data['Date'] = pd.to_datetime(data['Date'])
data['Days'] = (data['Date'] - data['Date'].min()).dt.days
print("Data prepared. Peek at the treasure:", data.head())

# Prepare for the model battle with weather magic
print("Gearing up the Random Forest model with rainfall power...")
X = data[['Days', 'Rainfall']].values
y = data['Maize_Price'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training squad ready. Size:", X_train.shape)

# Train the mighty Random Forest model
print("Unleashing the Random Forest training!")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model trained! Skipping score due to limited data.")

# Interactive prediction horizons (multiple)
print("\nChoose your prediction horizons, brave adventurer!")
print("Enter multiple days into the future (e.g., '30 60 90'), separated by spaces:")
while True:
    try:
        horizons = [int(day) for day in input("Days ahead: ").strip().split()]
        if all(day > 0 for day in horizons):
            break
        else:
            print("Please enter positive numbers only!")
    except ValueError:
        print("Invalid input! Enter numbers like '30 60 90'.")

# Predict for each horizon
last_day = X[-1][0]
last_rainfall = data['Rainfall'].iloc[-1]
last_price = data['Maize_Price'].iloc[-1]
last_date = data['Date'].max()

predictions = []
plt.figure(figsize=(12, 8))
plt.plot(data['Date'], data['Maize_Price'], label='Historical Prices', marker='o', color='green', linewidth=2)

for days in horizons:
    print(f"\nPeering {days} days into the future...")
    future_day = last_day + days
    future_price = model.predict([[future_day, last_rainfall]])
    future_date = last_date + pd.Timedelta(days=days)
    print(f"Predicted maize price in {days} days: KES {future_price[0]:.2f}")

    # Save prediction to list
    predictions.append({
        'Future_Date': future_date,
        'Predicted_Price': future_price[0],
        'Days_Ahead': days,
        'Rainfall_Used': last_rainfall
    })

    # Plot the prediction
    plt.plot([last_date, future_date], [last_price, future_price[0]], 
             label=f'Predicted Price ({days} days)', linestyle='--', marker='*', linewidth=2)

# Save predictions to CSV (append mode)
print("\nRecording predictions in ancient scrolls...")
prediction_data = pd.DataFrame(predictions)
prediction_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'predictions.csv')
if os.path.exists(prediction_path):
    existing_data = pd.read_csv(prediction_path)
    updated_data = pd.concat([existing_data, prediction_data], ignore_index=True)
    updated_data.to_csv(prediction_path, index=False)
else:
    prediction_data.to_csv(prediction_path, index=False)
print(f"Predictions recorded at: {os.path.abspath(prediction_path)}")

# Craft the legendary visualization
print("Weaving the price trend masterpiece...")
try:
    visuals_path = os.path.join(os.path.dirname(__file__), '..', 'visuals')
    os.makedirs(visuals_path, exist_ok=True)
    print("Canvas set at:", os.path.abspath(visuals_path))
    plt.title('Epic Maize Price Trend & Predictions (Random Forest)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (KES)', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    save_path = os.path.join(visuals_path, 'price_trend.png')
    print(f"Painting saved to: {os.path.abspath(save_path)}")
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Masterpiece complete at: {os.path.abspath(save_path)}")
except Exception as e:
    print(f"The art failed! Error: {e}")
    exit(1)