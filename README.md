# Short-Term Electricity Load Forecasting

## Introduction
Electricity demand fluctuates hourly and seasonally, making it challenging for grid operators to maintain stability and efficiency. Underestimating demand can cause blackouts, while overestimating leads to wasted resources. This project leverages statistical, machine learning, and deep learning techniques to provide accurate short-term electricity load forecasts, enabling better grid management and operational planning.

## Objective
Develop accurate short-term electricity load forecasts using time series–based models to support improved operational planning, efficient energy use, and grid stability.

## Project Overview
This project uses hourly electricity consumption data from the **UCI Electricity Load Diagrams (2011–2014)** dataset. The main goal is to predict future electricity demand based on historical consumption patterns, enabling reliable grid management and efficient operational planning.

### Importance of Load Forecasting
Accurate forecasting helps:

- Maintain balance between electricity supply and demand
- Improve operational efficiency and energy planning
- Reduce wastage from overproduction
- Support renewable energy integration into the grid

The project implements statistical models (ARIMA, SARIMA), machine learning models (Linear Regression, XGBoost), and deep learning approaches (LSTM, GRU) to capture both short-term fluctuations and long-term temporal dependencies.

---

## Dataset
**Source:** [UCI Electricity Load Diagrams (2011–2014)](https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014)  
**Details:**

- **Time period:** January 2011 – December 2014  
- **Frequency:** 15-minute intervals (resampled to hourly averages)  
- **Clients:** 370 anonymized Portuguese households  
- **Features:**  
  - `datetime`: timestamp of the observation (set as index)  
  - `MT_001` to `MT_370`: hourly electricity consumption (kWh)  

**Dataset Statistics:**

- DatetimeIndex: 35,065 entries  
- Missing values: None  
- Memory usage: 99.3 MB  

---

## Data Understanding & Preparation
- **Exploratory Data Analysis (EDA)**: Visualized daily/weekly load patterns and autocorrelations.
- **Time Series Analysis**:  
  - Autocorrelation Function (ACF) indicated strong persistence in load data.  
  - Partial Autocorrelation (PACF) suggested an AR(1) process.  
  - Seasonality decomposition revealed a level-shift trend around 2012 with high residual volatility.  
- **Stationarity Check (ADF Test):** p-value < 0.05 → series is likely stationary.

---

## Modeling Approach

### 1. Baseline Models
| Model             | MAE  | RMSE |
|------------------|------|------|
| Naïve Forecast    | 0.77 | 1.78 |
| Moving Average (24h) | 1.67 | 3.19 |

### 2. Statistical Time Series Models
| Model | MAE  | RMSE |
|-------|------|------|
| ARIMA | 4.43 | 6.66 |
| SARIMA | 4.57 | 6.56 |

### 3. Machine Learning Models
| Model            | Train MAE | Train RMSE | Test MAE | Test RMSE |
|-----------------|------------|------------|----------|-----------|
| Linear Regression | 1.03       | 2.33       | 1.21     | 2.41      |
| Random Forest     | 0.32       | 0.79       | 1.08     | 2.15      |
| XGBoost           | 0.58       | 1.31       | 1.04     | 2.14      |

**Best ML Model:** XGBoost

### 4. Deep Learning Models (Client MT_001)
| Model | MAE   | RMSE  |
|-------|-------|-------|
| LSTM  | 1.158 | 2.327 |
| GRU   | 1.167 | 2.340 |

**Observation:** LSTM slightly outperforms GRU and is robust for sequential dependencies.

---

## Deployment
- Trained LSTM model saved as `lstm_forecast_model.h5`
- Scaler saved as `scaler_lstm.pkl`
- Deployed for real-time forecasting through Streamlit

---

## Insights & Discussion
- **Real-world Impact:** Helps electricity providers anticipate peak demand and optimize energy distribution.
- **Key Findings:** LSTM-based forecasting captures temporal dependencies and improves grid stability.
- **Best Model:** LSTM (deep learning) for sequence forecasting, XGBoost for traditional ML approaches.

---

## Conclusion & Recommendations
- Short-term electricity load forecasting enhances grid reliability and operational efficiency.
- LSTM models provide accurate sequential forecasting and generalize well.
- Future improvements:
  - Integrate weather/temperature data for multivariate forecasting
  - Use Kenyan dataset (KPLC) for localized forecasting models
  - Develop interactive dashboards for monitoring

---
## Website  
https://gridmind-forecast.lovable.app

**Developed by:** Joy Murengi | Advanced Machine Learning Capstone 2025

