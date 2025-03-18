'''
1_Recommendation_Landing.py
'''
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="DripFinder | Lace Up", layout="wide")

# --- Navbar ---
st.markdown('<div style="display: flex; align-items: center; padding: 20px 40px;">', unsafe_allow_html=True)
st.image("assets/logo.png", width=40)
st.markdown('</div>', unsafe_allow_html=True)

# --- Hero Section with background image layered manually ---
# --- Hero Section with background image layered manually ---
from PIL import Image

banner = Image.open("assets/1_banner_image.png")

# Background Image
st.image(banner, use_column_width=True)

# Overlay Hero Text Section (manual overlay effect)
st.markdown("""
    <div style="margin-top: -350px; padding: 100px 0; text-align: center; position: relative; z-index: 999;">
        <h1 style="font-size: 48px; font-weight: bold; color: #ffffff;">Yo, let’s lace you up!</h1>
        <p style="font-size: 20px; color: #ffffff;">We need a lil’ info to make sure your sneaker recs are straight heat 🔥</p>
    </div>
""", unsafe_allow_html=True)



# --- Input Form ---
with st.form("user_info_form"):
    user_name = st.text_input("Name", placeholder="What should we call you?")
    gender = st.selectbox("Gender/Age Group (optional)", 
                          options=["", 'kids', 'men', 'women', 'toddler', 'child', 'preschool', 'youth', 'infant'],
                          index=0,
                          placeholder="How do you roll?")
    
    with stylable_container(
        "lock-btn",
        css_styles="""
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
        """,
    ):
        submitted = st.form_submit_button("Lock It In 🚀")

# --- Redirect after submission ---
if submitted:
    st.session_state["user_name"] = user_name
    st.session_state["gender"] = gender
    st.switch_page("2_Recommendation_Preferences.py")
