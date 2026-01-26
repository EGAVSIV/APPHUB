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
# CSS FOR SMALL SQUARE TILES
# ================================
st.markdown("""
<style>
.app-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
    gap: 16px;
}

.app-card {
    background: #0e1117;
    border: 1px solid #262730;
    border-radius: 12px;
    padding: 14px;
    height: 180px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.app-title {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 4px;
}

.app-desc {
    font-size: 12px;
    color: #b0b3b8;
}

.app-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>
""", unsafe_allow_html=True)

# ================================
# APP REGISTRY
# ================================
APPS = [
    {"name": "🪐 Planetary Aspect Scanner","category": "Astrology+Equity","desc": "Planetary aspect filter","url": "https://aspectfilter.streamlit.app/"},
    {"name": "📉 Stocks on Aspects","category": "Astrology+Equity","desc": "Astro-based stock analysis","url": "https://stock-scanner-ascpect.streamlit.app/"},
    {"name": "🔁 F&O Reversal","category": "FNO","desc": "Price & time reversal zones","url": "https://fnoreversalpnt.streamlit.app/"},
    {"name": "🌍 Live Planet Position","category": "Astrology","desc": "Real-time planet positions","url": "https://liveplanetpostion.streamlit.app/"},
    {"name": "🤵 RaoSaab Desk","category": "Screener","desc": "AS-based filtration","url": "https://raosaab.streamlit.app/"},
    {"name": "💰 FII–DII Tracker","category": "Market Data","desc": "FII & DII activity","url": "https://fiidii.streamlit.app/"},
    {"name": "📐 Gann Cycle","category": "GANN","desc": "Time & price cycles","url": "https://ganncycle.streamlit.app/"},
    {"name": "⏱ NIFTY Time Cycle","category": "Index","desc": "NIFTY forecasting","url": "https://niftytimecycle.streamlit.app/"},
    {"name": "⚡ Intraday Reversal","category": "FNO","desc": "Intraday setups","url": "https://intradayreversal.streamlit.app/"},
    {"name": "📊 Multi TF Screener","category": "Screener","desc": "Multi-timeframe scans","url": "https://multis.streamlit.app/"},
    {"name": "📉 OI Decay","category": "FNO","desc": "OI decay analysis","url": "https://oidecay.streamlit.app/"},
    {"name": "📉 Option Chain","category": "FNO","desc": "OI & strikes","url": "https://optionchainbygaurav.streamlit.app/"},
    {"name": "📚 OI Analytics","category": "FNO","desc": "Advanced OI insights","url": "https://oiwithgsy.streamlit.app/"},
    {"name": "☀️ Sun Cycle","category": "Astrology","desc": "Solar cycle timing","url": "https://suncycle.streamlit.app/"},
    {"name": "🌎 USA Weather","category": "Weather","desc": "Weather & energy impact","url": "https://usaweather.streamlit.app/"},
    {"name": "🔺🔻 FNO Backtesting","category": "Screener","desc": "Scenario backtesting","url": "https://fnobacktesting.streamlit.app/"},
    {"name": "🏦 Sector Analysis","category": "Screener","desc": "Sector rotation","url": "https://sectoranalysis.streamlit.app/"},
    {"name": "🫐 Gamma Blaster","category": "FNO","desc": "Gamma scanner","url": "https://gammascan.streamlit.app/"},
    {"name": "🟢🔴 Market Depth","category": "FNO","desc": "Order flow","url": "https://marketdepthgs.streamlit.app/"},
    {"name": "💹 TV Fundamental","category": "Screener","desc": "Fundamental screener","url": "https://fundamentalgs.streamlit.app/"},
    {"name": "❇️ TV Technical","category": "Screener","desc": "Technical screener","url": "https://technicalgs.streamlit.app/"},
    {"name": "✳️ Hybrid Screener","category": "Screener","desc": "Tech + funda","url": "https://techfunda.streamlit.app/"},
    {"name": "🌠 Kundali","category": "Astrology","desc": "Birth chart","url": "https://birthhcharts.streamlit.app/"},
]

# ================================
# SEARCH & FILTER
# ================================
search = st.text_input("🔍 Search App")
category = st.selectbox(
    "🧭 Category",
    ["All"] + sorted(set(a["category"] for a in APPS))
)

def is_live(url):
    try:
        r = requests.get(url, timeout=3)
        return r.status_code == 200
    except:
        return False

# ================================
# DISPLAY GRID
# ================================
st.markdown('<div class="app-grid">', unsafe_allow_html=True)

for app in APPS:
    if search.lower() not in app["name"].lower():
        continue
    if category != "All" and app["category"] != category:
        continue

    live = is_live(app["url"])
    status = "🟢 Live" if live else "🔴 Down"

    st.markdown(f"""
    <div class="app-card">
        <div>
            <div class="app-title">{app["name"]}</div>
            <div class="app-desc">{app["category"]}</div>
            <div class="app-desc">{app["desc"]}</div>
        </div>
        <div class="app-footer">
            <span>{status}</span>
            <a href="{app["url"]}" target="_blank">🚀 Open</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================================
# FOOTER
# ================================
st.markdown("""
---
**Designed by:**  
**Gaurav Singh Yadav**  
Built with ❤️ | Energy • Commodity • Quant  
📱 +91-8003994518  
📧 yadav.gauravsingh@gmail.com
""")
