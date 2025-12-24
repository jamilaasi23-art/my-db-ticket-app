import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

# Full-screen app mode
st.set_page_config(page_title="Mein Ticket", layout="centered")

# Hide Streamlit elements
st.markdown("""
    <style>
    #MainMenu, footer, header {visibility: hidden;}
    .stApp {padding-top: 0px;}
    </style>
""", unsafe_allow_html=True)

# Load images (use your file names)
top_bar = Image.open("top_bar.png")
qr_code = Image.open("qr_code.png")
bottom_bg = Image.open("bottom_background.png")

# Dynamic dates (updates every open)
now = datetime.now()
today = now.strftime("%d.%m.%Y")
tomorrow = (now + timedelta(days=1)).strftime("%d.%m.%Y")
future_time = (now + timedelta(hours=2)).strftime("%H:%M")
day_month = now.strftime("%d.%m.")

# Top bar
st.image(top_bar, use_column_width=True)

# QR code
st.image(qr_code, use_column_width=True)

# Main content
st.markdown("<h1 style='text-align: left; font-size: 28px; margin: 15px 0 5px;'>Jamil Aasi</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #cc1e2c; font-size: 18px; font-weight: bold; margin-bottom: 25px;'>CIV 1080</p>", unsafe_allow_html=True)

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
st.write("Zubringung: Gilt nur für eingetragene Züge. Dieser ist bei der Kontrolle vorzulegen. Nur gültig mit amtlichem Lichtbildausweis. Dieser ist bei der Kontrolle vorzulegen. Bei Fahrkarten mit BahnCard-Rabatt zeugen Sie bitte zustätzlich Ihre gültige BahnCard vor. Für die nationalen und internationalen Verkehrsverbindungen der DB AG. Innerhalb von Verkehrsverbünden und Tarifgemeinschaften gelten deren Bestimmungen. Alle Bedingungen finden Sie unter www.bahn.de/agb und www.diebefoerderer.de. Eine Fahrkarte entspricht grundsätzlich einem Beförderungsvertrag, mehrere Fahrkarten mehreren Beförderungsverträgen. Beförderungsverträgen können dabei ein oder mehrere Verkehrsmittelnetze sein. Für die Eisenbahnfahrt handelt es sich bei dieser Fahrkarte um eine Durchgangsfahrkarte gemäß der Fahrgastrechte-Verordnung (EU) 2021/782 für den Eisenbahnverkehr. Für eine Fahrkarte, die neben der Eisenbahnfahrt noch die Fahrt mit einem anderen Verkehrsmittel umfasst (z.B. Schiff zu den Nordseeinseln; ÖPNV) gilt: Die Fahrkarte dokumentiert dann je einen gesonderten Beförderungsvertrag pro Richtung für die Beförderungsträger. Die Haftung erfolgt auch nur für den jeweiligen Beförderungsvertrag. Be einer zu erwartenden Verspätung ab 20 Minuten am Zielbahnhof Ihrer Fahrkarte ist die ausführende Bescheinigung Kleinkindabteil, Rollstuhlplatzplätze und Voranplatzplätze für Personen mit eingeschränkter Mobilität sowie Platz für Reiseroute mit BahnBonus Gold, oder der Platinum Status sind bei Bedarf für diese Personenengruppen freizugeben. Stornierung ausgeschlossen.")  # Full text from screenshot – edit if needed

# Bottom background with overlay
st.image(bottom_bg, use_column_width=True)
st.markdown(f"""
    <div style="position: relative; margin-top: -180px; text-align: center; pointer-events: none; color: #000;">
        <div style="font-size: 62px; font-weight: 900; letter-spacing: 10px;">225073878296</div>
        <div style="font-size: 28px; font-weight: bold; margin: 15px 0;">Jamil Aasi</div>
        <div style="font-size: 44px; font-weight: 900;">{day_month}.</div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("<p style='text-align: center; color: gray; font-size: 14px; margin-top: 60px;'>Stornierung Ausgeschlossen<br>Ticketcode: BNAZcb...</p>", unsafe_allow_html=True)