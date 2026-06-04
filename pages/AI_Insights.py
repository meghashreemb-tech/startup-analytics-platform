import streamlit as st
import pandas as pd

df = pd.read_csv("data/startup_data.csv")

st.title("🤖 AI Business Insights")

top_valuation = df.loc[
    df["Valuation (M USD)"].idxmax()
]

st.success(
    f"""
    Highest Valuation Startup:
    {top_valuation['Startup Name']}

    Valuation:
    ${top_valuation['Valuation (M USD)']}M
    """
)

top_revenue = df.loc[
    df["Revenue (M USD)"].idxmax()
]

st.info(
    f"""
    Highest Revenue Startup:
    {top_revenue['Startup Name']}
    """
)

industry = (
    df.groupby("Industry")
    ["Valuation (M USD)"]
    .sum()
    .idxmax()
)

st.warning(
    f"Most Valuable Industry: {industry}"
)

region = (
    df.groupby("Region")
    ["Revenue (M USD)"]
    .sum()
    .idxmax()
)

st.success(
    f"Top Revenue Region: {region}"
)
