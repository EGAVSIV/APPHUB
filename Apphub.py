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

    st.title("🙏 Welcome To Gs World 🔐 Login Required to Aceess this ")

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
        "name": "🪐-☀️ Planetary Aspect Scanner",
        "category": "Astrology+Equity",
        "desc": "Filter planetary aspects between two dates using sidereal calculations.",
        "url": "https://aspectfilter.streamlit.app/"
    },
    {
        "name": "🪐-📉 Stocks Movement on Aspects",
        "category": "Astrology+Equity",
        "desc": "Astrological aspect-based stock market analysis.",
        "url": "https://stock-scanner-ascpect.streamlit.app/"
    },
    {
        "name": "🔁 F&O Reversal Price & Time ",
        "category": "FNO & Astro",
        "desc": "Identify high-probability reversal points in F&O stocks.",
        "url": "https://fnoreversalpnt.streamlit.app/"
    },

    {
        "name": "🌍-🪐-☀️ Live Planet Position",
        "category": "Astrology",
        "desc": "Real-time planetary positions with sidereal reference.",
        "url": "https://liveplanetpostion.streamlit.app/"
    },
    {
        "name": "🤵‍♂️ RaoSaab Research Desk",
        "category": "Screener",
        "desc": "Stock Filtration As per AS",
        "url": "https://raosaab.streamlit.app/"
    },
    {
        "name": "💰 FII–DII Activity Tracker",
        "category": "Market Data",
        "desc": "Track daily, weekly and monthly FII–DII activity.",
        "url": "https://fiidii.streamlit.app/"
    },
    {
        "name": "🔄 F&O Price Cycle",
        "category": "FNO",
        "desc": "Price cycle based on Weekly Close 3-69 in F&O instruments.",
        "url": "https://fnopricecycle.streamlit.app/"
    },
    {
        "name": "📐 Gann Cycle Analyzer",
        "category": "GANN",
        "desc": "Gann-based time and price cycle analysis.",
        "url": "https://ganncycle.streamlit.app/"
    },
    {
        "name": "⏱️ NIFTY Time Cycle",
        "category": "Index",
        "desc": "Time-cycle based forecasting for NIFTY.",
        "url": "https://niftytimecycle.streamlit.app/"
    },
    {
        "name": "⚡ Intraday Reversal Scanner",
        "category": "FNO & Astro",
        "desc": "Detect intraday reversal setups with precision.",
        "url": "https://intradayreversal.streamlit.app/"
    },
    {
        "name": "📰 Market News Aggregator",
        "category": "News",
        "desc": "All important market and global news at one place.",
        "url": "https://allnews.streamlit.app/"
    },
    {
        "name": "📊 Multi-Timeframe Stock Screener",
        "category": "Screener",
        "desc": "Multiple Scan Stock Selection",
        "url": "https://multis.streamlit.app/"
    },
    
    {
        "name": "1️⃣ 📉 OI Decay Scanner",
        "category": "FNO",
        "desc": "Option OI decay and expiry-based behavior analysis.",
        "url": "https://oidecay.streamlit.app/"
    },
        {
        "name": "2️⃣📉 Option Chain by Gaurav",
        "category": "FNO",
        "desc": "Option chain analysis with OI, strikes, and market structure.",
        "url": "https://optionchainbygaurav.streamlit.app/"
    },

    {
        "name": "3️⃣📚 OI Analytics (GSY)",
        "category": "FNO",
        "desc": "Advanced Open Interest analysis and insights.",
        "url": "https://oiwithgsy.streamlit.app/"
    },
    {
        "name": "☀️ Sun Cycle Analyzer",
        "category": "Astrology+Equity",
        "desc": "Solar cycle based timing and trend insights.",
        "url": "https://suncycle.streamlit.app/"
    },
    {
        "name": "🌎 USA Weather & Energy Impact",
        "category": "Weather + Commodities",
        "desc": "US weather analysis with energy and commodity impact.",
        "url": "https://usaweather.streamlit.app/"
    },
    {
        "name": "1️⃣ USA Weather (Alt-1)",
        "category": "Weather + Commodities",
        "desc": "Alternative US weather forecast dashboard.",
        "url": "https://usaweather1.streamlit.app/"
    },
    {
        "name": "2️⃣ USA Weather (Alt-2)",
        "category": "Weather + Commodities",
        "desc": "Secondary US weather and temperature analysis.",
        "url": "https://usaweather2.streamlit.app/"
    },

    
    {
        "name": "3️⃣ USA Weather (Alt-3)",
        "category": "Weather + Commodities",
        "desc": "Alternative US weather forecast dashboard.",
        "url": "https://usaweather3.streamlit.app/"
    },
    {
        "name": "4️⃣ USA Weather (Alt-4)",
        "category": "Weather + Commodities",
        "desc": "Alternative US weather forecast dashboard.",
        "url": "https://usaweather4.streamlit.app/"
    },
    {
        "name": "🔺🔻 Back Testing FNO",
        "category": "Screener",
        "desc": "Back_Testing of FNO Stock with Current matching Scenario",
        "url": "https://fnobacktesting.streamlit.app/"
    },
    {
        "name": "🏦 NIFTY Sector Analysis",
        "category": "Screener",
        "desc": "Sector anlysis with sector rotation",
        "url": "https://sectoranalysis.streamlit.app/"
    },

    {
        "name": "📦 Company Announcement to NSE",
        "category": "Screener",
        "desc": "Compnies Getting Order , Volume Spike, Mangment change Data",
        "url": "https://orderbooktrack.streamlit.app/"
    },
    {
        "name": "🫐 GAMMA_Blaster",
        "category": "FNO",
        "desc": "Cange is GAMMA Value Scanner",
        "url": "https://gammascan.streamlit.app/"
    },
    {
        "name": "🟢🔴 Market Depth_Screener",
        "category": "FNO",
        "desc": "Compnies Getting Order , Volume Spike, Mangment change Data",
        "url": "https://marketdepthgs.streamlit.app/"
    },
    {
        "name": "💹 TV_Fundmental Screener",
        "category": "Screener",
        "desc": "Fundamental Screener",
        "url": "https://fundamentalgs.streamlit.app/"
    },
    {
        "name": "❇️ TV_Technical Screener",
        "category": "Screener",
        "desc": "Technical Screener",
        "url": "https://technicalgs.streamlit.app/"
    },
    {
        "name": "✳️ TV_Hybrid Screener",
        "category": "Screener",
        "desc": "Hybrid Screener",
        "url": "https://techfunda.streamlit.app/"
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


st.markdown("""
---
**Designed by:-  
Gaurav Singh Yadav**   
🩷💛🩵💙🩶💜🤍🤎💖  Built With Love 🫶  
Energy | Commodity | Quant Intelligence 📶  
📱 +91-8003994518 〽️   
📧 yadav.gauravsingh@gmail.com ™️
""")
