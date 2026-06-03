import streamlit as st
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Trip details", layout="centered")

def image_to_base64(img, fmt="JPEG"):
    buffered = BytesIO()
    img.save(buffered, format=fmt)
    return base64.b64encode(buffered.getvalue()).decode()

qr_code = Image.open("qr_code4.jpeg")
qr_code_str = image_to_base64(qr_code)

berlin_tz = ZoneInfo("Europe/Berlin")
now = datetime.now(berlin_tz)

today = now.strftime("%d.%m.%Y")
issued_date = (now - timedelta(days=1)).strftime("%d.%m.%Y")
issue_time = "12:21"
ticket_time = (now + timedelta(minutes=45)).strftime("%H:%M")

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, .stApp, [data-testid="stAppViewContainer"] {
    background: #f1f1f1;
    margin: 0 !important;
    padding: 0 !important;
}

[data-testid="stMainBlockContainer"] {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 390px !important;
}

.block-container {
    padding: 0 !important;
    margin: 0 auto !important;
    max-width: 390px !important;
}

div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

@keyframes vmt-sway {
    0%   { transform: translateX(-5px); }
    50%  { transform: translateX(5px); }
    100% { transform: translateX(-5px); }
}

@keyframes blink-time {
    0%, 48%   { opacity: 1; }
    50%, 100% { opacity: 0.18; }
}

.mobile-shell {
    width: 100%;
    background: #f1f1f1;
    color: #111111;
    font-family: Arial, Helvetica, sans-serif;
    overflow: visible;
}

.top-header {
    background: #1e2437;
    color: #ffffff;
    width: 100%;
    display: block;
    position: relative;
    z-index: 10;
    padding-top: 16px;
}

.top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 14px 18px 18px 18px;
}

.top-left {
    display: flex;
    align-items: center;
    gap: 14px;
}

.back-arrow {
    font-size: 21px;
    font-weight: 700;
    line-height: 1;
}

.top-title {
    font-size: 17px;
    font-weight: 700;
    line-height: 1;
}

.top-icons {
    font-size: 24px;
    line-height: 1;
    letter-spacing: 6px;
    opacity: 0.95;
}

.tabs {
    display: flex;
    width: 100%;
    color: #d6dbe5;
    font-size: 14px;
    font-weight: 700;
}

.tab {
    width: 50%;
    text-align: center;
    padding: 14px 0 16px 0;
    position: relative;
}

.tab.active {
    color: #ffffff;
}

.tab.active::after {
    content: "";
    position: absolute;
    left: 18%;
    right: 18%;
    bottom: 0;
    height: 4px;
    background: #ee9ca2;
    border-radius: 3px 3px 0 0;
}

.ticket-card {
    background: #ffffff;
}

.ticket-meta {
    position: relative;
    padding: 10px 18px 8px 18px;
}

.ticket-date {
    font-size: 12px;
    color: #5e5e5e;
    margin-bottom: 3px;
}

.ticket-id {
    position: absolute;
    top: 10px;
    right: 18px;
    font-size: 12px;
    color: #8a8a8a;
}

.ticket-name {
    font-size: 13px;
    font-weight: 700;
    color: #1c1c1c;
    margin-bottom: 2px;
}

.ticket-line {
    font-size: 12px;
    color: #6b6b6b;
}

.ticket-time {
    position: absolute;
    right: 18px;
    bottom: 9px;
    font-size: 12px;
    color: #efefef;
    background: rgba(245,245,245,0.75);
    padding: 1px 5px;
    border-radius: 4px;
}

.blinking-time {
    animation: blink-time 1.0s steps(1, end) infinite;
}

.vmt-row {
    text-align: center;
    padding-top: 4px;
    padding-bottom: 7px;
}

.vmt-logo {
    display: inline-flex;
    align-items: center;
    gap: 1px;
    line-height: 1;
    font-size: 18px;
    font-weight: 900;
    animation: vmt-sway 1.45s ease-in-out infinite;
}

