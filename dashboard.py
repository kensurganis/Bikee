import streamlit as st
import sys 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.write(sys.executable)

@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv("Bike-sharing-dataset/hour.csv")
    return data

data = load_data()

st.title("Dashboard Bike-Share Analysis")

st.sidebar.title("Bio:")
st.sidebar.markdown("Nama: Kens Urganis Awangsari Puttrisia Soenarto")
st.sidebar.markdown("Email: [M258d4kx1912@bangkit.academy]")
st.sidebar.markdown("Dicoding: [M258d4kx1912]")

st.sidebar.title("Dataset Bike-Share")

if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Data Overview")
    st.write(data)

if st.sidebar.checkbox("Show Dataset Statistics"):
    st.subheader("Statistical Overview")
    st.write(data.describe())

col1, col2 = st.columns(2)

with col1:
    season_mapping = {1: "spring", 2: "summer", 3: "fall", 4: "winter"}
    data['season_label'] = data['season'].map(season_mapping)
    season_count = data.groupby('season_label')['cnt'].sum().reset_index()
    fig_season_count = px.bar(season_count, x='season_label', y='cnt', title="Season-wise Bike Share Count")
    st.plotly_chart(fig_season_count, use_container_width=True)

with col2:
    weather_count = data.groupby('weathersit')['cnt'].sum().reset_index()
    fig_weather_count = px.bar(weather_count, x='weathersit', y='cnt', title="Weather Situation-wise Bike Share Count")
    st.plotly_chart(fig_weather_count, use_container_width=True)

hourly_count = data.groupby('hr')['cnt'].sum().reset_index()
fig_hourly_count = px.line(hourly_count, x='hr', y='cnt', title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True)

fig_humidity_chart = px.scatter(data, x='hum', y='cnt', title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart, use_container_width=True)

fig_wind_speed_chart = px.scatter(data, x='windspeed', y='cnt', title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart, use_container_width=True)

fig_temp_chart = px.scatter(data, x='temp', y='cnt', title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True)

st.sidebar.title("About")
st.sidebar.info("This dashboard visualizes data from a Bike Share dataset including variables like season, temperature, humidity, and more.")
