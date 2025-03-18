'''
2_Recommendation_Preferences.py
'''

import streamlit as st
from streamlit_extras.stylable_container import stylable_container

st.set_page_config(page_title="DripFinder | Preferences", layout="wide")

# --- Navbar ---
st.markdown('<div style="display: flex; align-items: center; padding: 20px 40px;">', unsafe_allow_html=True)
st.image("assets/logo.png", width=100)
st.markdown('</div>', unsafe_allow_html=True)

# --- Brand & Silhouette Mapping ---
brand_silhouettes = {
    'Jordan': ['air jordan 1', 'air jordan 1 brooklyn', 'air jordan 11', 'air jordan 12', 'air jordan 14', 'air jordan 2/3', 'air jordan 20', 'air jordan 3', 'air jordan 39', 'air jordan 4', 'air jordan 4 rm', 'air jordan 5', 'air jordan 7', 'air jordan 9', 'air ship', 'jordan 23', 'jordan adg 5', 'jordan day 1', 'jordan flight court', 'jordan heir', 'jordan hydro slide', 'jordan jumpman jack', 'jordan jumpman slide', 'jordan legacy 312', 'jordan luka 3', 'jordan max aura', 'jordan mvp', 'jordan one take 5', 'jordan post slide', 'jordan roam', 'jordan spizike', 'jordan stadium 90', 'jordan stay loyal', 'jordan tatum 3'],
    'Nike': ['acg izy', "air dt max '96", 'air foamposite', 'air force 1', "air force 1 low '07", "air force 1 low '07 lv8", 'air force 3', 'air max 1', 'air max 1000', 'air max 2013', 'air max 90', 'air max 95', 'air max dn', 'air max muse', 'air max plus', 'air max portal', 'air max sc', 'air max sunder', 'air max tl 2.5', 'air max waffle', 'air max waffle racer', 'air more uptempo', 'air pegasus wave', 'air sunder max', 'air tech challenge 2', 'air trainer huarache', 'air zoom alphafly next% 3', 'air zoom diamond elite', 'air zoom gt cut 3', 'air zoom gt hustle 2', 'air zoom gt hustle 3', 'air zoom gt jump 2', 'air zoom pegasus 41', 'air zoom rival fly 4', 'air zoom spiridon', 'air zoom victory tour', 'air zoom vomero 5', "blazer mid '77", 'blazer sb', 'book 1', 'c1', 'c1ty', 'cortez', 'court borough', 'dunk', 'dunk low ducks', 'dunk low se', 'dunk sb', 'flex experience', 'free metcon', 'gato', 'giannis immortality 4', 'giannis zoom freak 6', 'gt hustle 3', 'huarache 9', 'in-season', 'ja 2', 'journey run', 'kd 17', 'kd 4', 'kobe 5', 'kobe 9', 'kobe 9 elite protro christmas (2024', 'lebron 22', 'lebron tr 1', 'little posite', 'little posite one copper (2024', 'lunar roam', 'metcon 1', 'metcon 9', 'nike kd 17', 'p-6000', 'pegasus wave', 'reactx infinity run', 'renew elevate 3', 'sabrina 2', 'shox r4', 'shox ride', 'shox tl black', 'superrep cycle', 'team hustle d11', 'vapor edge', 'vapor edge kobe 6', 'zoom fly 6', 'zoom gp challenge pro', 'zoom mercurial superfly 10', 'zoom mercurial vapor 1', 'zoom mercurial vapor 16', 'zoom spiridon', 'zoomx vaporfly next% 3'],
    'Puma': ['accelerate nitro', 'all-pro nitro', 'all-pro nitro elite', 'amplifier', 'avanti', 'axelion', 'ca pro', 'cali', 'carina', 'caven', 'cell thrill', 'clyde', 'clyde soph', 'cool cat slides', 'dagger', 'desierto', 'deviate nitro 3', 'dribble', 'easy rider', 'extend lite trail', 'extos', 'fast-rb nitro elite', 'fast-trac nitro 3', 'forever', 'foreverrun nitro', 'future match', 'future play', 'future pro', 'future rider', 'future ultimate', 'genetics', 'gv special', 'hypnotic', 'indoor og', 'inhale', 'king', 'king ultimate', 'kruz', 'lafrancé', 'leadcat slide', 'magmax nitro', 'mayze', 'mayze wellis', 'mb.03', 'mb.04', 'mb.04 slide', 'mostro', 'mostro san san', 'neutron', 'palermo', 'park lifestyle', 'puma court', 'puma trinity', 'puma ultra pro', 'pwr nitro squared 2', 'r78', 'rdr', 'rebound v6', 'roma', 'rs-x', 'scend pro', 'softride frequence', 'speedcat', 'speedcat archive haute', 'speedcat archive team', 'spirex', 'stewie 3', 'suede', 'ultra 5 ultimate', 'ultra play', 'velophasis', 'vis2k', 'voyage nitro', 'x-ray'],
    'adidas': ['adidas italia', 'adilette', 'adimatic', 'adistar cushion', 'adizero adios pro 4', 'adizero adios pro evo 1', 'adizero electric', 'adizero electric+', 'adizero evo sl', 'adizero f50', 'adizero impact', 'adizero instinct', 'aloha super', 'break start', 'campus', 'centennial', 'climamog', 'codechaos', 'country', 'courtblock', 'crazy 8', 'crazy 98', 'crazy iiinfinity', 'crazy iiinfinity 130', 'd.o.n. issue #6', 'dame 9', 'dame certified 3', 'defiant speed', 'duramo', 'equipment agravic', 'freak', 'galaxy 7', 'gazelle', 'goletto', 'grand court', 'gt', 'gt manchester', 'handball', 'harden vol. 8', 'helvellyn', 'hoops', 'hoops 3.0', 'jabbar', 'kaptir', 'kouza', 'lite racer adapt', 'lotherton', 'mad iiinfinity', 'megaride o1', 'moonboost', 'mundial team', 'nmd_g1', 'nova iiinfinity', 'novaflight', 'ozweego', 'palos hills', 'predator 24 league', 'predator elite', 'prototype trx', 'racer', 'racer tr23', 'radlander', 'rivalry', 'runfalcon 3.0', 'samba', 'semm cumasch', 'sl72', 'sl83', 'superstar', 'superstar adv', 'terrex ax4', 'terrex hyperhiker', 'turnaround', 'ultimashow 2.0', 'velosamba', 'vl court', 'wimberly', 'x crazyfast'],
    'New Balance': ['1000', '1080', '1080v14', '1500', '1906', '1906l', '2002r', '272', '3000v7', '327', '408', '475', '480', '508', '509', '530', '550', '574', '580', '740', '8040', '860', '880', '9060', '990v4', '990v6', '991v2', '993', '996v6', 'balance 2002', 'balance 530', 'balance 550', 'balance 574', 'coco cg2', 'freezelx', 'freezelx box', 'fresh foam arishi', 'fresh foam cruz', 'fresh foam x 840', 'fuelcell supercomp trainer v3', 'furon', 'kawhi 4', 'minimus trail', 'numeric 1010', 'numeric 306', 'numeric 417', 'numeric 425', 'numeric 440', 'numeric 574', 'numeric 600', 'numeric 808', 'rainier', 't500', 'tekela', 'two wxy v5', 'wrpd runner']
}