.vmt-v { color: #76ab36; }
.vmt-m { color: #005fab; }
.vmt-t { color: #d8b11c; }

.dark-divider {
    height: 16px;
    background: #121827;
}

.qr-wrap {
    background: #ffffff;
    text-align: center;
    padding: 18px 0 22px 0;
}

.qr-wrap img {
    width: 86%;
    max-width: 318px;
    display: block;
    margin: 0 auto;
}

.content {
    background: #ffffff;
    padding: 0 22px 28px 22px;
    color: #1a1a1a;
}

.passenger {
    font-size: 20px;
    line-height: 1.08;
    margin-top: 4px;
    margin-bottom: 30px;
}

.route-block {
    font-size: 22px;
    font-weight: 800;
    line-height: 1.08;
    margin-bottom: 34px;
}

.copy {
    font-size: 18px;
    line-height: 1.16;
    margin-bottom: 28px;
}

.booking {
    font-size: 19px;
    line-height: 1.12;
    margin-bottom: 26px;
}

.watermark-wrap {
    position: relative;
    border-top: 2px solid #909090;
    padding-top: 16px;
    min-height: 250px;
    overflow: hidden;
}

.watermark-big {
    position: absolute;
    top: 6px;
    left: 8px;
    font-size: 38px;
    font-weight: 800;
    color: rgba(120,120,120,0.56);
    letter-spacing: 0.5px;
}

.watermark-bg {
    position: absolute;
    top: 54px;
    left: 0;
    right: 0;
    font-size: 17px;
    line-height: 1.02;
    font-weight: 700;
    color: rgba(140,140,140,0.28);
    transform: rotate(-4deg);
    white-space: pre-line;
}

.watermark-name {
    position: absolute;
    top: 96px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 20px;
    font-weight: 700;
    color: #111111;
    background: rgba(255,255,255,0.42);
    padding: 0 4px;
}

.watermark-date {
    position: absolute;
    bottom: 40px;
    left: 8px;
    font-size: 27px;
    color: #2b2b2b;
    letter-spacing: 1px;
}

.transport-row {
    display: flex;
    justify-content: center;
    gap: 16px;
    margin-top: 18px;
    padding-bottom: 10px;
}

.transport-pill {
    width: 64px;
    height: 64px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 18px;
    font-weight: 700;
}

.bus  { background: #9836a8; }
.zug  { background: #11a34f; }
.tram { background: #eb2f2f; }
</style>
""", unsafe_allow_html=True)

watermark_text = (
    "03.06.2026 VMT Gruppentageskarte Ab: 748 Eisenach Hbf 10 Erfurt "
    "über: Gotha Sättelstädt Julie Aasi gültig am: 03:00 Uhr Gesamtpreis: 40,50 "
) * 10

st.markdown(f"""
<div class="mobile-shell">
    <div class="top-header">
        <div class="top-row">
            <div class="top-left">
                <div class="back-arrow">←</div>
                <div class="top-title">Trip details</div>
            </div>
            <div class="top-icons">⌖ ⋮</div>
        </div>

        <div class="tabs">
            <div class="tab">Itinerary ❗</div>
            <div class="tab active">Ticket</div>
        </div>
    </div>

    <div class="ticket-card">
        <div class="ticket-meta">
            <div class="ticket-date">{today}</div>
            <div class="ticket-id">181258037062</div>
            <div class="ticket-name">VMT Gruppentageskarte</div>
            <div class="ticket-line">Ab 748 Eisenach, Preisstufe 8 CityRegio</div>
            <div class="ticket-time blinking-time">{ticket_time}</div>
        </div>

        <div class="vmt-row">
            <div class="vmt-logo">
                <span class="vmt-v">V</span><span class="vmt-m">M</span><span class="vmt-t">T</span>
            </div>
        </div>

        <div class="dark-divider"></div>

        <div class="qr-wrap">
            <img src="data:image/jpeg;base64,{qr_code_str}">
        </div>

        <div class="content">
            <div class="passenger">
                Julie Aasi<br>
                Ausweis: Amtlicher<br>
                Lichtbildausweis
            </div>

            <div class="route-block">
                Gruppentageskarte<br>
                gültig am: {today}<br>
                bis 03:00 Uhr des Folgetages<br>
                zw.: 748 Eisenach<br>
                und: 10 Erfurt<br>
                über: Gotha Sättelstädt<br>
                Preisstufe: 8 CityRegio
            </div>

            <div class="copy">
                Gültig für beliebig viele Fahrten für max. 5 Personen in den gelösten Tarifzonen
                (Start-, Ziel- und Wegzonen), bis zum Folgetag 3 Uhr, Mitnahme von Kindern bis
                Einschulung frei. Statt 1 Person kann 1 Fahrrad oder ein Hund mitgenommen werden.
            </div>

            <div class="copy">
                Es gelten die Beförderungs- und Tarifbestimmungen der im Verkehrsverbund
                Mittelthüringen (VMT) zusammenwirkenden Verkehrsunternehmen.
            </div>

            <div class="copy">
                Ausgegeben durch die DB Fernverkehr AG im Auftrag der DB Vertrieb GmbH.
            </div>

            <div class="booking">
                Auftrags-Nr: 181258037062<br>
                Ticketcode: N0DQFL3B<br>
                Gesamtpreis: 40,50 EUR<br>
                Ausgestellt am {issued_date} um<br>
                {issue_time} Uhr
            </div>

            <div class="watermark-wrap">
                <div class="watermark-big">181258037062</div>
                <div class="watermark-bg">{watermark_text}</div>
                <div class="watermark-name">Julie Aasi</div>
                <div class="watermark-date">03 06</div>
            </div>

            <div class="transport-row">
                <div class="transport-pill bus">BUS</div>
                <div class="transport-pill zug">Zug</div>
                <div class="transport-pill tram">Tram</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
