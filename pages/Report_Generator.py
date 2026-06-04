import streamlit as st
import pandas as pd

df = pd.read_csv("data/startup_data.csv")

st.title("📄 Report Generator")

st.subheader("Dataset Preview")

st.dataframe(df.head())

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV Report",
    data=csv,
    file_name="startup_report.csv",
    mime="text/csv"
)

st.success("Report Ready")