# --- Form ---
st.markdown("## Your Drip Checklist")
st.markdown("Tell us what you’re feelin’ and we’ll find your next heat drop 🔥")

# Brand selector (optional)
brand = st.selectbox(
    "Brand (Optional)", 
    options=[""] + ['Jordan', 'Nike', 'Puma', 'adidas', 'New Balance'], 
    index=0
)
brand = brand if brand != "" else None
st.caption("Leave blank to consider all brands")

# Max price input
max_price = st.text_input("Max Price", placeholder="Type your max price here...")

# Dynamically load silhouette options based on brand selection
if brand:
    silhouettes = brand_silhouettes.get(brand, [])
else:
    # If no brand is selected, show all unique silhouettes from all brands
    all_silhouettes = []
    for s_list in brand_silhouettes.values():
        all_silhouettes.extend(s_list)
    silhouettes = sorted(set(all_silhouettes))

# Silhouette selector (optional)
silhouette = st.selectbox(
    "Silhouette (Optional)",
    options=[""] + silhouettes,
    index=0
)
silhouette = silhouette if silhouette != "" else None

# Pre-filled common color options for tag-style multi-select
common_colors = ['red', 'white', 'black', 'blue', 'green', 'yellow', 'grey', 'purple', 'orange', 'brown', 'beige', 'pink']
colorway_tags = st.multiselect(
    "Colorway (Optional)",
    options=common_colors,
    default=[],
    placeholder="Type a color and hit Enter (e.g., red, white, blue)"
)

# CTA button
with stylable_container("show-btn", css_styles="""
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
    if st.button("Show Me the Heat 🔥"):
        st.session_state["brand"] = brand
        st.session_state["max_price"] = max_price
        st.session_state["colorway"] = "/".join(colorway_tags)
        st.session_state["silhouette"] = silhouette
        st.switch_page("pages/3_Final_Results.py")