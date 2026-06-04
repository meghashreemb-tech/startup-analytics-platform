import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/startup_data.csv")

st.title("📈 Deep Analytics")

tab1,tab2,tab3 = st.tabs([
    "Valuation",
    "Revenue",
    "Market Share"
])

with tab1:

    fig = px.scatter(
        df,
        x="Revenue (M USD)",
        y="Valuation (M USD)",
        color="Industry",
        size="Employees",
        hover_name="Startup Name"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with tab2:

    revenue = df.groupby(
        "Industry"
    )["Revenue (M USD)"].sum()

    fig = px.bar(
        revenue,
        title="Revenue by Industry"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with tab3:

    fig = px.box(
        df,
        x="Industry",
        y="Market Share (%)",
        color="Industry"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
