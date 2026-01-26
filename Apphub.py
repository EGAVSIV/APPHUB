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
# COMPACT TILE CSS (KEY CHANGE)
# ================================
st.markdown("""
<style>
.app-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 10px;
}

.app-card {
    background: #0e1117;
    border: 1px solid #262730;
    border-radius: 10px;
    padding: 8px;
    height: 120px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.app-title {
    font-size: 13px;
    font-weight: 600;
    line-height: 1.2;
}

.app-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
}
</style>
""", unsafe_allow_html=True)

# ================================
# APP REGISTRY
# ================================
APPS = [
    {"name": "🪐 Planetary Aspect","category": "Astrology+Equity","url": "https://aspectfilter.streamlit.app/"},
    {"name": "📉 Stocks on Aspects","category": "Astrology+Equity","url": "https://stock-scanner-ascpect.streamlit.app/"},
    {"name": "🔁 F&O Reversal","category": "FNO","url": "https://fnoreversalpnt.streamlit.app/"},
    {"name": "🌍 Live Planet","category": "Astrology","url": "https://liveplanetpostion.streamlit.app/"},
    {"name": "🤵 RaoSaab Desk","category": "Screener","url": "https://raosaab.streamlit.app/"},
    {"name": "💰 FII–DII","category": "Market Data","url": "https://fiidii.streamlit.app/"},
    {"name": "📐 Gann Cycle","category": "GANN","url": "https://ganncycle.streamlit.app/"},
    {"name": "⏱ NIFTY Cycle","category": "Index","url": "https://niftytimecycle.streamlit.app/"},
    {"name": "⚡ Intraday","category": "FNO","url": "https://intradayreversal.streamlit.app/"},
    {"name": "📊 Multi TF","category": "Screener","url": "https://multis.streamlit.app/"},
    {"name": "📉 OI Decay","category": "FNO","url": "https://oidecay.streamlit.app/"},
    {"name": "📉 Option Chain","category": "FNO","url": "https://optionchainbygaurav.streamlit.app/"},
    {"name": "📚 OI Analytics","category": "FNO","url": "https://oiwithgsy.streamlit.app/"},
    {"name": "☀️ Sun Cycle","category": "Astrology","url": "https://suncycle.streamlit.app/"},
    {"name": "🌎 USA Weather","category": "Weather","url": "https://usaweather.streamlit.app/"},
    {"name": "🔺🔻 Backtesting","category": "Screener","url": "https://fnobacktesting.streamlit.app/"},
    {"name": "🏦 Sector","category": "Screener","url": "https://sectoranalysis.streamlit.app/"},
    {"name": "🫐 Gamma","category": "FNO","url": "https://gammascan.streamlit.app/"},
    {"name": "🟢🔴 Market Depth","category": "FNO","url": "https://marketdepthgs.streamlit.app/"},
    {"name": "💹 Fundamental","category": "Screener","url": "https://fundamentalgs.streamlit.app/"},
    {"name": "❇️ Technical","category": "Screener","url": "https://technicalgs.streamlit.app/"},
    {"name": "✳️ Hybrid","category": "Screener","url": "https://techfunda.streamlit.app/"},
    {"name": "🌠 Kundali","category": "Astrology","url": "https://birthhcharts.streamlit.app/"},
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
        return requests.get(url, timeout=2).status_code == 200
    except:
        return False

# ================================
# DISPLAY TILED VIEW
# ================================
st.markdown('<div class="app-grid">', unsafe_allow_html=True)

for app in APPS:
    if search.lower() not in app["name"].lower():
        continue
    if category != "All" and app["category"] != category:
        continue

    status = "🟢" if is_live(app["url"]) else "🔴"

    st.markdown(f"""
    <div class="app-card">
        <div class="app-title">{app["name"]}</div>
        <div class="app-footer">
            <span>{status}</span>
            <a href="{app["url"]}" target="_blank">Open</a>
        </div>
    </div>
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
