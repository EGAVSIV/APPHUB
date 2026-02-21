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
# OPTIONAL BACKGROUND IMAGE
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
# GLOBAL CUSTOM CSS
# High‑contrast, legible dark theme
# ================================
st.markdown(
    """
    <style>
    /* Base app colors: dark grey surfaces, light text */
    .stApp {
        background: linear-gradient(135deg, #020617 0%, #0b1120 40%, #020617 100%);
        color: #e5e7eb;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* HEADERS */
    .gs-header {
        text-align: center;
        padding: 0.6rem 0 0.2rem 0;
        background: linear-gradient(90deg, #22c55e, #38bdf8, #6366f1);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        text-shadow: 0 0 14px rgba(15,23,42,0.9);
    }
    .gs-subtitle {
        text-align: center;
        font-size: 0.95rem;
        color: #cbd5f5;
        margin-top: -0.15rem;
        margin-bottom: 1.0rem;
    }

    /* LOGIN CARD */
    .login-card {
        max-width: 420px;
        margin: 2.2rem auto 0 auto;
        padding: 1.6rem 1.4rem 1.2rem 1.4rem;
        border-radius: 18px;
        background: #020617;
        border: 1px solid #1f2937;
        box-shadow: 0 22px 45px rgba(0,0,0,0.85);
    }
    .login-title {
        text-align: center;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #f9fafb;
    }
    .login-sub {
        text-align: center;
        font-size: 0.9rem;
        color: #9ca3af;
        margin-bottom: 1.1rem;
    }

    /* FILTER STRIP */
    .filter-strip {
        background: #020617;
        border-radius: 14px;
        padding: 0.6rem 0.9rem 0.7rem 0.9rem;
        border: 1px solid #1f2937;
        box-shadow: 0 16px 32px rgba(0,0,0,0.8);
        margin-bottom: 0.8rem;
    }
    .filter-title {
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #94a3b8;
        margin-bottom: 0.25rem;
    }

    /* CATEGORY CARD */
    .cat-card {
        border-radius: 16px;
        padding: 0.75rem 0.8rem 0.8rem 0.8rem;
        margin-top: 0.4rem;
        background: #020617;
        border: 1px solid #1f2937;
        text-align: center;
        cursor: pointer;
        box-shadow: 0 14px 30px rgba(0,0,0,0.85);
        transition: transform 0.12s ease-out,
                    box-shadow 0.12s ease-out,
                    border-color 0.12s ease-out,
                    background 0.12s ease-out;
    }
    .cat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 18px 36px rgba(0,0,0,0.95);
        border-color: #22c55e;
        background: radial-gradient(circle at top, #020617, #020617 40%, #0f172a 100%);
    }
    .cat-title {
        font-size: 1rem;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 0.1rem;
    }
    .cat-count {
        font-size: 0.8rem;
        color: #9ca3af;
    }

    /* APP CARD */
    .app-card {
        border-radius: 18px;
        padding: 0.9rem 0.9rem 0.85rem 0.9rem;
        margin-bottom: 0.9rem;
        background: #020617;
        border: 1px solid #1f2937;
        box-shadow: 0 16px 34px rgba(0,0,0,0.9);
        transition: transform 0.12s ease-out,
                    box-shadow 0.12s ease-out,
                    border-color 0.12s ease-out,
                    background 0.12s ease-out;
    }
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 40px rgba(0,0,0,1);
        border-color: #38bdf8;
        background: radial-gradient(circle at top, #020617, #020617 45%, #0b1120 100%);
    }

    .app-title {
        font-size: 0.98rem;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 0.18rem;
        white-space: normal;
    }
    .app-category {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        color: #38bdf8;
        text-transform: uppercase;
        margin-bottom: 0.25rem;
    }
    .app-desc {
        font-size: 0.8rem;
        color: #cbd5f5;
        min-height: 2.2rem;
        margin-bottom: 0.5rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.14rem 0.7rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .status-live {
        background: rgba(22,163,74,0.18);
        color: #bbf7d0;
        border: 1px solid #22c55e;
    }
    .status-down {
        background: rgba(220,38,38,0.18);
        color: #fecaca;
        border: 1px solid #f97373;
    }

    /* BUTTON INSIDE APP CARD */
    .app-card button[kind="secondary"] {
        width: 100% !important;
        border-radius: 999px !important;
        border: none !important;
        padding-top: 0.42rem !important;
        padding-bottom: 0.42rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #22c55e, #38bdf8) !important;
        color: #020617 !important;
        box-shadow: 0 12px 24px rgba(0,0,0,0.85);
    }
    .app-card button[kind="secondary"]:hover {
        filter: brightness(1.08);
        box-shadow: 0 16px 30px rgba(0,0,0,0.95);
    }

    /* FOOTER */
    .gs-footer {
        text-align: center;
        font-size: 0.82rem;
        color: #9ca3af;
        margin-top: 1.4rem;
        padding-top: 0.7rem;
        border-top: 1px dashed rgba(55,65,81,0.9);
        background: rgba(15,23,42,0.8);
    }
    .gs-footer strong {
        color: #e5e7eb;
    }
    .footer-highlight {
        color: #22c55e;
        font-weight: 600;
    }
    a.gs-mail {
        color: #38bdf8;
        text-decoration: none;
    }
    a.gs-mail:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ================================
# LOGIN
# ================================
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.markdown("<div class='gs-header'>GS WORLD • SECURED HUB</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='gs-subtitle'>🔐 Single Sign‑On • Quant Intelligence • Astro + Markets</div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<div class='login-title'>🙏 Welcome, Trader</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='login-sub'>Enter your <b>credentials</b> to unlock all analytics & scanners.</div>",
        unsafe_allow_html=True,
    )

    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    c1, c2 = st.columns([1, 1.1])
    with c1:
        login_btn = st.button("🚀 Unlock Dashboard", use_container_width=True)
    with c2:
        st.caption("Tip: Keep your access strictly confidential.")

    if login_btn:
        users = st.secrets["users"]
        hashed = hashlib.sha256(password.encode()).hexdigest()
        if username in users and users[username] == hashed:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials. Please try again.")

    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

check_login()

# ================================
# HEADER
# ================================
st.markdown("<div class='gs-header'>GS WORLD • APP HUB</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='gs-subtitle'>🧭 High‑contrast dashboard for Astrology • F&O • Sector • Weather tools</div>",
    unsafe_allow_html=True,
)

# ================================
# APP REGISTRY (your mapping)
# ================================
APPS = [
    # ASTROLOGY
    {"name": "Upcoming Aspectes and Past Aspects", "category": "ASTROLOGY",
     "desc": "Upcoming and past planetary aspects.", "url": "https://aspectfilter.streamlit.app"},
    {"name": "Live Planent postion", "category": "ASTROLOGY",
     "desc": "Live planetary positions.", "url": "https://liveplanetpostion.streamlit.app"},
    {"name": "Janam Kundali + Live Planets", "category": "ASTROLOGY",
     "desc": "Birth chart with live planet positions.", "url": "https://birthhcharts.streamlit.app"},

    # FINASTRO
    {"name": "Stocks Moving on Aspect Filter", "category": "FINASTRO",
     "desc": "Stocks reacting to planetary aspects.", "url": "https://stock-scanner-ascpect.streamlit.app"},
    {"name": "Daily Reveral Time of FNO Stocks", "category": "FINASTRO",
     "desc": "Astro based intraday reversal time for F&O.", "url": "https://fnoreversalpnt.streamlit.app"},
    {"name": "All Cycle Scan", "category": "FINASTRO",
     "desc": "Multiple astro cycles scan.", "url": "https://allcycles.streamlit.app"},
    {"name": "30‑60‑90 Cycles for FNO", "category": "FINASTRO",
     "desc": "Cycle scanner for F&O instruments.", "url": "https://fnopricecycle.streamlit.app"},
    {"name": "INTRADE Day REVERSAL (Nakshatra)", "category": "FINASTRO",
     "desc": "Intraday reversal based on Nakshatra.", "url": "https://intradayreversal.streamlit.app"},
    {"name": "Sun Cycle / Move Between Dates", "category": "FINASTRO",
     "desc": "Sun cycle scanner between two dates.", "url": "https://suncycle.streamlit.app"},

    # FUNDAMENTAL
    {"name": "Daily Order Receiving Status", "category": "FUNDAMENTAL",
     "desc": "Order book tracking screener.", "url": "https://orderbooktrack.streamlit.app"},
    {"name": "FII‑DII MH Activity", "category": "FUNDAMENTAL",
     "desc": "FII and DII money flow analysis.", "url": "https://fiidii.streamlit.app"},
    {"name": "Fundamental Metrics Screener", "category": "FUNDAMENTAL",
     "desc": "Market cap, PE, ROE, ROA, dividend, revenue.", "url": "https://fundamentalgs.streamlit.app"},
    {"name": "Mutual Fund Entry Exit 1", "category": "FUNDAMENTAL",
     "desc": "Mutual fund activity scanner 1.", "url": "https://mfhanalysis2.streamlit.app"},
    {"name": "Mutual Fund Entry Exit 2", "category": "FUNDAMENTAL",
     "desc": "Mutual fund activity scanner 2.", "url": "https://mfhanalysis.streamlit.app"},
    {"name": "SCREENER App Scan (Cookies)", "category": "FUNDAMENTAL",
     "desc": "Fundamental screener with cookies.", "url": "https://screenersapp.streamlit.app"},

    # GANN
    {"name": "GANN CYCLES for All STOCKS", "category": "GANN",
     "desc": "Gann time and price cycles.", "url": "https://ganncycle.streamlit.app"},
    {"name": "GANN Nifty Time Cycle", "category": "GANN",
     "desc": "Nifty time cycle analysis.", "url": "https://niftytimecycle.streamlit.app"},

    # TECHNICAL SCAN
    {"name": "ASSTTA PARAMERTER SCAN", "category": "TECHNICAL SCAN",
     "desc": "RaoSaab technical parameter scan.", "url": "https://raosaab.streamlit.app"},
    {"name": "DOW THEORY TREND Measure", "category": "TECHNICAL SCAN",
     "desc": "Trend measure using Dow Theory.", "url": "https://dowtheory.streamlit.app"},
    {"name": "FIB Retracement Levels Scan", "category": "TECHNICAL SCAN",
     "desc": "Fibonacci retracement scanner.", "url": "https://fibretracement.streamlit.app"},
    {"name": "ALL Technical Scan in One APP", "category": "TECHNICAL SCAN",
     "desc": "Multi‑scan technical screener.", "url": "https://multis.streamlit.app"},
    {"name": "MACD BASE Trend Detector", "category": "TECHNICAL SCAN",
     "desc": "Trend detection using MACD.", "url": "https://8003994518.streamlit.app"},
    {"name": "Technical With Fundamental Scans", "category": "TECHNICAL SCAN",
     "desc": "Hybrid technical + fundamental scans.", "url": "https://techfunda.streamlit.app"},
    {"name": "TOP Stock Finding (EMA/RSI/BB/ADX)", "category": "TECHNICAL SCAN",
     "desc": "Preset technical filters for stock picking.", "url": "https://technicalgs.streamlit.app"},

    # OPTION CHAIN + GREEKS
    {"name": "Gamma Blast Scan", "category": "OPTION CHAIN+GREEKS",
     "desc": "Gamma blaster scan.", "url": "https://gammascan.streamlit.app"},
    {"name": "Gamma Blast Scan 2", "category": "OPTION CHAIN+GREEKS",
     "desc": "Advanced gamma blaster scan.", "url": "https://gammascan1.streamlit.app"},
    {"name": "Live Market Depth", "category": "OPTION CHAIN+GREEKS",
     "desc": "Market depth and order book.", "url": "https://marketdepthgs.streamlit.app"},
    {"name": "Option Chain analysis 1", "category": "OPTION CHAIN+GREEKS",
     "desc": "Option chain scanner v1.", "url": "https://optionchainbygaurav.streamlit.app"},
    {"name": "Option Chain analysis 2", "category": "OPTION CHAIN+GREEKS",
     "desc": "Option chain scanner v2.", "url": "https://oiwithgaurav.streamlit.app"},
    {"name": "Option Chain analysis 3", "category": "OPTION CHAIN+GREEKS",
     "desc": "Option chain scanner v3.", "url": "https://oiwithgsy.streamlit.app"},
    {"name": "OI Decay – Sell Movement", "category": "OPTION CHAIN+GREEKS",
     "desc": "OI decay scanner.", "url": "https://oidecay.streamlit.app"},

    # SECTOR ANALYSIS
    {"name": "Sector Analysis With Comparison", "category": "SECTOR ANALYSIS",
     "desc": "Sector comparison dashboard.", "url": "https://secsea.streamlit.app"},
    {"name": "Sector Seasonal Impact Monitoring", "category": "SECTOR ANALYSIS",
     "desc": "Seasonality of sectors.", "url": "https://sectoranalysis.streamlit.app"},

    # COMMODITY / WEATHER
    {"name": "US Weather Forecast", "category": "COMMODITY",
     "desc": "Primary US weather forecast.", "url": "https://usaweather.streamlit.app"},
    {"name": "US Weather Forecast 1", "category": "COMMODITY",
     "desc": "US weather forecast alt‑1.", "url": "https://usaweather1.streamlit.app"},
    {"name": "US Weather Forecast 2", "category": "COMMODITY",
     "desc": "US weather forecast alt‑2.", "url": "https://usaweather2.streamlit.app"},
    {"name": "US Weather Forecast 3", "category": "COMMODITY",
     "desc": "US weather forecast alt‑3.", "url": "https://usaweather3.streamlit.app"},
    {"name": "US Weather Forecast 4", "category": "COMMODITY",
     "desc": "US weather forecast alt‑4.", "url": "https://usaweather4.streamlit.app"},

    # OTHERS
    {"name": "ALGO Trading Suite", "category": "Others",
     "desc": "GS Algo trading utilities.", "url": "https://gsalgo.streamlit.app"},
    {"name": "NEOTRADER / GeoTrader", "category": "Others",
     "desc": "GeoTrader based utilities.", "url": "https://geotrader.streamlit.app"},
    {"name": "LTP Monitoring", "category": "Others",
     "desc": "Last traded price monitoring.", "url": "https://lasttradedprice.streamlit.app"},
    {"name": "NEWS at One Place", "category": "Others",
     "desc": "Market and global news hub.", "url": "https://allnews.streamlit.app"},
    {"name": "NEWS at One Place (API)", "category": "Others",
     "desc": "Indian news with API.", "url": "https://oneindianews.streamlit.app"},
    {"name": "FNO Best Run Condition Detection", "category": "Others",
     "desc": "Back‑testing for best FNO runs.", "url": "https://fnobacktesting.streamlit.app"},
    {"name": "Trading Journals", "category": "Others",
     "desc": "Trading journal manager.", "url": "https://tradingjournalgs.streamlit.app"},
]

# ================================
# HELPERS
# ================================
def is_live(url: str) -> bool:
    try:
        return requests.get(url, timeout=3).status_code == 200
    except Exception:
        return False

all_categories = sorted({a["category"] for a in APPS})

if "selected_category" not in st.session_state:
    st.session_state.selected_category = None

# ================================
# CATEGORY HOME VIEW
# ================================
if st.session_state.selected_category is None:
    st.markdown(
        "<div class='gs-subtitle'>Select a category card to view all tools inside it.</div>",
        unsafe_allow_html=True,
    )

    cols = st.columns(4)
    idx = 0
    for cat in all_categories:
        cat_apps = [a for a in APPS if a["category"] == cat]
        with cols[idx]:
            if st.button(cat, key=f"cat_btn_{cat}"):
                st.session_state.selected_category = cat
                st.experimental_rerun()
            st.markdown(
                f"<div class='cat-card'>"
                f"<div class='cat-title'>{cat}</div>"
                f"<div class='cat-count'>{len(cat_apps)} tools</div>"
                f"</div>",
                unsafe_allow_html=True,
            )
        idx += 1
        if idx == 4:
            cols = st.columns(4)
            idx = 0

# ================================
# CATEGORY DETAIL VIEW
# ================================
else:
    cat = st.session_state.selected_category
    st.markdown(
        f"<div class='gs-subtitle'>Category: <b>{cat}</b></div>",
        unsafe_allow_html=True,
    )

    if st.button("⬅️ Back to Categories"):
        st.session_state.selected_category = None
        st.experimental_rerun()

    cat_apps = sorted(
        [a for a in APPS if a["category"] == cat],
        key=lambda x: x["name"].lower()
    )

    cols = st.columns(4)
    col_index = 0

    for app in cat_apps:
        with cols[col_index]:
            st.markdown("<div class='app-card'>", unsafe_allow_html=True)
            st.markdown(f"<div class='app-title'>{app['name']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='app-category'>{app['category']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='app-desc'>{app['desc']}</div>", unsafe_allow_html=True)

            live = is_live(app["url"])
            if live:
                st.markdown(
                    "<span class='status-pill status-live'>🟢 LIVE</span>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    "<span class='status-pill status-down'>🔴 DOWN</span>",
                    unsafe_allow_html=True,
                )

            st.write("")
            st.link_button("🚀 Launch App", app["url"])
            st.markdown("</div>", unsafe_allow_html=True)

        col_index += 1
        if col_index == 4:
            cols = st.columns(4)
            col_index = 0

# ================================
# FOOTER
# ================================
st.markdown(
    """
    <div class="gs-footer">
        <strong>Designed by:</strong>  <span class="footer-highlight">Gaurav Singh Yadav</span><br/>
        Built with ❤️ • Energy • Commodity • Quant Intelligence<br/>
        📱 +91-8003994518<br/>
        📧 <a class="gs-mail" href="mailto:yadav.gauravsingh@gmail.com">yadav.gauravsingh@gmail.com</a>
    </div>
    """,
    unsafe_allow_html=True,
)
