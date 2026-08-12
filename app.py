import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE SETUP
st.set_page_config(page_title="AQI Dashboard", layout="wide")
st.title("AQI Forecasting Dashboard (India)")

# LOAD DATA
data = pd.read_csv("aqi_data.csv")
data["Date"] = pd.to_datetime(data["Date"])

# SIDEBAR
city = st.sidebar.selectbox(
    "Select City",
    sorted(data["City"].unique())
)

city_data = data[data["City"] == city].sort_values("Date")

#PAST AQI – BAR CHART (MATPLOTLIB)
st.subheader(f"Past AQI (Recent Days) – {city}")

past_data = city_data.tail(10)

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(4, 3))
    ax1.bar(past_data["Date"], past_data["AQI"])
    ax1.set_ylabel("AQI")
    ax1.tick_params(axis="x", rotation=45)
    st.pyplot(fig1, use_container_width=False)


#AQI TREND – LINE CHART (SEABORN)
with col2:
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    sns.lineplot(
        x=city_data["Date"],
        y=city_data["AQI"],
        ax=ax2
    )
    ax2.set_ylabel("AQI")
    st.pyplot(fig2, use_container_width=False)


#AQI DISTRIBUTION – SCATTER (SEABORN)
st.subheader(f"AQI Distribution – {city}")

fig3, ax3 = plt.subplots(figsize=(4, 3))
sns.scatterplot(
    x=city_data["Date"],
    y=city_data["AQI"],
    ax=ax3
)
ax3.set_ylabel("AQI")
st.pyplot(fig3, use_container_width=False)


#FUTURE AQI PREDICTION – BAR (MATPLOTLIB)
st.subheader(f"Future AQI Prediction – {city}")

last_avg_aqi = city_data["AQI"].tail(5).mean()

future_days = 7
future_aqi = [last_avg_aqi + i * 2 for i in range(future_days)]

fig4, ax4 = plt.subplots(figsize=(4, 3))
ax4.bar(range(1, future_days + 1), future_aqi)
ax4.set_xlabel("Future Days")
ax4.set_ylabel("Predicted AQI")
st.pyplot(fig4, use_container_width=False)

# RAW DATA (OPTIONAL)
with st.expander("Show Raw Data"):
    st.dataframe(city_data.tail(15))
