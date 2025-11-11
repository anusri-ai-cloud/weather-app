import streamlit as st
import requests

st.set_page_config(page_title="Weather Forecast", page_icon="🌦", layout="centered")

st.title("🌦 Simple Weather Forecast App")
st.write("Enter any city name below to get real-time weather details!")

city = st.text_input("🔍 City name:")

if st.button("Get Weather"):
    api_key = "73959b17ea5e7b69a18f3e4b99c5270b"  # <-- replace with your OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()

    if data["cod"] == 200:
        st.success(f"**Weather for {city.title()}**")
        st.write(f"🌡 Temperature: {data['main']['temp']}°C")
        st.write(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        st.write(f"☁ Condition: {data['weather'][0]['description'].title()}")
        st.write(f"💧 Humidity: {data['main']['humidity']}%")
    else:
        st.error("City not found! Please enter a valid city name.")
