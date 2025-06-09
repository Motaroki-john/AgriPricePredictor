# Data Description

This document provides a detailed overview of the datasets used in the AgriPricePredictor project.

---

## 📁 Dataset Summary

- **Dataset Name**: Maize Price and Weather Data
- **Source**: [e.g., Kenya National Bureau of Statistics (KNBS), Kenya Meteorological Department]
- **Format**: CSV
- **Location**: `data/raw/`

---

## 📊 Data Fields

### 1. `date`
- **Type**: Date (YYYY-MM-DD)
- **Description**: The specific day the data was recorded.

### 2. `location`
- **Type**: String
- **Description**: The town or market where maize prices were collected (e.g., Nairobi, Eldoret).

### 3. `maize_price`
- **Type**: Float
- **Description**: Price of maize per 90kg bag in Kenyan Shillings (KES).

### 4. `rainfall_mm`
- **Type**: Float
- **Description**: Amount of rainfall in millimeters.

### 5. `temperature_celsius`
- **Type**: Float
- **Description**: Average temperature in degrees Celsius.

---

## 🧹 Preprocessing Steps

- **Missing Values**: Handled using forward fill and mean imputation.
- **Date Conversion**: Parsed to datetime format.
- **Encoding**: Location column converted using one-hot encoding for ML models.

---

## 📈 Usage

The processed data is used to:
- Train a linear regression model to predict maize prices.
- Analyze how weather patterns (rainfall and temperature) affect price trends.

---

## 📝 Notes

- Ensure the `date` column is sorted before modeling.
- Rainfall data may be more granular (daily) than price data (weekly); aggregation is applied.

## Data Columns

- **Date**: Record date (format: YYYY-MM-DD).
- **Price**: Maize price in Kenyan Shillings (KES) per kilogram.
- **Market**: The specific market/location where the maize was sold (e.g., Nairobi, Eldoret).
- **Volume_Sold** *(optional)*: Quantity of maize sold in kilograms (useful for volume-based analysis).
- **Rainfall**: Amount of rainfall recorded on the date (in mm).
- **Temperature**: Average temperature (in degrees Celsius).

> This structure helps in understanding the correlation between market prices and weather patterns.
