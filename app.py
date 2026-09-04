import warnings
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag


# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="InvoiceX",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# Theme state
# ---------------------------------------------------------
if "night_mode" not in st.session_state:
    st.session_state.night_mode = False

night_mode = st.session_state.night_mode

if night_mode:
    bg = "#101211"
    sidebar_bg = "#141615"
    panel_bg = "rgba(28, 31, 29, 0.78)"
    text = "#f1f1ec"
    muted = "#a6aaa3"
    border = "rgba(255,255,255,0.12)"
    input_bg = "#1b1e1c"
    input_text = "#f4f4ef"
    button_bg = "#f1f1ec"
    button_text = "#181916"
    button_hover = "#d8d8d1"
    glass_highlight = "rgba(255,255,255,0.055)"
else:
    bg = "#f3f3ef"
    sidebar_bg = "#fafaf7"
    panel_bg = "rgba(255, 255, 255, 0.70)"
    text = "#20211e"
    muted = "#6e716b"
    border = "rgba(30,32,28,0.13)"
    input_bg = "#ffffff"
    input_text = "#242520"
    button_bg = "#252621"
    button_text = "#ffffff"
    button_hover = "#41423c"
    glass_highlight = "rgba(255,255,255,0.52)"


# ---------------------------------------------------------
# CSS
# ---------------------------------------------------------
st.markdown(f"""
<style>
    html, body, [class*="css"] {{
        font-family: Arial, Helvetica, sans-serif;
    }}

    .stApp {{
        background: {bg};
        color: {text};
    }}

    .block-container {{
        max-width: 1160px;
        padding: 34px 52px 70px 52px;
    }}

    /* ---------- Subtle background treatment ---------- */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.025) 0%,
                transparent 45%,
                rgba(0,0,0,0.018) 100%
            );
        z-index: 0;
    }}

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {{
        background: {sidebar_bg};
        border-right: 1px solid {border};
    }}

    section[data-testid="stSidebar"] .block-container {{
        padding: 30px 20px;
    }}

    /* Keep sidebar navigation arrows visible when the sidebar is collapsed. */
    [data-testid="stSidebarCollapseButton"] button,
    button[data-testid="stExpandSidebarButton"] {{
        color: {text} !important;
        background: {sidebar_bg} !important;
        border-color: {border} !important;
    }}

    [data-testid="stSidebarCollapseButton"] [data-testid="stIconMaterial"],
    button[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"],
    [data-testid="stSidebarCollapseButton"] button svg,
    button[data-testid="stExpandSidebarButton"] svg {{
        color: {text} !important;
        fill: currentColor !important;
        stroke: currentColor !important;
    }}

    .brand-row {{
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 7px;
    }}

    .brand-mark {{
        width: 38px;
        height: 38px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid {border};
        border-radius: 10px;
        background: {glass_highlight};
        color: {text};
        font-size: 12px;
        font-weight: 800;
        letter-spacing: -0.04em;
        box-shadow: 0 5px 18px rgba(0,0,0,0.04);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }}

    .brand-name {{
        color: {text} !important;
        font-size: 20px;
        font-weight: 700;
        line-height: 1.1;
    }}

    .brand-description {{
        color: {muted} !important;
        font-size: 12px;
        margin-left: 50px;
        line-height: 1.4;
        margin-bottom: 26px;
    }}

    .sidebar-rule {{
        height: 1px;
        background: {border};
        margin: 0 0 22px 0;
    }}

    .sidebar-label {{
        color: {muted} !important;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.11em;
        text-transform: uppercase;
        margin-bottom: 9px;
    }}

    /* Make radio controls visible in both themes */
    section[data-testid="stSidebar"] .stRadio label,
    section[data-testid="stSidebar"] .stRadio label p,
    section[data-testid="stSidebar"] .stRadio [data-testid="stMarkdownContainer"] p {{
        color: {text} !important;
        font-size: 13px !important;
    }}

    section[data-testid="stSidebar"] .stRadio label {{
        padding: 8px 4px;
    }}

    section[data-testid="stSidebar"] .stRadio [role="radiogroup"] {{
        gap: 1px;
    }}

    .sidebar-note-title {{
        color: {text} !important;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 7px;
    }}

    .sidebar-note {{
        color: {muted} !important;
        font-size: 11.5px;
        line-height: 1.55;
    }}

    /* ---------- Top bar ---------- */
    .topbar {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 8px;
    }}

    .eyebrow {{
        color: {muted} !important;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }}

    .mode-label {{
        color: {muted} !important;
        font-size: 11px;
        text-align: right;
        margin-top: 4px;
    }}

    /* ---------- Heading ---------- */
    .page-title {{
        color: {text} !important;
        font-size: 39px !important;
        font-weight: 700 !important;
        line-height: 1.08 !important;
        letter-spacing: -0.038em !important;
        margin: 3px 0 0 0 !important;
        padding: 0 !important;
    }}

    .page-description {{
        color: {muted} !important;
        font-size: 14px;
        line-height: 1.65;
        max-width: 760px;
        margin-top: 10px;
        margin-bottom: 30px;
    }}

    /* ---------- Glass panels: subtle, not futuristic ---------- */
    .panel {{
        position: relative;
        background: {panel_bg};
        border: 1px solid {border};
        border-radius: 12px;
        padding: 27px 30px 26px 30px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.045);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        overflow: hidden;
    }}

    .panel::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 1px;
        background: rgba(255,255,255,0.35);
    }}

    .panel-title {{
        color: {text} !important;
        font-size: 16px;
        font-weight: 700;
        margin-bottom: 5px;
    }}

    .panel-description {{
        color: {muted} !important;
        font-size: 12.5px;
        line-height: 1.55;
        margin-bottom: 20px;
    }}

    /* ---------- Inputs ---------- */
    div[data-baseweb="input"] {{
        background: {input_bg} !important;
        border: 1px solid {border} !important;
        border-radius: 7px !important;
        box-shadow: none !important;
    }}

    div[data-baseweb="input"] > div {{
        background: {input_bg} !important;
        border: 0 !important;
        box-shadow: none !important;
    }}

    div[data-baseweb="input"] input {{
        background: {input_bg} !important;
        color: {input_text} !important;
        -webkit-text-fill-color: {input_text} !important;
        font-size: 14px !important;
    }}

    div[data-baseweb="input"] button {{
        color: {muted} !important;
        background: {input_bg} !important;
        border: 0 !important;
    }}

    div[data-baseweb="input"]:focus-within {{
        border-color: #777a72 !important;
        box-shadow: 0 0 0 1px #777a72 !important;
    }}

    .stNumberInput label,
    .stNumberInput label p {{
        color: {text} !important;
        font-size: 12px !important;
        font-weight: 600 !important;
    }}

    /* ---------- Button ---------- */
    .stFormSubmitButton > button {{
        width: auto !important;
        min-width: 180px;
        min-height: 41px;
        background: {button_bg} !important;
        color: {button_text} !important;
        border: 1px solid {button_bg} !important;
        border-radius: 7px !important;
        padding: 0 19px;
        font-size: 12.5px;
        font-weight: 600;
        box-shadow: none !important;
    }}

    .stFormSubmitButton > button:hover {{
        background: {button_hover} !important;
        border-color: {button_hover} !important;
        color: {button_text} !important;
    }}

    /* ---------- Theme toggle ---------- */
    div[data-testid="stToggle"] label p {{
        color: {muted} !important;
        font-size: 11px !important;
        font-weight: 600 !important;
    }}

    /* ---------- Result ---------- */
    .result {{
        background: {panel_bg};
        border: 1px solid {border};
        border-left: 3px solid #444640;
        border-radius: 9px;
        padding: 19px 22px;
        margin-top: 18px;
        box-shadow: 0 9px 26px rgba(0,0,0,0.035);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
    }}

    .result.safe {{
        border-left-color: #47705a;
    }}

    .result.warning {{
        border-left-color: #a45f31;
    }}

    .result-label {{
        color: {muted} !important;
        font-size: 9px;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }}

    .result-value {{
        color: {text} !important;
        font-size: 32px;
        font-weight: 700;
        margin: 4px 0 5px 0;
    }}

    .result-status {{
        color: {text} !important;
        font-size: 19px;
        font-weight: 700;
        margin: 4px 0 6px 0;
    }}

    .result-text {{
        color: {muted} !important;
        font-size: 12px;
        line-height: 1.5;
    }}

    .status-dot {{
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        margin-right: 7px;
    }}

    .dot-safe {{
        background: #47705a;
    }}

    .dot-warning {{
        background: #a45f31;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    footer {{
        visibility: hidden;
    }}

    .stSpinner > div {{
        border-top-color: #55574f !important;
    }}

    @media (max-width: 800px) {{
        .block-container {{
            padding: 25px 20px 50px 20px;
        }}

        .page-title {{
            font-size: 31px !important;
        }}

        .panel {{
            padding: 22px;
        }}
    }}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div class="brand-row">
        <div class="brand-mark">IX</div>
        <div class="brand-name">InvoiceX</div>
    </div>
    <div class="brand-description">Vendor invoice intelligence</div>
    <div class="sidebar-rule"></div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="sidebar-label">Modules</div>',
        unsafe_allow_html=True
    )

    selected_model = st.radio(
        "Choose module",
        [
            "Freight Cost Prediction",
            "Invoice Manual Approval Flag"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        '<div class="sidebar-rule" style="margin-top:24px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-note-title">About</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-note">'
        'InvoiceX uses trained machine-learning models to estimate '
        'freight costs and identify invoices that may need review.'
        '</div>',
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Top right theme toggle
# ---------------------------------------------------------
top_left, top_right = st.columns([8, 2])

with top_left:
    st.markdown(
        '<div class="eyebrow">Vendor Invoice Intelligence</div>',
        unsafe_allow_html=True
    )

with top_right:
    new_mode = st.toggle(
        "Night mode",
        value=st.session_state.night_mode,
        key="theme_toggle",
    )

    if new_mode != st.session_state.night_mode:
        st.session_state.night_mode = new_mode
        st.rerun()


# ---------------------------------------------------------
# Main heading
# ---------------------------------------------------------
if selected_model == "Freight Cost Prediction":
    st.markdown(
        '<div class="page-title">Freight cost prediction</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">'
        'Estimate expected freight cost from invoice value. '
        'Use the result as a reference for budgeting and invoice review.'
        '</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<div class="page-title">Invoice approval review</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-description">'
        'Check an invoice for patterns that may indicate a discrepancy '
        'and require manual approval.'
        '</div>',
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# Freight Cost Prediction
# ---------------------------------------------------------
if selected_model == "Freight Cost Prediction":

    st.markdown("""
    <div class="panel">
        <div class="panel-title">Invoice details</div>
        <div class="panel-description">
            Enter the shipment quantity and invoice value.
        </div>
    """, unsafe_allow_html=True)

    with st.form("freight_form", clear_on_submit=False):
        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Quantity",
                min_value=1,
                value=1200,
                help="Total number of units in the shipment."
            )

        with col2:
            dollars = st.number_input(
                "Invoice value ($)",
                min_value=1.0,
                value=18500.0,
                help="Total monetary value of the invoice."
            )

        st.markdown(
            '<div style="height:10px;"></div>',
            unsafe_allow_html=True
        )

        submit_freight = st.form_submit_button("Predict freight cost")

    st.markdown("</div>", unsafe_allow_html=True)

    if submit_freight:
        with st.spinner("Calculating prediction..."):
            input_data = {"Dollars": [dollars]}
            predictions = predict_freight_cost(input_data)["Predicted_Freight"]

        st.markdown(f"""
        <div class="result safe">
            <div class="result-label">Predicted freight cost</div>
            <div class="result-value">${predictions[0]:,.2f}</div>
            <div class="result-text">
                Estimated from an invoice value of ${dollars:,.2f}.
            </div>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# Invoice Approval Flag
# ---------------------------------------------------------
else:

    st.markdown("""
    <div class="panel">
        <div class="panel-title">Invoice discrepancy factors</div>
        <div class="panel-description">
            Compare invoice values with the corresponding purchased values.
        </div>
    """, unsafe_allow_html=True)

    with st.form("invoice_flag_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            invoice_quantity = st.number_input(
                "Invoice quantity",
                min_value=1,
                value=50,
                help="Quantity claimed on the vendor invoice."
            )

            freight = st.number_input(
                "Freight cost ($)",
                min_value=0.0,
                value=15.00,
                help="Freight amount on the invoice."
            )

        with col2:
            invoice_dollars = st.number_input(
                "Invoice value ($)",
                min_value=1.0,
                value=1500.00,
                help="Amount billed by the vendor."
            )

            total_item_quantity = st.number_input(
                "Purchased quantity",
                min_value=1,
                value=50,
                help="Quantity officially purchased."
            )

        with col3:
            total_item_dollars = st.number_input(
                "Purchased value ($)",
                min_value=1.0,
                value=1500.00,
                help="Expected value of the purchased items."
            )

        st.markdown(
            '<div style="height:10px;"></div>',
            unsafe_allow_html=True
        )

        submit_flag = st.form_submit_button("Evaluate invoice")

    st.markdown("</div>", unsafe_allow_html=True)

    if submit_flag:
        with st.spinner("Reviewing invoice..."):
            input_data = {
                "invoice_quantity": [invoice_quantity],
                "invoice_dollars": [invoice_dollars],
                "Freight": [freight],
                "total_item_quantity": [total_item_quantity],
                "total_item_dollars": [total_item_dollars]
            }

            flag_prediction = predict_invoice_flag(input_data)["flag_invoice"]
            is_flagged = bool(flag_prediction[0])

        if is_flagged:
            st.markdown("""
            <div class="result warning">
                <div class="result-label">Review status</div>
                <div class="result-status">
                    <span class="status-dot dot-warning"></span>
                    Manual approval required
                </div>
                <div class="result-text">
                    The model identified patterns that may indicate a discrepancy.
                    Review the invoice before approval.
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result safe">
                <div class="result-label">Review status</div>
                <div class="result-status">
                    <span class="status-dot dot-safe"></span>
                    Suitable for auto-approval
                </div>
                <div class="result-text">
                    No significant anomaly was identified by the model.
                </div>
            </div>
            """, unsafe_allow_html=True)
