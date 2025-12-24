import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

# Full-screen app mode
st.set_page_config(page_title="Mein Ticket", layout="centered")

# Custom CSS for sticky top bar, white background, black text, tighter spacing, and bottom date style
st.markdown("""
    <style>
    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Sticky top bar */
    .sticky-top {
        position: sticky;
        top: 0;
        z-index: 100;
        width: 100%;
    }
    
    /* White background, black text, tighter line spacing */
    .main-content {
        background-color: white;
        color: black;
        padding: 20px;
        line-height: 1.4;  /* Reduced from default ~1.6 */
        font-size: 16px;
    }
    .main-content h1 {
        font-size: 28px;
        margin: 10px 0 5px 0;
    }
    .main-content p, .main-content div {
        margin: 8px 0;  /* Tighter spacing between lines */
    }
    </style>
""", unsafe_allow_html=True)

# Load images
top_bar = Image.open("top_bar.jpeg")          # ← Use your exact top bar filename (.jpg or .jpeg)
qr_code = Image.open("qr_code.jpeg")          # ← Your QR filename
bottom_bg = Image.open("bottom_background.jpeg")  # ← Your bottom filename

# Dynamic dates (today is 24.12.2025)
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month = now.strftime("%d.%m.")

# 1. Sticky top bar
st.image(top_bar, use_column_width=True, caption=None)
st.markdown('<div class="sticky-top"></div>', unsafe_allow_html=True)  # Keeps it fixed on scroll

# 2. QR code
st.image(qr_code, use_column_width=True)

# 3. Main content (white bg, black text, tight spacing)
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("<h1>Jamil Aasi</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 18px; font-weight: bold; margin-bottom: 20px;'>CIV 1080</p>", unsafe_allow_html=True)  # Black, not red

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
st.write("Zubringung: Gilt nur für eingetragene Züge. Dieser ist bei der Kontrolle vorzulegen. Nur gültig mit amtlichem Lichtbildausweis...")  # Keep your full text here

st.markdown('</div>', unsafe_allow_html=True)  # End main content

# 4. Bottom background with ONLY the date overlaid (dark gray text + light gray stroke)
st.image(bottom_bg, use_column_width=True)

st.markdown(f"""
    <div style="position: relative; margin-top: -100px; text-align: center; pointer-events: none;">
        <div style="
            font-size: 48px; 
            font-weight: 900; 
            color: #333333;          /* Dark gray */
            -webkit-text-stroke: 2px #aaaaaa;  /* Light gray stroke */
            text-stroke: 2px #aaaaaa;
            text-shadow: 2px 2px 4px #cccccc;
        ">
            {day_month}.
        </div>
    </div>
""", unsafe_allow_html=True)

# Adjust margin-top above if the date position isn't perfect (-100px works for most — change to -80px or -120px if needed)

# Footer
st.markdown("<p style='text-align: center; color: gray; font-size: 14px; margin-top: 40px;'>Stornierung Ausgeschlossen<br>Ticketcode: BNAZcb...</p>", unsafe_allow_html=True)

