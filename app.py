import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import base64
from io import BytesIO

# Page config
st.set_page_config(page_title="Mein Ticket", layout="centered")

# CSS for truly fixed top bar + styling
st.markdown("""
    <style>
    /* Hide Streamlit defaults */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Remove padding */
    .stApp {padding-top: 0 !important; margin-top: 0 !important;}
    .block-container {padding-top: 0 !important;}
    
    /* Fixed top bar */
    .fixed-top-bar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        width: 100%;
        z-index: 9999;
        background-color: white;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    /* Content starts below fixed bar */
    .main-content {
        margin-top: 110px;   /* Change this if needed (90-130px) */
        background-color: white;
        color: black;
        padding: 20px;
        line-height: 1.4;
        font-size: 16px;
    }
    .main-content h1 {
        font-size: 28px;
        margin: 10px 0 5px 0;
    }
    .main-content p, .main-content div {
        margin: 6px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load images - make sure filenames match exactly what you uploaded
top_bar = Image.open("top_bar.jpeg")          # ← change if different
qr_code = Image.open("qr_code.jpeg")          # ← change if different
bottom_bg = Image.open("bottom_background.jpeg")  # ← change if different

# Convert top_bar to base64 for embedding in HTML
buffered = BytesIO()
top_bar.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Dynamic dates
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month = now.strftime("%d.%m.")

# === DISPLAY ===

# 1. FIXED TOP BAR (always visible)
st.markdown(
    f'<div class="fixed-top-bar"><img src="data:image/jpeg;base64,{img_str}" style="width:100%; height:auto; display:block;"></div>',
    unsafe_allow_html=True
)

# 2. QR code
st.image(qr_code, use_column_width=True)

# 3. Main content
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
st.write("Zubringung: Gilt nur für eingetragene Züge. Dieser ist bei der Kontrolle vorzulegen. Nur gültig mit amtlichem Lichtbildausweis...")

st.markdown('</div>', unsafe_allow_html=True)

# 4. Bottom background + only the date
st.image(bottom_bg, use_column_width=True)

st.markdown(f"""
    <div style="position: relative; margin-top: -100px; text-align: center; pointer-events: none;">
        <div style="
            font-size: 48px;
            font-weight: 900;
            color: #333333;
            -webkit-text-stroke: 3px #bbbbbb;
            text-stroke: 3px #bbbbbb;
            paint-order: stroke fill;
        ">
            {day_month}.
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: gray; font-size: 14px; margin-top: 40px;'>Stornierung Ausgeschlossen<br>Ticketcode: BNAZcb...</p>", unsafe_allow_html=True)
