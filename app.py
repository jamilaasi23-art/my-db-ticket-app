import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

# Page config
st.set_page_config(page_title="Mein Ticket", layout="centered")

# Strong CSS for TRUE fixed top bar + clean styling
st.markdown("""
    <style>
    /* Hide Streamlit defaults */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Remove padding/margin */
    .stApp {padding-top: 0 !important; margin-top: 0 !important;}
    .block-container {padding-top: 0 !important;}
    
    /* TRUE fixed top bar - always stays at the very top */
    .fixed-top-bar {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        z-index: 9999 !important;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Content starts below the fixed top bar */
    .main-content {
        margin-top: 110px;   /* Adjust this if your top bar is taller/shorter (try 90px–130px) */
        background-color: white;
        color: black;
        padding: 20px;
        line-height: 1.4;    /* Tighter line spacing */
        font-size: 16px;
    }
    .main-content h1 {
        font-size: 28px;
        margin: 10px 0 5px 0;
        color: black;
    }
    .main-content p, .main-content div {
        margin: 6px 0;       /* Even tighter spacing between lines */
    }
    </style>
""", unsafe_allow_html=True)

# Load your images - make sure filenames match EXACTLY what you uploaded
top_bar = Image.open("top_bar.jpeg")          # ← change if different (e.g. top_bar.jpg)
qr_code = Image.open("qr_code.jpeg")          # ← change if different
bottom_bg = Image.open("bottom_background.jpeg")  # ← change if different

# Dynamic dates (today = December 24, 2025)
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month = now.strftime("%d.%m.")

# === DISPLAY ===

# 1. FIXED TOP BAR (always visible)
st.markdown(
    f'<div class="fixed-top-bar"><img src="{top_bar.getbuffer().tobytes()}" style="width:100%; height:auto; display:block;"></div>',
    unsafe_allow_html=True
)

# 2. QR code (below the fixed bar)
st.image(qr_code, use_column_width=True)

# 3. Main text content (white bg, black text, tight spacing)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("<h1>Jamil Aasi</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 18px; font-weight: bold; margin-bottom: 20px; color: black;'>CIV 1080</p>", unsafe_allow_html=True)

st.markdown("**Gültigkeit**")
st.write("ICE/ Fahrkarte (Einfache Fahrt)")
st.write("Super Sparpreis")
st.write("2. Klasse")
st.write("1 Person (27-64 Jahre)")
st.write(f"Von: {today}, 00:00 Uhr")
st.write(f"Bis: {tomorrow}, 10:00 Uhr")

st.markdown("**Verbindung**")
st.write("Eisenach Hbf - Dortmund Hbf")
st.write("Zubringung:")
st.write(f"IC 2156, **{future_time} Uhr am {today}**")
st.write("Von: * (RB/ALT*PB*HAM)")
st.write("")
st.write("Buchungsdetails")
st.write("")
st.write(f"**Gebucht am: {today} um 04:35 Uhr**")
st.write("Auftrags-Nr: 225073878296")
st.write("Gesamtpreis: 45,99 €")

st.markdown("**Kontingente**")
st.write("Zubringung: Gilt nur für eingetragene Züge. Dieser ist bei der Kontrolle vorzulegen. Nur gültig mit amtlichem Lichtbildausweis. Mehrfachfahrt nicht möglich... (add full text if you want)")

st.markdown('</div>', unsafe_allow_html=True)  # End main content

# 4. Bottom background with ONLY the date (dark gray + light gray stroke)
st.image(bottom_bg, use_column_width=True)

st.markdown(f"""
    <div style="position: relative; margin-top: -100px; text-align: center; pointer-events: none;">
        <div style="
            font-size: 48px;
            font-weight: 900;
            color: #333333;                  /* Dark gray */
            -webkit-text-stroke: 3px #bbbbbb; /* Light gray outline */
            text-stroke: 3px #bbbbbb;
            paint-order: stroke fill;
        ">
            {day_month}.
        </div>
    </div>
""", unsafe_allow_html=True)

# Optional footer
st.markdown("<p style='text-align: center; color: gray; font-size: 14px; margin-top: 40px;'>Stornierung Ausgeschlossen<br>Ticketcode: BNAZcb...</p>", unsafe_allow_html=True)
