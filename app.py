import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import base64
from io import BytesIO

# Page config
st.set_page_config(page_title="Mein Ticket", layout="centered")

# Load reliable OCR-B font from CDN
st.markdown("""
    <link href="https://cdn.jsdelivr.net/gh/jaycee723/ocr-b@master/ocrb.css" rel="stylesheet">
""", unsafe_allow_html=True)

# CSS with stronger pull-up and bigger text
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
        margin-top: 80px; /* Reduced further to compensate strong pull-up */
        background-color: white;
        color: black;
        padding: 0 5px 5px 5px;
        line-height: 1.1;
        font-size: 22px; /* Increased text size */
    }
    .section-header {
        font-weight: bold;
        font-size: 22px;
        margin: 10px 0 4px 0;
    }
    .name-line {
        margin-top: -45px; /* Even stronger pull-up for tighter gap */
        margin-bottom: -2px;
        font-size: 22px;
    }
    </style>
""", unsafe_allow_html=True)

# Load images
top_bar = Image.open("top_bar.jpeg")
qr_code = Image.open("qr_code4.jpeg")
bottom_bg = Image.open("bottom_background.jpeg")

# Convert to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode()

top_bar_str = image_to_base64(top_bar)
qr_code_str = image_to_base64(qr_code)
bottom_bg_str = image_to_base64(bottom_bg)

# Dynamic dates
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month_with_space = now.strftime("%d %m")  # "26 12" with one normal space

# Fixed top bar
st.markdown(
    f'<div class="fixed-top-bar"><img src="data:image/jpeg;base64,{top_bar_str}" style="width:100%; height:auto; display:block;"></div>',
    unsafe_allow_html=True
)

# 40px space after top bar
st.markdown("<div style='height: 40px; background-color: white;'></div>", unsafe_allow_html=True)

# QR code as raw HTML
st.markdown(
    f'<img src="data:image/jpeg;base64,{qr_code_str}" style="width:100%; height:auto; display:block; margin:0; padding:0; margin-bottom: -30px;">',
    unsafe_allow_html=True
)

# Text content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("<div class='name-line'>Jamil Aasi</div>", unsafe_allow_html=True)

st.markdown("<p class='section-header'>CIV 1080</p>", unsafe_allow_html=True)

st.markdown("<p class='section-header'>Gültigkeit</p>", unsafe_allow_html=True)
st.markdown(f"""
IC/EC Fahrkarte (Einfache Fahrt)<br>
Super Sparpreis<br>
2. Klasse<br>
1 Person (27-64 Jahre)<br>
Von: {today}, 00:00 Uhr<br>
Bis: {tomorrow}, 10:00 Uhr
""", unsafe_allow_html=True)

st.markdown("<p class='section-header'>Verbindung</p>", unsafe_allow_html=True)
st.markdown(f"""
Eisenach Hbf - Dortmund Hbf<br>
Zugbindung:<br>
IC 2156, {future_time} Uhr am {today}<br>
Via: <1080>(HERS/BEB)KS*WAR(BRI/ALT*PB*HAM)
""", unsafe_allow_html=True)

st.markdown("<p class='section-header'>Buchungsdetails</p>", unsafe_allow_html=True)
st.markdown(f"""
Gebucht am: {today} um 04:35 Uhr<br>
Auftrags-Nr: 225073878296<br>
Gesamtpreis: 45,99 €
""", unsafe_allow_html=True)

st.markdown("<p class='section-header'>Konditionen</p>", unsafe_allow_html=True)
st.markdown("""
Zugbindung: Gilt nur für eingetragene Züge.<br>
Nur gültig mit amtlichem Lichtbildausweis. Dieser ist bei der Kontrolle vorzuzeigen.<br>
Bei Fahrkarten mit BahnCard-Rabatt zeigen Sie bitte zusätzlich Ihre gültige BahnCard vor.<br>
Es gelten die nationalen und internationalen Beförderungsbedingungen der DB AG. Innerhalb von Verkehrsverbünden und Tarifgemeinschaften gelten deren Bestimmungen. Alle Bedingungen finden Sie unter www.bahn.de/agb und www.diebefoerderer.de.<br>
Eine Fahrkarte entspricht grundsätzlich einem Beförderungsvertrag, mehrere Fahrkarten mehreren Beförderungsverträgen. Vertraglicher Beförderer können dabei ein oder mehrere Verkehrsunternehmen sein. Für die Eisenbahnfahrt handelt es sich bei dieser Fahrkarte um eine Durchgangsfahrkarte gemäß der Fahrgastrechte-Verordnung (EU) 2021/782 für den Eisenbahnverkehr. Für eine Fahrkarte, die neben der Eisenbahnfahrt noch die Fahrt mit einem anderen Verkehrsträger umfasst (z.B. Schiff zu den Nordseeinseln; ÖPNV) gilt: Die Fahrkarte dokumentiert dann je einen gesonderten Beförderungsvertrag pro Richtung und pro Verkehrsträger. Die Haftung für fahrgastrechtliche Ansprüche gilt dann auch nur für den jeweiligen Beförderungsvertrag.<br>
Bei einer zu erwartenden Verspätung ab 20 Minuten am Zielbahnhof Ihrer Fahrkarte ist die Zugbindung Ihrer Fahrt ohne besondere Bescheinigung aufgehoben.<br>
Kleinkindabteile, Rollstuhlstellplätze und Vorrangplätze für Personen mit eingeschränkter Mobilität sowie Plätze für Reisende mit BahnBonus Gold- oder Platinstatus sind bei Bedarf für diese Personengruppen freizugeben.<br><br>
Stornierung ausgeschlossen<br>
Ticketcode: BNAZCDJ0
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Bottom background as raw HTML — full width
st.markdown(
    f'<img src="data:image/jpeg;base64,{bottom_bg_str}" style="width:100vw; height:auto; display:block; margin:0; padding:0;">',
    unsafe_allow_html=True
)

# Bottom date — OCR-B font from reliable CDN
st.markdown(f"""
    <div style="position: relative; margin-top: -280px; text-align: left; padding-left: 20px; pointer-events: none;">
        <div style="
            font-size: 34px;
            font-weight: 900;
            font-family: 'OCR B', monospace;
            color: #444444;
            -webkit-text-stroke: 3px #bbbbbb;
            text-stroke: 3px #bbbbbb;
            paint-order: stroke fill;
        ">
            {day_month_with_space}
        </div>
    </div>
""", unsafe_allow_html=True)
