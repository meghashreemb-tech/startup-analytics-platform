import streamlit as st

from assets.load_css import local_css
from assets.custom_components import page_header

st.set_page_config(
    page_title="Startup Analytics",
    layout="wide"
)

local_css("assets/styles.css")

page_header(
    "🚀 Startup Analytics Platform",
    "Deep Business Intelligence Dashboard"
)

st.image(
    "assets/banner.jpg",
    use_container_width=True
)
