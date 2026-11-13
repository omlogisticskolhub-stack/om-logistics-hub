import streamlit as st

st.set_page_config(
    page_title="Om Logistics - Control Tower Master Hub",
    page_icon="🚛",
    layout="wide",
)

# Custom Styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    .stApp {
        background-color: #f8fafc;
    }
    .main-header {
        background: linear-gradient(90deg, #b91c1c 0%, #dc2626 100%);
        padding: 25px 30px;
        border-radius: 12px;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 4px 12px rgba(220, 38, 38, 0.2);
    }
    .main-title {
        font-size: 28px;
        font-weight: 900;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .main-sub {
        font-size: 14px;
        opacity: 0.9;
        margin-top: 5px;
    }
    .card {
        background-color: white;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .card-icon {
        font-size: 36px;
        margin-bottom: 12px;
    }
    .card-title {
        font-size: 19px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
    }
    .card-desc {
        font-size: 13px;
        color: #475569;
        margin-bottom: 20px;
        line-height: 1.5;
    }
    .btn-link {
        display: block;
        text-align: center;
        background-color: #dc2626;
        color: white !important;
        text-decoration: none;
        padding: 10px 16px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 14px;
        transition: background 0.2s;
    }
    .btn-link:hover {
        background-color: #991b1b;
    }
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

# Header Banner
st.markdown(
    """
    <div class="main-header">
        <div class="main-title">🚛 OM LOGISTICS — CONTROL TOWER MASTER HUB</div>
        <div class="main-sub">Unified Operations, Warehouse & MIS Analytics Portal (East Zone)</div>
    </div>
""",
    unsafe_allow_html=True,
)

# 3 Dashboard Cards
col1, col2, col3 = st.columns(3)

# आपके तीनों ऐप्स के लिंक्स
WAREHOUSE_URL = "https://warehouse-app.streamlit.app"
AGING_URL = "https://sector3-aging-dashboard.streamlit.app"
BOOKING_MIS_URL = "https://daily-booking-mis-dashboard.streamlit.app"

with col1:
  st.markdown(
      f"""
        <div class="card">
            <div>
                <div class="card-icon">🏭</div>
                <div class="card-title">Warehouse Floor Operations</div>
                <div class="card-desc">
                    Track floor stock, loading/unloading status, short-scan logs, and hub operational KPIs in real time.
                </div>
            </div>
            <a href="{WAREHOUSE_URL}" target="_blank" class="btn-link">Open Warehouse App ↗</a>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col2:
  st.markdown(
      f"""
        <div class="card">
            <div>
                <div class="card-icon">⏳</div>
                <div class="card-title">Sector-3 Aging Dashboard</div>
                <div class="card-desc">
                    Monitor transit delays, 24/48/96-hour aging buckets, pending consignments, and hub bottlenecks.
                </div>
            </div>
            <a href="{AGING_URL}" target="_blank" class="btn-link">Open Aging Dashboard ↗</a>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col3:
  st.markdown(
      f"""
        <div class="card">
            <div>
                <div class="card-icon">📊</div>
                <div class="card-title">Daily Booking & Dispatch MIS</div>
                <div class="card-desc">
                    Analyze daily CN bookings, tonnage load, destination-wise performance, and TO_ZONE_NAME breakdowns.
                </div>
            </div>
            <a href="{BOOKING_MIS_URL}" target="_blank" class="btn-link">Open Booking MIS ↗</a>
        </div>
    """,
      unsafe_allow_html=True,
  )
