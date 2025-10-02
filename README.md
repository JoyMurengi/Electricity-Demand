# Electricity-Demand

# Short-Term Electricity Demand Forecasting  

## Overview  
This project focuses on **short-term load forecasting (STLF)** using hourly electricity demand data from the U.S. Energy Information Administration (EIA). The goal is to predict the next 24 hours of electricity demand based on historical data.  

Accurate demand forecasting helps grid operators:  
- Maintain balance between electricity supply and demand  
- Prevent blackouts and reduce operational costs  
- Support renewable energy integration into the grid  

---

## Problem Statement  
Electricity demand fluctuates daily and seasonally due to factors such as time of day, weather, and human activity. If demand is underestimated, the grid risks blackouts; if overestimated, resources are wasted.  

**Objective:** Forecast hourly electricity demand for the next 24 hours using past demand values.  

---

## Dataset  
- **Source:** [U.S. Energy Information Administration (EIA) Open Data](https://www.eia.gov/opendata/)  
- **Type:** Hourly electricity demand (megawatts)  
- **Region Example:** New York ISO (NYISO), though other regions are available  
- **Variables:**  
  - `datetime`: timestamp of the observation  
  - `demand_mw`: electricity demand in megawatts  

The dataset is univariate (demand only) for this version.  

---

## Approach  
1. **Data Collection:** Retrieve hourly demand data from EIA  
2. **Exploratory Data Analysis (EDA):** Identify patterns, trends, seasonality, and autocorrelation  
3. **Modeling:**  
   - Baseline models: Naïve forecast, moving average  
   - Statistical models: ARIMA, SARIMA  
   - Machine learning models: XGBoost, Random Forest  
   - Deep learning models (optional): LSTM, GRU  
4. **Evaluation:** Assess forecast accuracy using metrics such as MAE, RMSE, and MAPE  

---

## Tools and Technologies  
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Statsmodels  
- Scikit-learn, XGBoost  
- TensorFlow/PyTorch (optional)  

---

## Results  
- Baseline performance established using simple models  
- Comparison of statistical and machine learning models  
- Key insights into electricity demand behavior and forecasting accuracy  

(Results will be added after implementation.)  

---

## Future Work  
- Incorporate weather and renewable generation data  
- Develop multivariate forecasting models  
- Explore probabilistic forecasting for uncertainty estimation  
- Build a dashboard for real-time demand forecasting and visualization  

---
