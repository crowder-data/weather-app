import streamlit as st
import pandas as pd

st.title("La Crosse Weather Dashboard (2025)")

df = pd.read_parquet("data/weather-app.parquet")

month = st.selectbox(
    "Select month",
    ["January","February","March","April","May","June","July","August","September","October","November","December"]
)


filtered = df[df["Month"] == month]

st.dataframe(
    filtered,
    use_container_width=True
)
