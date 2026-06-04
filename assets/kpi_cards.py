import streamlit as st

def show_kpi(title, value):

    st.markdown(
        f"""
        <div style="
            background:white;
            padding:20px;
            border-radius:15px;
            box-shadow:0px 4px 10px rgba(0,0,0,0.1);
            text-align:center;">
            <h4>{title}</h4>
            <h2>{value}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
