import streamlit as st
import requests
import hashlib

# ================================
# LOGIN FUNCTION (SAME FILE)
# ================================
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("🔐 Login Required")

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
# APP REGISTRY
# ================================
APPS = [
    {
        "name": "🪐 Planetary Aspect Scanner",
        "category": "Astrology",
        "desc": "Planetary aspect filtering between two dates (Sidereal).",
        "url": "https://aspectfilter.streamlit.app"
    },
    {
        "name": "📊 Multi-Timeframe Stock Screener",
        "category": "Stock Market",
        "desc": "EMA, trend, breakout, multi-timeframe scanner.",
        "url": "https://multis.streamlit.app/"
    },
    {
        "name": "📉 OI & Option Chain Analyzer",
        "category": "Derivatives",
        "desc": "OTM decay, Greeks, expiry-wise option chain analysis.",
        "url": "https://oi-scanner.streamlit.app"
    }
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
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except:
        return False

# ================================
# DISPLAY APPS
# ================================
for app in APPS:
    if search.lower() not in app["name"].lower():
        continue
    if category != "All" and app["category"] != category:
        continue

    col1, col2, col3 = st.columns([4, 2, 2])

    with col1:
        st.subheader(app["name"])
        st.write(app["desc"])
        st.caption(f"Category: {app['category']}")

    with col2:
        if is_live(app["url"]):
            st.success("🟢 Live")
        else:
            st.error("🔴 Down")

    with col3:
        st.link_button("🚀 Open", app["url"])

    st.divider()
