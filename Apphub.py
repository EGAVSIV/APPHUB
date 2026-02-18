import streamlit as st
import requests
import hashlib

# ================================
# PAGE CONFIG (ENHANCED)
# ================================
st.set_page_config(
    page_title="GS World • App Hub",
    page_icon="🪐",
    layout="wide"
)

# ================================
# GLOBAL CUSTOM CSS
# ================================
st.markdown(
    """
    <style>
    /* Main page background – subtle dark gradient */
    .stApp {
        background: radial-gradient(circle at top left, #101428 0, #050712 45%, #000000 100%);
        color: #f5f5f5;
        font-family: "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Hide Streamlit default menu & footer for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Centered neon header */
    .gs-header {
        text-align: center;
        padding: 0.4rem 0 0.2rem 0;
        background: linear-gradient(90deg, #ffdd00, #ff7a00, #ff00d4, #00e5ff, #00ff6a);
        -webkit-background-clip: text;
        color: transparent;
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        text-shadow: 0 0 18px rgba(255,255,255,0.25);
    }

    .gs-subtitle {
        text-align: center;
        font-size: 0.9rem;
        color: #c6d4ff;
        margin-top: -0.4rem;
        margin-bottom: 0.8rem;
    }

    /* Login card */
    .login-card {
        max-width: 420px;
        margin: 2.5rem auto 0 auto;
        padding: 1.6rem 1.4rem 1.2rem 1.4rem;
        border-radius: 18px;
        background: radial-gradient(circle at top left, #1f2937 0, #020617 60%);
        border: 1px solid rgba(148, 163, 184, 0.6);
        box-shadow:
            0 0 0 1px rgba(15,23,42,0.9),
            0 22px 55px rgba(0,0,0,0.85);
    }
    .login-title {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .login-sub {
        text-align: center;
        font-size: 0.85rem;
        color: #e5e7eb;
        margin-bottom: 1.1rem;
    }

    /* App card styling */
    .app-card {
        border-radius: 18px;
        padding: 0.9rem 0.8rem 0.8rem 0.8rem;
        margin-bottom: 0.8rem;
        background: linear-gradient(140deg, rgba(30,64,175,0.9), rgba(88,28,135,0.95));
        border: 1px solid rgba(129, 140, 248, 0.9);
        box-shadow:
            0 12px 24px rgba(15,23,42,0.85),
            0 0 0 1px rgba(15,23,42,0.9);
        transform: translateY(0px);
        transition:
            transform 0.18s ease-out,
            box-shadow 0.18s ease-out,
            border-color 0.18s ease-out,
            background 0.18s ease-out;
    }
    .app-card:hover {
        transform: translateY(-3px);
        box-shadow:
            0 16px 40px rgba(15,23,42,0.95),
            0 0 0 1px rgba(129,140,248,0.8);
        border-color: #fbbf24;
        background: linear-gradient(140deg, rgba(59,130,246,1), rgba(192,38,211,1));
    }

    .app-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: #f9fafb;
        margin-bottom: 0.1rem;
    }
    .app-category {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        color: #e0f2fe;
        text-transform: uppercase;
        opacity: 0.9;
        margin-bottom: 0.2rem;
    }
    .app-desc {
        font-size: 0.78rem;
        color: #e5e7eb;
        min-height: 2.2rem;
        margin-bottom: 0.4rem;
    }

    /* Status pill */
    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.1rem 0.6rem;
        border-radius: 999px;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
    }
    .status-live {
        background: rgba(22, 163, 74, 0.12);
        color: #bbf7d0;
        border: 1px solid rgba(34,197,94,0.7);
    }
    .status-down {
        background: rgba(220, 38, 38, 0.15);
        color: #fecaca;
        border: 1px solid rgba(248,113,113,0.85);
    }

    /* Make link button full-width inside card */
    .app-card button[kind="secondary"] {
        width: 100% !important;
        border-radius: 999px !important;
        border: none !important;
        padding-top: 0.35rem !important;
        padding-bottom: 0.35rem !important;
        font-weight: 700 !important;
        background: linear-gradient(90deg, #f97316, #facc15) !important;
        color: #111827 !important;
        box-shadow: 0 10px 18px rgba(15,23,42,0.75);
    }
    .app-card button[kind="secondary"]:hover {
        box-shadow: 0 12px 26px rgba(15,23,42,0.95);
        filter: brightness(1.06);
    }

    /* Search & filter strip */
    .filter-strip {
        background: rgba(15,23,42,0.95);
        border-radius: 16px;
        padding: 0.6rem 0.9rem 0.7rem 0.9rem;
        border: 1px solid rgba(148,163,184,0.65);
        box-shadow: 0 15px 35px rgba(15,23,42,0.95);
        margin-bottom: 0.8rem;
    }
    .filter-title {
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 0.15rem;
    }

    /* Footer */
    .gs-footer {
        text-align: center;
        font-size: 0.8rem;
        color: #9ca3af;
        margin-top: 1.5rem;
        padding-top: 0.7rem;
        border-top: 1px dashed rgba(148,163,184,0.6);
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
# LOGIN FUNCTION (UI IMPROVED)
# ================================
def check_login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    # Gradient GS World header
    st.markdown("<div class='gs-header'>GS WORLD • SECURED HUB</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='gs-subtitle'>🔐 Single Sign‑On • Quant Intelligence • Astro + Markets</div>",
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)

        st.markdown(
            "<div class='login-title'>🙏 Welcome, Trader</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<div class='login-sub'>Enter your <b>credentials</b> to unlock all analytics & scanners.</div>",
            unsafe_allow_html=True,
        )

        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")

        col_l, col_r = st.columns([1, 1.1])
        with col_l:
            login_btn = st.button("🚀 Unlock Dashboard", use_container_width=True)
        with col_r:
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
# APP REGISTRY (UNCHANGED DATA)
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
        "desc": "Back testing of FNO stocks with current scenarios.",
        "url": "https://fnobacktesting.streamlit.app/"
    },
    {
        "name": "🏦 NIFTY Sector Analysis",
        "category": "Screener",
        "desc": "Sector analysis with rotation.",
        "url": "https://sectoranalysis.streamlit.app/"
    },
    {
        "name": "📦 Company Announcement to NSE",
        "category": "Screener",
        "desc": "Orders, volume spike, management changes.",
        "url": "https://orderbooktrack.streamlit.app/"
    },
    {
        "name": "🫐 GAMMA_Blaster",
        "category": "FNO",
        "desc": "Gamma value scanner.",
        "url": "https://gammascan.streamlit.app/"
    },
    {
        "name": "🔆✴️ GAMMA_Blaster_2",
        "category": "FNO",
        "desc": "Advanced gamma scanner.",
        "url": "https://gammascan1.streamlit.app/"
    },
    {
        "name": "🟢🔴 Market Depth_Screener",
        "category": "FNO",
        "desc": "Order flow and market depth.",
        "url": "https://marketdepthgs.streamlit.app/"
    },
    {
        "name": "💹 TV_Fundmental Screener",
        "category": "Screener",
        "desc": "Fundamental screener.",
        "url": "https://fundamentalgs.streamlit.app/"
    },
    {
        "name": "❇️ TV_Technical Screener",
        "category": "Screener",
        "desc": "Technical screener.",
        "url": "https://technicalgs.streamlit.app/"
    },
    {
        "name": "✳️ TV_Hybrid Screener",
        "category": "Screener",
        "desc": "Hybrid tech + funda screener.",
        "url": "https://techfunda.streamlit.app/"
    },
    {
        "name": "🏤🏪 Mutual Fund & DII Activities",
        "category": "Screener",
        "desc": "MF, Insurance, DII activity.",
        "url": "https://mfhanalysis.streamlit.app/"
    },
    {
        "name": "🌠 Kundali",
        "category": "Astrology",
        "desc": "जन्म कुंडली",
        "url": "https://birthhcharts.streamlit.app/"
    }
]

# ================================
# SEARCH & FILTER (RESTYLED)
# ================================
with st.container():
    st.markdown("<div class='filter-strip'>", unsafe_allow_html=True)
    st.markdown(
        "<div class='filter-title'>APP DISCOVERY PANEL • SEARCH + FILTER</div>",
        unsafe_allow_html=True,
    )
    col_search, col_cat, col_info = st.columns([2.2, 1.4, 1.2])
    with col_search:
        search = st.text_input("🔍 Search by name or keyword", value="")
    with col_cat:
        category = st.selectbox(
            "🎯 Filter by category",
            ["All"] + sorted(set(a["category"] for a in APPS)),
        )
    with col_info:
        st.metric("Total Tools", len(APPS), help="Count of all apps currently available in GS World Hub.")
    st.markdown("</div>", unsafe_allow_html=True)


def is_live(url: str) -> bool:
    try:
        return requests.get(url, timeout=3).status_code == 200
    except Exception:
        return False

# ================================
# SORT ALPHABETICALLY BY NAME
# ================================
APPS = sorted(APPS, key=lambda x: x["name"].lower())

# ================================
# DISPLAY IN 8 COLUMNS WITH CARDS
# ================================
cols = st.columns(8)
col_index = 0

for app in APPS:
    if search.strip():
        if search.lower() not in app["name"].lower() and search.lower() not in app["desc"].lower():
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

        st.write("")  # small spacing
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
