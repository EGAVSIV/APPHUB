import streamlit as st
import requests
import hashlib

# ================================
# LOGIN FUNCTION
# ================================
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("🙏 Welcome To Gs World 🔐 Login Required")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        users = st.secrets["users"]
        hashed = hashlib.sha256(password.encode()).hexdigest()

        if username in users and users[username] == hashed:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()


# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="App Hub",
    page_icon="🧭",
    layout="wide"
)

check_login()

st.title("🧭 Analytics & Scanner Hub")
st.caption("Single login • All tools • Live status")
st.divider()

# ================================
# CSS — MATCH ATTACHED IMAGE
# ================================
st.markdown("""
<style>
.app-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: 18px;
}

.app-tile {
    background: linear-gradient(180deg, #0c0f14, #090c11);
    border: 1px solid #1f2430;
    border-radius: 12px;
    height: 170px;
    padding: 14px;
    position: relative;
    cursor: pointer;
    transition: all 0.2s ease;
}

.app-tile:hover {
    transform: translateY(-3px);
    border-color: #2b3242;
}

.app-title {
    font-size: 15px;
    font-weight: 600;
    color: #ffffff;
}

.status-dot {
    position: absolute;
    bottom: 14px;
    left: 14px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #3ddc84;
}
</style>
""", unsafe_allow_html=True)

# ================================
# APP REGISTRY
# ================================
APPS = [
    {"name": "🪐 Planetary Aspect", "url": "https://aspectfilter.streamlit.app/"},
    {"name": "📉 Stocks on Aspects", "url": "https://stock-scanner-ascpect.streamlit.app/"},
    {"name": "🌍 Live Planet", "url": "https://liveplanetpostion.streamlit.app/"},
    {"name": "🔁 F&O Reversal", "url": "https://fnoreversalpnt.streamlit.app/"},
    {"name": "🤵 RaoSaab Desk", "url": "https://raosaab.streamlit.app/"},
    {"name": "💰 FII–DII Tracker", "url": "https://fiidii.streamlit.app/"},
    {"name": "📐 Gann Cycle", "url": "https://ganncycle.streamlit.app/"},
    {"name": "⚡ Intraday Reversal", "url": "https://intradayreversal.streamlit.app/"},
    {"name": "📊 Multi TF Screener", "url": "https://multis.streamlit.app/"},
]

# ================================
# LIVE CHECK
# ================================
def is_live(url):
    try:
        return requests.get(url, timeout=2).status_code == 200
    except:
        return False

# ================================
# TILE RENDER
# ================================
st.markdown('<div class="app-grid">', unsafe_allow_html=True)

for app in APPS:
    if not is_live(app["url"]):
        continue

    st.markdown(f"""
    <a href="{app["url"]}" target="_blank" style="text-decoration:none;">
        <div class="app-tile">
            <div class="app-title">{app["name"]}</div>
            <div class="status-dot"></div>
        </div>
    </a>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================================
# FOOTER
# ================================
st.markdown("""
---
**Designed by Gaurav Singh Yadav**  
Built with ❤️ | Energy • Commodity • Quant
""")
