'''
home.py
'''

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="DripFinder", layout="wide")

# --- Navbar ---
st.markdown('<div style="display: flex; align-items: center; padding: 20px 40px;">', unsafe_allow_html=True)
st.image("assets/logo.png", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("<h1 style='text-align: center; font-size: 50px;'>DripFinder</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px; color: gray;'>AI-Powered Sneaker Picks, No Cap.</p>", unsafe_allow_html=True)

# --- CTA button with routing ---
left, center, right = st.columns([3, 2, 3])
with center:
    with stylable_container(
        "cta-btn",
        css_styles="""
        button {
            background-color: #333333;
            color: #ffffff;
            padding: 0.8rem 2.5rem;
            border-radius: 8px;
            font-weight: bold;
            border: none;
        }
        button:hover {
            background-color: #222222;
        }
        """,
    ):
        if st.button("Find Your Drip"):
            st.switch_page("pages/1_Recommendation_Landing.py")

# --- Banner Image ---
st.image("assets/jordans_banner.jpeg", use_container_width=True)

# --- Footer ---
st.markdown('<div class="team-footer">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("assets/logo.png", width=40)
with col2:
    st.markdown("#### The Team")
    st.markdown("""
    - Christiaan Kenjee Koh  
    - Kento Morita  
    - Cyan Huang  
    - Billy Hsieh  
    - Dennis Wu
    """)
st.markdown('</div>', unsafe_allow_html=True)
