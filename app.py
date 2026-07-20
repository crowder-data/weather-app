import streamlit as st
import pandas as pd

st.title("La Crosse Weather Dashboard")

df = pd.read_parquet("data/weather-app.parquet")

df["date"] = pd.to_datetime(df["date"])

month = st.selectbox(
    "Select month",
    range(1, 13)
)

filtered = df[df["date"].dt.month == month]

st.dataframe(
    filtered,
    use_container_width=True
)
