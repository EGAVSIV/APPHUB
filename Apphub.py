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

    st.title("🙏 Welcome To Gs World 🔐 Login Required to Access")

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
# APP REGISTRY (UNCHANGED)
# ================================
APPS = [  # <-- your full list unchanged
    {"name": "🪐 Planetary Aspect Scanner", "category": "Astrology+Equity", "url": "https://aspectfilter.streamlit.app/"},
    {"name": "📉 Stocks on Aspects", "category": "Astrology+Equity", "url": "https://stock-scanner-ascpect.streamlit.app/"},
    {"name": "🔁 F&O Reversal", "category": "FNO & Astro", "url": "https://fnoreversalpnt.streamlit.app/"},
    {"name": "🌍 Live Planet Position", "category": "Astrology", "url": "https://liveplanetpostion.streamlit.app/"},
    {"name": "🤵 RaoSaab Desk", "category": "Screener", "url": "https://raosaab.streamlit.app/"},
    {"name": "💰 FII–DII Tracker", "category": "Market Data", "url": "https://fiidii.streamlit.app/"},
    {"name": "📐 Gann Cycle", "category": "GANN", "url": "https://ganncycle.streamlit.app/"},
    {"name": "⏱️ NIFTY Time Cycle", "category": "Index", "url": "https://niftytimecycle.streamlit.app/"},
    {"name": "⚡ Intraday Reversal", "category": "FNO & Astro", "url": "https://intradayreversal.streamlit.app/"},
    {"name": "📊 Multi TF Screener", "category": "Screener", "url": "https://multis.streamlit.app/"},
    {"name": "📉 OI Decay", "category": "FNO", "url": "https://oidecay.streamlit.app/"},
    {"name": "📉 Option Chain", "category": "FNO", "url": "https://optionchainbygaurav.streamlit.app/"},
    {"name": "📚 OI Analytics", "category": "FNO", "url": "https://oiwithgsy.streamlit.app/"},
    {"name": "☀️ Sun Cycle", "category": "Astrology+Equity", "url": "https://suncycle.streamlit.app/"},
    {"name": "🌠 Kundali", "category": "Astrology", "url": "https://birthhcharts.streamlit.app/"},
]

# ================================
# SEARCH & FILTER
# ================================
search = st.text_input("🔍 Search app")
category = st.selectbox(
    "🧭 Category",
    ["All"] + sorted(set(a["category"] for a in APPS))
)

def is_live(url):
    try:
        return requests.get(url, timeout=3).status_code == 200
    except:
        return False


# ================================
# DISPLAY IN 5-COLUMN SQUARE GRID
# ================================
cols = st.columns(5)
col_index = 0

for app in APPS:
    if search.lower() not in app["name"].lower():
        continue
    if category != "All" and app["category"] != category:
        continue

    with cols[col_index]:
        st.markdown("### " + app["name"])
        st.write(" ")
        if is_live(app["url"]):
            st.success("🟢 Live")
        else:
            st.error("🔴 Down")

        st.link_button("🚀 Open", app["url"])

        st.markdown("---")

    col_index += 1
    if col_index == 5:
        cols = st.columns(5)
        col_index = 0


# ================================
# FOOTER
# ================================
st.markdown("""
---
**Designed by:**  
**Gaurav Singh Yadav**  
Built with ❤️ | Energy • Commodity • Quant Intelligence  
📱 +91-8003994518  
📧 yadav.gauravsingh@gmail.com
""")
