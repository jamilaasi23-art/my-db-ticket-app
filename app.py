import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import base64
from io import BytesIO

# Page config
st.set_page_config(page_title="Mein Ticket", layout="centered")

# CSS for fixed top bar + uniform text styling
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {padding-top: 0 !important; margin-top: 0 !important;}
    .block-container {padding-top: 0 !important;}
    
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
    
    .main-content {
        margin-top: 110px;   /* Adjust if top bar height changes */
        background-color: white;
        color: black;
        padding: 20px;
        line-height: 1.4;
        font-size: 16px;     /* All text same size */
    }
    .main-content p, .main-content div {
        margin: 6px 0;
    }
    .section-header {
        font-weight: bold;
        font-size: 16px;
        margin: 20px 0 8px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Load images - make sure filenames match exactly
top_bar = Image.open("top_bar.jpeg")
qr_code = Image.open("qr_code.jpeg")
bottom_bg = Image.open("bottom_background.jpeg")

# Convert top_bar to base64 for HTML embed
buffered = BytesIO()
top_bar.save(buffered, format="JPEG")
img_str = base64.b64encode(buffered.getvalue()).decode()

# Dynamic dates
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month_no_dots = now.strftime("%d %m")  # 24 12 format, no dots

# Fixed top bar
st.markdown(
    f'<div class="fixed-top-bar"><img src="data:image/jpeg;base64,{img_str}" style="width:100%; height:auto; display:block;"></div>',
    unsafe_allow_html=True
)

# QR code
st.image(qr_code, use_column_width=True)

# Main content - all text same size, only headers bold
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.write("Jamil Aasi")  # Normal size, not bold

st.markdown("<p class='section-header'>CIV 1080</p>", unsafe_allow_html=True)

st.markdown("<p class='section-header'>Gültigkeit</p>", unsafe_allow_html=True)
st.write("IC/EC Fahrkarte (Einfache Fahrt)")
st.write("Super Sparpreis")
st.write("2. Klasse")
st.write("1 Person (27-64 Jahre)")
st.write(f"Von: {today}, 00:00 Uhr")
st.write(f"Bis: {tomorrow}, 10:00 Uhr")

st.markdown("<p class='section-header'>Verbindung</p>", unsafe_allow_html=True)
st.write("Eisenach Hbf - Dortmund Hbf")
st.write("Zugbindung:")
st.write(f"IC 2156, {future_time} Uhr am {today}")
st.write("Via: <1080>(HERS/BEB)KS*WAR(BRI/ALT*PB*HAM)")

st.markdown("<p class='section-header'>Buchungsdetails</p>", unsafe_allow_html=True)
st.write("Gebucht am: 19.12.2025 um 19:51 Uhr")
st.write("Auftrags-Nr: 225073878296")
st.write("Gesamtpreis: 45,99 €")

st.markdown("<p class='section-header'>Konditionen</p>", unsafe_allow_html=True)
st.write("Zugbindung: Gilt nur für eingetragene Züge.")
st.write("Nur gültig mit amtlichem Lichtbildausweis. Dieser ist bei der Kontrolle vorzuzeigen.")
st.write("Bei Fahrkarten mit BahnCard-Rabatt zeigen Sie bitte zusätzlich Ihre gültige BahnCard vor.")
st.write("Es gelten die nationalen und internationalen Beförderungsbedingungen der DB AG. Innerhalb von Verkehrsverbünden und Tarifgemeinschaften gelten deren Bestimmungen. Alle Bedingungen finden Sie unter www.bahn.de/agb und www.diebefoerderer.de.")
st.write("Eine Fahrkarte entspricht grundsätzlich einem Beförderungsvertrag, mehrere Fahrkarten mehreren Beförderungsverträgen. Vertraglicher Beförderer können dabei ein oder mehrere Verkehrsunternehmen sein. Für die Eisenbahnfahrt handelt es sich bei dieser Fahrkarte um eine Durchgangsfahrkarte gemäß der Fahrgastrechte-Verordnung (EU) 2021/782 für den Eisenbahnverkehr. Für eine Fahrkarte, die neben der Eisenbahnfahrt noch die Fahrt mit einem anderen Verkehrsträger umfasst (z.B. Schiff zu den Nordseeinseln; ÖPNV) gilt: Die Fahrkarte dokumentiert dann je einen gesonderten Beförderungsvertrag pro Richtung und pro Verkehrsträger. Die Haftung für fahrgastrechtliche Ansprüche gilt dann auch nur für den jeweiligen Beförderungsvertrag.")
st.write("Bei einer zu erwartenden Verspätung ab 20 Minuten am Zielbahnhof Ihrer Fahrkarte ist die Zugbindung Ihrer Fahrt ohne besondere Bescheinigung aufgehoben.")
st.write("Kleinkindabteile, Rollstuhlstellplätze und Vorrangplätze für Personen mit eingeschränkter Mobilität sowie Plätze für Reisende mit BahnBonus Gold- oder Platinstatus sind bei Bedarf für diese Personengruppen freizugeben.")

st.write("Stornierung ausgeschlossen")
st.write("Ticketcode: BNAZCDJ0")

st.markdown('</div>', unsafe_allow_html=True)

# Bottom background
st.image(bottom_bg, use_column_width=True)

# Date on bottom: 24 12, no dots, higher and shifted left
st.markdown(f"""
    <div style="position: relative; margin-top: -120px; text-align: left; padding-left: 40px; pointer-events: none;">
        <div style="
            font-size: 48px;
            font-weight: 900;
            color: #333333;
            -webkit-text-stroke: 3px #bbbbbb;
            text-stroke: 3px #bbbbbb;
            paint-order: stroke fill;
        ">
            {day_month_no_dots}
        </div>
    </div>
""", unsafe_allow_html=True)
