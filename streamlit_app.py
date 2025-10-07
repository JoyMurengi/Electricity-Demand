import streamlit as st
import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt

# -----------------------------
# 1️⃣ Load Model and Scaler
# -----------------------------
@st.cache_resource
def load_artifacts():
    model = load_model("lstm_forecast_model.h5", compile=False)
    scaler = joblib.load("scaler_lstm.pkl")
    return model, scaler

model, scaler = load_artifacts()

st.title("⚡ Electricity Demand Forecasting (LSTM Model)")
st.markdown("""
This app uses a **trained LSTM deep learning model** to forecast the next hour of electricity consumption  
based on the previous 24 hours of data for a single client (e.g., MT_001).
""")

# -----------------------------
# 2️⃣ User Input Section
# -----------------------------
st.header(" Input Data")

option = st.radio(
    "How would you like to provide the last 24 hours of consumption data?",
    ("Upload CSV", "Enter manually", "Use sample data")
)

if option == "Upload CSV":
    uploaded_file = st.file_uploader("Upload a CSV with one column: 'consumption'", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        input_data = df['consumption'].values[-24:]
elif option == "Enter manually":
    user_input = st.text_area("Enter 24 comma-separated consumption values:")
    try:
        input_data = np.array([float(x) for x in user_input.split(",") if x.strip() != ""])
    except:
        input_data = None
    if input_data is not None and len(input_data) != 24:
        st.warning("Please enter exactly 24 values.")
elif option == "Use sample data":
    # Simulated data (replace with actual client MT_001 history if available)
    time_index = pd.date_range(end=pd.Timestamp.now(), periods=24, freq='H')
    input_data = np.random.uniform(200, 450, size=24)  # sample pattern
    df = pd.DataFrame({"datetime": time_index, "consumption": input_data})
    st.line_chart(df.set_index("datetime"))

# -----------------------------
# 3️⃣ Make Forecast
# -----------------------------
if 'input_data' in locals() and len(input_data) == 24:
    st.header("🔮 Forecasting Result")

    # Scale and reshape input for model
    scaled_input = scaler.transform(input_data.reshape(-1, 1))
    X_input = np.array([scaled_input])  # shape (1, 24, 1)

    # Predict
    pred_scaled = model.predict(X_input)
    pred = scaler.inverse_transform(pred_scaled)[0][0]

    # -----------------------------
    # 4️⃣ Display Results
    # -----------------------------
    st.subheader(f"Predicted Next Hour Consumption: **{pred:.2f} kWh**")

    # Plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(range(1, 25), input_data, label="Past 24 Hours", color='blue')
    ax.scatter(25, pred, color='red', label="Predicted Next Hour", s=80)
    ax.set_xlabel("Hour")
    ax.set_ylabel("Consumption (kWh)")
    ax.set_title("Electricity Consumption Forecast (LSTM)")
    ax.legend()
    st.pyplot(fig)

else:
    st.info("Provide valid 24-hour data to generate a forecast.")

# -----------------------------
# 5️⃣ Footer
# -----------------------------
st.markdown("---")
st.caption("Developed by [Your Name] | Electricity Load Forecasting Project")
