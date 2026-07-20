import streamlit as st
import pandas as pd

st.title("La Crosse Weather Dashboard")

df = pd.read_parquet("data/weather-app.parquet")

month = st.selectbox(
    "Select month",
    range(1, 13)
)

filtered = df[df["Month"] == month]

st.dataframe(
    filtered,
    use_container_width=True
)
