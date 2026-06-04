import streamlit as st
import pandas as pd

df = pd.read_csv("data/startup_data.csv")

st.title("🚀 Startup Explorer")

industry = st.selectbox(
    "Select Industry",
    sorted(df["Industry"].unique())
)

filtered = df[df["Industry"]==industry]

st.dataframe(filtered)

st.write(
    f"Total Startups: {len(filtered)}"
)
