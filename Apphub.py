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
def set_bg_image(image_path: str):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
                radial-gradient(circle at top left, #050816 0, #020617 45%, #000000 100%),
                url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# =====================================================
# APPLY BACKGROUND
# =====================================================

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

bg_path = os.path.join(BASE_PATH, "Assets", "BG11.png")

if os.path.exists(bg_path):
    set_bg_image(bg_path)
else:
    st.warning(f"Background not found at: {bg_path}")

# ================================
# GLOBAL CUSTOM CSS (CONTRAST TUNED)
# ================================
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #050816 0, #020617 45%, #000000 100%);
        color: #f9fafb;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    .gs-header {
        text-align: center;
        padding: 0.4rem 0 0.15rem 0;
        background: linear-gradient(90deg, #fde047, #fb923c, #f97316, #a855f7, #38bdf8);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 2.4rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        text-shadow: 0 0 18px rgba(255,255,255,0.25);
    }
    .gs-subtitle {
        text-align: center;
        font-size: 0.9rem;
        color: #e5e7eb;
        margin-top: -0.3rem;
        margin-bottom: 0.8rem;
    }

    .login-card {
        max-width: 420px;
        margin: 2.5rem auto 0 auto;
        padding: 1.6rem 1.4rem 1.2rem 1.4rem;
        border-radius: 18px;
        background: radial-gradient(circle at top left, #111827 0, #020617 60%);
        border: 1px solid rgba(148, 163, 184, 0.85);
        box-shadow:
            0 0 0 1px rgba(15,23,42,0.95),
            0 22px 55px rgba(0,0,0,0.9);
    }
    .login-title {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
        color: #f9fafb;
    }
    .login-sub {
        text-align: center;
        font-size: 0.85rem;
        color: #e5e7eb;
        margin-bottom: 1.1rem;
    }

    .filter-strip {
        background: rgba(15,23,42,0.98);
        border-radius: 16px;
        padding: 0.7rem 0.9rem 0.8rem 0.9rem;
        border: 1px solid rgba(148,163,184,0.85);
        box-shadow: 0 15px 35px rgba(15,23,42,0.95);
        margin-bottom: 0.8rem;
    }
    .filter-title {
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.25rem;
    }

    .app-card {
        border-radius: 18px;
        padding: 0.9rem 0.8rem 0.85rem 0.8rem;
        margin-bottom: 0.9rem;
        background: linear-gradient(140deg, #111827, #020617);
        border: 1px solid rgba(55,65,81,0.95);
        box-shadow:
            0 10px 20px rgba(0,0,0,0.9),
            0 0 0 1px rgba(15,23,42,0.95);
        transform: translateY(0px);
        transition:
            transform 0.16s ease-out,
            box-shadow 0.16s ease-out,
            border-color 0.16s ease-out,
            background 0.16s ease-out;
    }
    .app-card:hover {
        transform: translateY(-2px);
        box-shadow:
            0 16px 34px rgba(0,0,0,0.95),
            0 0 0 1px rgba(129,140,248,0.9);
        border-color: #facc15;
        background: radial-gradient(circle at top left, #1e293b, #020617);
    }

    .app-title {
        font-size: 0.96rem;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 0.15rem;
        white-space: normal;
    }
    .app-category {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        color: #a5b4fc;
        text-transform: uppercase;
        opacity: 0.96;
        margin-bottom: 0.2rem;
    }
    .app-desc {
        font-size: 0.78rem;
        color: #e5e7eb;
        min-height: 2.2rem;
        margin-bottom: 0.45rem;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.12rem 0.7rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
    }
    .status-live {
        background: rgba(22,163,74,0.18);
        color: #bbf7d0;
        border: 1px solid rgba(34,197,94,0.9);
    }
    .status-down {
        background: rgba(220,38,38,0.22);
        color: #fecaca;
        border: 1px solid rgba(248,113,113,0.95);
    }

    .app-card button[kind="secondary"] {
        width: 100% !important;
        border-radius: 999px !important;
        border: none !important;
        padding-top: 0.38rem !important;
        padding-bottom: 0.38rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #fb923c, #fde047) !important;
        color: #111827 !important;
        box-shadow: 0 10px 18px rgba(0,0,0,0.85);
    }
    .app-card button[kind="secondary"]:hover {
        box-shadow: 0 12px 24px rgba(0,0,0,0.95);
        filter: brightness(1.06);
    }

    .gs-footer {
        text-align: center;
        font-size: 0.8rem;
        color: #9ca3af;
        margin-top: 1.4rem;
        padding-top: 0.7rem;
        border-top: 1px dashed rgba(148,163,184,0.7);
    }
    .gs-footer strong {
        color: #e5e7eb;
    }
    .footer-highlight {
        color: #fbbf24;
        font-weight: 600;
    }
    a.gs-mail {
        color: #60a5fa;
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
# LOGIN FUNCTION
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
# TOP HEADER
# ================================
st.markdown("<div class='gs-header'>GS WORLD • APP HUB</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='gs-subtitle'>🧭 Astrology • F&O • Index • Weather • Quant Research — All in One Place</div>",
    unsafe_allow_html=True,
)
st.write("")

# ================================
# APP REGISTRY
# ================================
APPS = [
    {"name": "🪐-☀️ Planetary Aspect Scanner", "category": "Astrology+Equity",
     "desc": "Filter planetary aspects between two dates using sidereal calculations.",
     "url": "https://aspectfilter.streamlit.app/"},
    {"name": "🪐-📉 Stocks Movement on Aspects", "category": "Astrology+Equity",
     "desc": "Astrological aspect-based stock market analysis.",
     "url": "https://stock-scanner-ascpect.streamlit.app/"},
    {"name": "🔁 F&O Reversal Price & Time ", "category": "FNO & Astro",
     "desc": "Identify high-probability reversal points in F&O stocks.",
     "url": "https://fnoreversalpnt.streamlit.app/"},
    {"name": "🌍-🪐-☀️ Live Planet Position", "category": "Astrology",
     "desc": "Real-time planetary positions with sidereal reference.",
     "url": "https://liveplanetpostion.streamlit.app/"},
    {"name": "🤵‍♂️ RaoSaab Research Desk", "category": "Screener",
     "desc": "Stock Filtration As per AS",
     "url": "https://raosaab.streamlit.app/"},
    {"name": "💰 FII–DII Activity Tracker", "category": "Market Data",
     "desc": "Track daily, weekly and monthly FII–DII activity.",
     "url": "https://fiidii.streamlit.app/"},
    {"name": "🔄 F&O Price Cycle", "category": "FNO",
     "desc": "Price cycle based on Weekly Close 3-69 in F&O instruments.",
     "url": "https://fnopricecycle.streamlit.app/"},
    {"name": "📐 Gann Cycle Analyzer", "category": "GANN",
     "desc": "Gann-based time and price cycle analysis.",
     "url": "https://ganncycle.streamlit.app/"},
    {"name": "⏱️ NIFTY Time Cycle", "category": "Index",
     "desc": "Time-cycle based forecasting for NIFTY.",
     "url": "https://niftytimecycle.streamlit.app/"},
    {"name": "⚡ Intraday Reversal Scanner", "category": "FNO & Astro",
     "desc": "Detect intraday reversal setups with precision.",
     "url": "https://intradayreversal.streamlit.app/"},
    {"name": "📰 Market News Aggregator", "category": "News",
     "desc": "All important market and global news at one place.",
     "url": "https://allnews.streamlit.app/"},
    {"name": "📊 Multi-Timeframe Stock Screener", "category": "Screener",
     "desc": "Multiple Scan Stock Selection",
     "url": "https://multis.streamlit.app/"},
    {"name": "1️⃣ 📉 OI Decay Scanner", "category": "FNO",
     "desc": "Option OI decay and expiry-based behavior analysis.",
     "url": "https://oidecay.streamlit.app/"},
    {"name": "2️⃣📉 Option Chain by Gaurav", "category": "FNO",
     "desc": "Option chain analysis with OI, strikes, and market structure.",
     "url": "https://optionchainbygaurav.streamlit.app/"},
    {"name": "3️⃣📚 OI Analytics (GSY)", "category": "FNO",
     "desc": "Advanced Open Interest analysis and insights.",
     "url": "https://oiwithgsy.streamlit.app/"},
    {"name": "☀️ Sun Cycle Analyzer", "category": "Astrology+Equity",
     "desc": "Solar cycle based timing and trend insights.",
     "url": "https://suncycle.streamlit.app/"},
    {"name": "🌎 USA Weather & Energy Impact", "category": "Weather + Commodities",
     "desc": "US weather analysis with energy and commodity impact.",
     "url": "https://usaweather.streamlit.app/"},
    {"name": "1️⃣ USA Weather (Alt-1)", "category": "Weather + Commodities",
     "desc": "Alternative US weather forecast dashboard.",
     "url": "https://usaweather1.streamlit.app/"},
    {"name": "2️⃣ USA Weather (Alt-2)", "category": "Weather + Commodities",
     "desc": "Secondary US weather and temperature analysis.",
     "url": "https://usaweather2.streamlit.app/"},
    {"name": "3️⃣ USA Weather (Alt-3)", "category": "Weather + Commodities",
     "desc": "Alternative US weather forecast dashboard.",
     "url": "https://usaweather3.streamlit.app/"},
    {"name": "4️⃣ USA Weather (Alt-4)", "category": "Weather + Commodities",
     "desc": "Alternative US weather forecast dashboard.",
     "url": "https://usaweather4.streamlit.app/"},
    {"name": "🔺🔻 Back Testing FNO", "category": "Screener",
     "desc": "Back testing of FNO stocks with current scenarios.",
     "url": "https://fnobacktesting.streamlit.app/"},
    {"name": "🏦 NIFTY Sector Analysis", "category": "Screener",
     "desc": "Sector analysis with rotation.",
     "url": "https://sectoranalysis.streamlit.app/"},
    {"name": "📦 Company Announcement to NSE", "category": "Screener",
     "desc": "Orders, volume spike, management changes.",
     "url": "https://orderbooktrack.streamlit.app/"},
    {"name": "🫐 GAMMA_Blaster", "category": "FNO",
     "desc": "Gamma value scanner.",
     "url": "https://gammascan.streamlit.app/"},
    {"name": "🔆✴️ GAMMA_Blaster_2", "category": "FNO",
     "desc": "Advanced gamma scanner.",
     "url": "https://gammascan1.streamlit.app/"},
    {"name": "🟢🔴 Market Depth_Screener", "category": "FNO",
     "desc": "Order flow and market depth.",
     "url": "https://marketdepthgs.streamlit.app/"},
    {"name": "💹 TV_Fundmental Screener", "category": "Screener",
     "desc": "Fundamental screener.",
     "url": "https://fundamentalgs.streamlit.app/"},
    {"name": "❇️ TV_Technical Screener", "category": "Screener",
     "desc": "Technical screener.",
     "url": "https://technicalgs.streamlit.app/"},
    {"name": "✳️ TV_Hybrid Screener", "category": "Screener",
     "desc": "Hybrid tech + funda screener.",
     "url": "https://techfunda.streamlit.app/"},
    {"name": "🏤🏪 Mutual Fund & DII Activities", "category": "Screener",
     "desc": "MF, Insurance, DII activity.",
     "url": "https://mfhanalysis.streamlit.app/"},
    {"name": "🌠 Kundali", "category": "Astrology",
     "desc": "जन्म कुंडली",
     "url": "https://birthhcharts.streamlit.app/"},
]

# ================================
# ADDITIONAL APPS (SKIP IF DUPLICATE URL)
# ================================
extra_urls = [
    "https://gsalgo.streamlit.app/",
    "https://geotrader.streamlit.app/",
    "https://gammascan.streamlit.app/",
    "https://gammascan1.streamlit.app/",
    "https://marketdepthgs.streamlit.app/",
    "https://screenersapp-bgybondappuwidk3q7ttb38.streamlit.app/",
    "https://fnobacktesting.streamlit.app/",
]

existing_urls = {a["url"] for a in APPS}

extra_defs = {
    "https://gsalgo.streamlit.app/": {
        "name": "🧠 GS Algo Suite",
        "category": "FNO",
        "desc": "Algorithmic trading utilities and scanners.",
    },
    "https://geotrader.streamlit.app/": {
        "name": "🌐 GeoTrader",
        "category": "Astrology+Equity",
        "desc": "Geographical and astro based market studies.",
    },
    "https://screenersapp-bgybondappuwidk3q7ttb38.streamlit.app/": {
        "name": "📦 Master Screener Hub",
        "category": "Screener",
        "desc": "Collection of multiple GS screeners in one place.",
    },
}

for url in extra_urls:
    if url in existing_urls:
        continue
    meta = extra_defs.get(url, {
        "name": f"🔗 Tool @ {url.replace('https://', '').replace('.streamlit.app/','')}",
        "category": "Misc",
        "desc": "Additional GS World utility.",
    })
    APPS.append({
        "name": meta["name"],
        "category": meta["category"],
        "desc": meta["desc"],
        "url": url,
    })

# ================================
# SEARCH & FILTER
# ================================
with st.container():
    st.markdown("<div class='filter-strip'>", unsafe_allow_html=True)
    st.markdown(
        "<div class='filter-title'>APP DISCOVERY PANEL • SEARCH + FILTER</div>",
        unsafe_allow_html=True,
    )
    c_search, c_cat, c_info = st.columns([2.2, 1.4, 1.0])
    with c_search:
        search = st.text_input("🔍 Search by name or keyword", value="")
    with c_cat:
        category = st.selectbox(
            "🎯 Filter by category",
            ["All"] + sorted(set(a["category"] for a in APPS)),
        )
    with c_info:
        st.metric("Total Tools", len(APPS))
    st.markdown("</div>", unsafe_allow_html=True)


def is_live(url: str) -> bool:
    try:
        return requests.get(url, timeout=3).status_code == 200
    except Exception:
        return False

# ================================
# SORT & DISPLAY
# ================================
APPS = sorted(APPS, key=lambda x: x["name"].lower())

cols = st.columns(8)
col_index = 0

for app in APPS:
    text = search.strip().lower()
    if text:
        if text not in app["name"].lower() and text not in app["desc"].lower():
            continue
    if category != "All" and app["category"] != category:
        continue

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
    if col_index == 8:
        cols = st.columns(8)
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
