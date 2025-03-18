'''
3_Final_Results.py
'''

import streamlit as st
import pandas as pd
from streamlit_extras.stylable_container import stylable_container
from recommendation_model import get_recommendations, df, cosine_sim

st.set_page_config(page_title="DripFinder | Final Results", layout="wide")

# --- Navbar ---
st.markdown('<div style="display: flex; align-items: center; padding: 20px 40px;">', unsafe_allow_html=True)
st.image("assets/logo.png", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# --- Get User Inputs ---
user_name = st.session_state.get("user_name", "Sneakerhead")
brand = st.session_state.get("brand", "")
colorway = st.session_state.get("colorway", "")
silhouette = st.session_state.get("silhouette", "")
gender = st.session_state.get("gender", "")

# --- Safely parse max_price ---
max_price_raw = st.session_state.get("max_price", "")
try:
    max_price = float(max_price_raw)
except ValueError:
    st.error("Invalid max price input, please restart and enter a valid number.")
    st.stop()

# --- Title ---
st.markdown(f"<h2 style='font-size: 36px; font-weight: bold;'>Hey {user_name}, these are some potential cops we got for you 👟🚀</h2>", unsafe_allow_html=True)

# --- Get Recommendations ---
results_df = get_recommendations(
    Brand=brand,
    Colorway=colorway,
    Max_price=max_price,
    Silhouette=silhouette,
    Gender=gender,
    df=df,
    cosine_sim=cosine_sim
)

# --- Display Results ---
for index, row in results_df.iterrows():
    with st.container():
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(row["Image"], use_container_width=True)

        with col2:
            st.markdown(f"### {row['Brand']} | {row['Name']}")
            st.markdown(f"**Retail Price**\n\n${row['Retail Price']}")
            st.markdown(f"**Estimated Market Value**\n\n${row['Estimated Market Value']}")
            id_value = row.get('ID', 'N/A')
            sku_value = row.get('SKU', 'N/A')
            st.markdown(f"ID: {id_value}\n\nSKU: {sku_value}")
            st.markdown(f"Colorway: {row['Colorway']}")
            st.markdown(f"Silhouette: {row['Silhouette']}")

            with st.expander("Purchase Links"):
                st.markdown(f"- [StockX Link]({row['StockX Link']})")
                st.markdown(f"- [GOAT Link]({row['GOAT Link']})")

        st.markdown("---")

# --- Restart Button ---
with stylable_container("restart-btn", css_styles="""
    button {
        background-color: #333333;
        color: #ffffff;
        padding: 0.8rem 2.5rem;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        margin-top: 20px;
    }
    button:hover {
        background-color: #222222;
    }
    """):
    if st.button("Restart 🔄"):
        st.switch_page("pages/1_Recommendation_Landing.py")