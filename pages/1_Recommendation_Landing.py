'''
1_Recommendation_Landing.py
'''
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="DripFinder | Lace Up", layout="wide")

# --- Navbar ---
st.markdown('<div style="display: flex; align-items: center; padding: 20px 40px;">', unsafe_allow_html=True)
st.image("assets/logo.png", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# --- Hero Section with background image ---
from PIL import Image

banner = Image.open("assets/1_banner_image.png")

# Background Image
st.image(banner, use_container_width=True)

# Overlay Hero Text with faint black gradient
st.markdown("""
    <div style="
        margin-top: -500px;
        position: relative;
        z-index: 999;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 400px;
    ">
        <div style="
            background: rgba(0, 0, 0, 0.4);
            padding: 40px 60px;
            border-radius: 12px;
            text-align: center;
        ">
            <h1 style="font-size: 48px; font-weight: bold; color: #ffffff; margin-bottom: 10px;">Yo, let’s lace you up!</h1>
            <p style="font-size: 20px; color: #ffffff;">We need a lil’ info to make sure your sneaker recs are straight heat 🔥</p>
        </div>
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
    st.switch_page("pages/2_Recommendation_Preferences.py")