import streamlit as st
import requests
import time

from login import check_login   # or paste login code above directly

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
        "url": "https://multitimeframescreener.streamlit.app"
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
        live = is_live(app["url"])
        if live:
            st.success("🟢 Live")
        else:
            st.error("🔴 Down")

    with col3:
        st.link_button("🚀 Open", app["url"])

    st.divider()
