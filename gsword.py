import streamlit as st
import requests
import hashlib
import base64
import os

# ================================
# PAGE CONFIG
# ================================
st.set_page_config(
    page_title="GS World • App Hub",
    page_icon="🪐",
    layout="wide"
)

# ================================
# BACKGROUND FUNCTION
# ================================
def set_bg_image(image_path: str):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

BASE_PATH = os.path.dirname(__file__)
bg_path = os.path.join(BASE_PATH, "Assets", "BG11.png")

if os.path.exists(bg_path):
    set_bg_image(bg_path)

# ================================
# LOGIN
# ================================
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.title("🔐 GS WORLD • Secure Login")

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

check_login()

# ================================
# HEADER
# ================================
st.title("🪐 GS WORLD • APP HUB")
st.caption("Astro • FNO • Technical • Fundamental • Commodity • Gann")

# ================================
# APP REGISTRY (UPDATED MAPPING)
# ================================

APPS = [

# ASTROLOGY
{"name":"Aspect Filter","category":"ASTROLOGY","url":"https://aspectfilter.streamlit.app","desc":"Upcoming & Past Aspects"},
{"name":"Live Planet Position","category":"ASTROLOGY","url":"https://liveplanetpostion.streamlit.app","desc":"Live Planet Position"},
{"name":"Kundali","category":"ASTROLOGY","url":"https://birthhcharts.streamlit.app","desc":"Janam Kundali with planetary chart"},

# FINASTRO
{"name":"Stock Aspect Movement","category":"FINASTRO","url":"https://stock-scanner-ascpect.streamlit.app","desc":"Stocks moving on aspects"},
{"name":"FNO Reversal Time","category":"FINASTRO","url":"https://fnoreversalpnt.streamlit.app","desc":"Daily reversal time of FNO"},
{"name":"All Cycle Scan","category":"FINASTRO","url":"https://allcycles.streamlit.app","desc":"All cycle scanner"},
{"name":"FNO Price Cycle","category":"FINASTRO","url":"https://fnopricecycle.streamlit.app","desc":"30-60-90 cycles"},
{"name":"Intraday Reversal","category":"FINASTRO","url":"https://intradayreversal.streamlit.app","desc":"Nakshatra time reversal"},
{"name":"Sun Cycle","category":"FINASTRO","url":"https://suncycle.streamlit.app","desc":"Sun move cycle scanner"},

# FUNDAMENTAL
{"name":"Order Book Tracker","category":"FUNDAMENTAL","url":"https://orderbooktrack.streamlit.app","desc":"Daily order receiving"},
{"name":"FII DII Tracker","category":"FUNDAMENTAL","url":"https://fiidii.streamlit.app","desc":"FII-DII Activity"},
{"name":"Fundamental Screener","category":"FUNDAMENTAL","url":"https://fundamentalgs.streamlit.app","desc":"PE, ROE, ROA Scan"},
{"name":"MF Entry Exit 1","category":"FUNDAMENTAL","url":"https://mfhanalysis2.streamlit.app","desc":"Mutual fund flow"},
{"name":"MF Entry Exit 2","category":"FUNDAMENTAL","url":"https://mfhanalysis.streamlit.app","desc":"Mutual fund flow"},
{"name":"Screener App","category":"FUNDAMENTAL","url":"https://screenersapp.streamlit.app","desc":"Cookies based screener"},

# TECHNICAL
{"name":"RaoSaab Scanner","category":"TECHNICAL SCAN","url":"https://raosaab.streamlit.app","desc":"AS Parameter scan"},
{"name":"Dow Theory","category":"TECHNICAL SCAN","url":"https://dowtheory.streamlit.app","desc":"Trend measure"},
{"name":"Fib Retracement","category":"TECHNICAL SCAN","url":"https://fibretracement.streamlit.app","desc":"Fib levels"},
{"name":"Multi Technical Scan","category":"TECHNICAL SCAN","url":"https://multis.streamlit.app","desc":"All technical scan"},
{"name":"MACD Trend","category":"TECHNICAL SCAN","url":"https://8003994518.streamlit.app","desc":"MACD trend detection"},
{"name":"Hybrid Scan","category":"TECHNICAL SCAN","url":"https://techfunda.streamlit.app","desc":"Tech + funda"},
{"name":"Technical Screener","category":"TECHNICAL SCAN","url":"https://technicalgs.streamlit.app","desc":"EMA RSI ADX BB Scan"},

# OPTION CHAIN
{"name":"Gamma Blast 1","category":"OPTION CHAIN+GREEKS","url":"https://gammascan.streamlit.app","desc":"Gamma Scan"},
{"name":"Gamma Blast 2","category":"OPTION CHAIN+GREEKS","url":"https://gammascan1.streamlit.app","desc":"Gamma Scan 2"},
{"name":"Market Depth","category":"OPTION CHAIN+GREEKS","url":"https://marketdepthgs.streamlit.app","desc":"Live market depth"},
{"name":"Option Chain 1","category":"OPTION CHAIN+GREEKS","url":"https://optionchainbygaurav.streamlit.app","desc":"Option chain 1"},
{"name":"Option Chain 2","category":"OPTION CHAIN+GREEKS","url":"https://oiwithgaurav.streamlit.app","desc":"Option chain 2"},
{"name":"Option Chain 3","category":"OPTION CHAIN+GREEKS","url":"https://oiwithgsy.streamlit.app","desc":"Option chain 3"},
{"name":"OI Decay","category":"OPTION CHAIN+GREEKS","url":"https://oidecay.streamlit.app","desc":"OI Decay scanner"},

# GANN
{"name":"Gann Cycle","category":"GANN","url":"https://ganncycle.streamlit.app","desc":"Gann cycles"},
{"name":"Nifty Time Cycle","category":"GANN","url":"https://niftytimecycle.streamlit.app","desc":"Gann Nifty time cycle"},

# SECTOR
{"name":"Sector Compare","category":"SECTOR ANALYSIS","url":"https://secsea.streamlit.app","desc":"Sector comparison"},
{"name":"Sector Seasonal","category":"SECTOR ANALYSIS","url":"https://sectoranalysis.streamlit.app","desc":"Seasonal impact"},

# COMMODITY
{"name":"USA Weather","category":"COMMODITY","url":"https://usaweather.streamlit.app","desc":"US Weather"},
{"name":"USA Weather 1","category":"COMMODITY","url":"https://usaweather1.streamlit.app","desc":"Weather alt"},
{"name":"USA Weather 2","category":"COMMODITY","url":"https://usaweather2.streamlit.app","desc":"Weather alt"},
{"name":"USA Weather 3","category":"COMMODITY","url":"https://usaweather3.streamlit.app","desc":"Weather alt"},
{"name":"USA Weather 4","category":"COMMODITY","url":"https://usaweather4.streamlit.app","desc":"Weather alt"},

# OTHERS
{"name":"GS Algo","category":"Others","url":"https://gsalgo.streamlit.app","desc":"Algo trading"},
{"name":"GeoTrader","category":"Others","url":"https://geotrader.streamlit.app","desc":"Geo trading"},
{"name":"LTP Monitor","category":"Others","url":"https://lasttradedprice.streamlit.app","desc":"LTP tracking"},
{"name":"News","category":"Others","url":"https://allnews.streamlit.app","desc":"All news"},
{"name":"News API","category":"Others","url":"https://oneindianews.streamlit.app","desc":"News with API"},
{"name":"FNO Backtesting","category":"Others","url":"https://fnobacktesting.streamlit.app","desc":"Best run condition"},
{"name":"Trading Journal","category":"Others","url":"https://tradingjournalgs.streamlit.app","desc":"Journal tracking"},
]

# ================================
# CATEGORY NAVIGATION
# ================================

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

categories = sorted(set(app["category"] for app in APPS))

# ================================
# HOME PAGE → SHOW ONLY CATEGORIES
# ================================

if st.session_state.selected_category is None:

    st.subheader("📂 Select Category")

    cols = st.columns(4)
    i = 0

    for cat in categories:
        with cols[i]:
            if st.button(cat, use_container_width=True):
                st.session_state.selected_category = cat
                st.rerun()
        i += 1
        if i == 4:
            cols = st.columns(4)
            i = 0

# ================================
# CATEGORY PAGE → SHOW APPS
# ================================

else:

    cat = st.session_state.selected_category

    col1, col2 = st.columns([6,1])
    with col1:
        st.subheader(f"📁 {cat}")
    with col2:
        if st.button("⬅ Back"):
            st.session_state.selected_category = None
            st.rerun()

    st.divider()

    filtered_apps = [a for a in APPS if a["category"] == cat]

    for app in filtered_apps:
        st.markdown(f"### {app['name']}")
        st.write(app["desc"])
        st.link_button("🚀 Launch App", app["url"])
        st.divider()
