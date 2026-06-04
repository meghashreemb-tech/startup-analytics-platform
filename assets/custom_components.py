import streamlit as st

def page_header(title, subtitle):

    st.markdown(
        f"""
        <div style="
            background:linear-gradient(
            90deg,
            #0A66C2,
            #4CAF50
            );
            padding:20px;
            border-radius:15px;
            color:white;">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
