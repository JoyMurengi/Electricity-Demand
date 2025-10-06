# Electricity Load Forecasting, Clustering, and Anomaly Detection

## Overview
This project focuses on short-term electricity load forecasting, customer clustering, and anomaly detection using hourly electricity consumption data from the **UCI Electricity Load Diagrams (2011–2014)** dataset.  
The goal is to predict hourly electricity demand, identify groups of customers with similar consumption patterns, and detect unusual behavior that may indicate anomalies.

Accurate load forecasting and anomaly detection are crucial for:
- Maintaining balance between electricity supply and demand  
- Improving operational efficiency and energy planning  
- Detecting abnormal or fraudulent consumption  
- Supporting renewable energy integration into the grid  

---

## Problem Statement
Electricity demand fluctuates hourly and seasonally due to factors such as time of day, weather, and user behavior.  
If demand is underestimated, the grid risks blackouts; if overestimated, resources are wasted.  
Similarly, abnormal consumption by certain customers can indicate faults, inefficiencies, or fraud.

**Objectives:**
1. Forecast hourly electricity load using historical data.  
2. Cluster customers based on load patterns to identify behavioral similarities.  
3. Detect anomalies in customer consumption over time.

---

## Dataset
**Source:** [UCI Machine Learning Repository – Electricity Load Diagrams (2011–2014)](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014)

**Description:**
- Time period: January 2011 – December 2014  
- Frequency: 15-minute intervals (resampled to hourly averages in this project)  
- 370 clients (anonymized) from Portugal  
- Each column represents a client's electricity consumption (kWh)

**Key Variables:**
- `datetime`: timestamp of the observation (set as index)  
- `client_x`: hourly electricity consumption for client *x*

---

## Approach

### 1. Data Preprocessing
- Loaded and merged the CSV files  
- Converted timestamps to datetime and resampled to hourly data  
- Handled missing values and performed normalization  

### 2. Exploratory Data Analysis (EDA)
- Visualized overall load trends and daily/weekly seasonality  
- Examined correlation between clients  
- Identified typical consumption patterns across time  

### 3. Clustering
- Applied **PCA** for dimensionality reduction  
- Used **K-Means clustering** to group customers with similar load patterns  
- Visualized clusters in 2D/3D using PCA components  
- Interpreted cluster behavior using average profiles per cluster  

### 4. Anomaly Detection
- Detected anomalies using **distance from cluster centroids** and **threshold-based methods**  
- Identified customers or periods showing unusual consumption patterns  
- Visualized anomalies on time series plots  

### 5. Forecasting
- Modeled short-term load forecasting using hourly data  
- Implemented baseline models: Naïve, Moving Average  
- Applied regression-based models: Linear Regression, XGBoost  
- Developed deep learning models (LSTM/GRU) for sequence forecasting  
- Evaluated models using **MAE**, **RMSE**, and **MAPE**

---

## Tools and Technologies
- **Python**  
- **Pandas**, **NumPy**  
- **Matplotlib**, **Seaborn**, **Plotly**  
- **Scikit-learn** (for PCA, clustering, regression)  
- **Statsmodels** (for ARIMA/SARIMA)  
- **TensorFlow/Keras** (for LSTM and GRU models)

---

## Results
- Established baseline forecasting performance using simple models  
- Improved accuracy with machine learning and LSTM models  
- Clustered customers into meaningful groups based on usage patterns  
- Detected anomalies across clients and time intervals  

(Detailed visualizations and results will be added after implementation.)

---

## Future Work
- Integrate weather and temperature data for multivariate forecasting  
- Apply dynamic time warping (DTW) for better similarity detection  
- Develop an interactive dashboard for visualization and real-time monitoring  
- Extend the model for probabilistic and uncertainty-based forecasting  

---


