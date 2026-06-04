import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df = pd.read_csv("data/startup_data.csv")

st.title("📊 Executive Dashboard")

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Startups",len(df))

col2.metric(
    "Total Funding",
    f"${df['Funding Amount (M USD)'].sum():,.0f}M"
)

col3.metric(
    "Total Valuation",
    f"${df['Valuation (M USD)'].sum():,.0f}M"
)

col4.metric(
    "Total Revenue",
    f"${df['Revenue (M USD)'].sum():,.0f}M"
)

st.divider()

fig = px.histogram(
    df,
    x="Funding Amount (M USD)",
    title="Funding Distribution"
)

st.plotly_chart(fig,use_container_width=True)

fig2 = px.pie(
    df,
    names="Industry",
    title="Industry Distribution"
)

st.plotly_chart(fig2,use_container_width=True)
