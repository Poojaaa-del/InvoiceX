# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px

# from inference.predict_freight import predict_freight_cost
# from inference.predict_invoice_flag import predict_invoice_flag

# # ---------------------------------------------------------
# # Page Configuration
# # ---------------------------------------------------------
# st.set_page_config(
#     page_title="Vendor Invoice Intelligence",
#     page_icon="📦",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # ---------------------------------------------------------
# # Custom CSS for Premium UI
# # ---------------------------------------------------------
# st.markdown("""
# <style>
#     /* Main Background & Fonts */
#     .stApp {
#         font-family: 'Inter', sans-serif;
#     }
    
#     /* Header Styling */
#     .main-header {
#         background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
#         padding: 2.5rem;
#         border-radius: 12px;
#         color: white;
#         margin-bottom: 2rem;
#         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
#     }
#     .main-header h1 {
#         color: white !important;
#         font-size: 2.5rem;
#         font-weight: 800;
#         margin-bottom: 0.5rem;
#     }
#     .main-header p {
#         font-size: 1.1rem;
#         opacity: 0.9;
#         margin: 0;
#         color: white;
#     }

#     /* Card Styling */
#     .info-card {
#         background: var(--secondary-background-color);
#         padding: 1.5rem;
#         border-radius: 12px;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.1);
#         border: 1px solid rgba(128, 128, 128, 0.2);
#         margin-bottom: 1.5rem;
#     }
#     .info-card h3, .info-card p {
#         color: var(--text-color) !important;
#     }
    
#     /* Big Prediction Results */
#     .result-metric {
#         background: var(--secondary-background-color);
#         padding: 2rem;
#         border-radius: 16px;
#         text-align: center;
#         box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2);
#         border-top: 5px solid #3b82f6;
#         animation: fadeIn 0.5s ease-in;
#     }
#     .result-metric.danger {
#         border-top: 5px solid #ef4444;
#     }
#     .result-metric.success {
#         border-top: 5px solid #10b981;
#     }
#     .result-value {
#         font-size: 3rem;
#         font-weight: 800;
#         color: var(--text-color);
#         margin: 1rem 0;
#     }
    
#     @keyframes fadeIn {
#         from { opacity: 0; transform: translateY(10px); }
#         to { opacity: 1; transform: translateY(0); }
#     }
    
#     /* Buttons */
#     .stButton>button {
#         width: 100%;
#         border-radius: 8px;
#         font-weight: 600;
#         height: 3rem;
#         background-color: #3b82f6;
#         color: white;
#         border: none;
#         transition: all 0.2s;
#     }
#     .stButton>button:hover {
#         background-color: #2563eb;
#         color: white;
#         box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------------------------------------------------
# # Header Section
# # ---------------------------------------------------------
# st.markdown("""
# <div class="main-header">
#     <h1>📦 Vendor Invoice Intelligence</h1>
#     <p>AI-Driven Freight Cost Prediction & Invoice Risk Flagging</p>
#     This internal analytics portal leverages machine learning to<br>
# - Forecast freight costs accurately<br>
# - Detect risky or abnormal vendor invoices<br>
# - Reduce financial leakage and manual workload<br>
# </div>
# """, unsafe_allow_html=True)

# # st.markdown("""
# # # 📦 Vendor Invoice Intelligence Portal
# # ### AI-Driven Freight Cost Prediction & Invoice Risk Flagging

# # This internal analytics portal leverages machine learning to
# # - **Forecast freight costs accurately**
# # - **Detect risky or abnormal vendor invoices**
# # - **Reduce financial leakage and manual workload**
# # """)
# # ---------------------------------------------------------
# # Sidebar
# # ---------------------------------------------------------
# with st.sidebar:
#     st.image("https://cdn-icons-png.flaticon.com/512/3143/3143460.png", width=60)
#     st.markdown("### **Navigation**")
#     selected_model = st.radio(
#         "Choose Module",
#         [
#             "🚛 Freight Cost Prediction",
#             "📋 Invoice Manual Approval Flag"
#         ],
#         label_visibility="collapsed"
#     )
    
#     st.markdown("---")
#     st.markdown("""
#     ### 💡 **Business Impact**
#     <div style='background: var(--secondary-background-color); color: var(--text-color); padding: 1rem; border-radius: 8px; font-size: 0.9rem; border: 1px solid rgba(128, 128, 128, 0.2);'>
#     <b>• Improved cost forecasting</b><br>
#     <b>• Reduced invoice fraud</b><br>
#     <b>• Faster finance operations</b>
#     </div>
#     """, unsafe_allow_html=True)

# # ---------------------------------------------------------
# # Module 1: Freight Cost Prediction
# # ---------------------------------------------------------
# if selected_model == "🚛 Freight Cost Prediction":
    
#     st.markdown("""
#     <div class="info-card">
#         <h3 style="margin-top:0;">🎯 Objective</h3>
#         <p style="margin-bottom:0; color:#475569;">Predict the freight cost for vendor invoices using <b>Quantity</b> and <b>Invoice Dollars</b> to support accurate budgeting, forecasting, and vendor negotiation.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.container():
#         with st.form("freight_form", clear_on_submit=False):
#             st.markdown("#### 📝 Input Invoice Details")
#             col1, col2 = st.columns(2)
            
#             with col1:
#                 quantity = st.number_input(
#                     "📦 Quantity",
#                     min_value=1,
#                     value=1200,
#                     help="Total number of units in the shipment"
#                 )
                
#             with col2:
#                 dollars = st.number_input(
#                     "💰 Invoice Dollars ($)",
#                     min_value=1.0,
#                     value=18500.0,
#                     help="Total monetary value of the invoice"
#                 )

#             st.write("")
#             submit_freight = st.form_submit_button("Predict Freight Cost 🚀")

#     if submit_freight:
#         with st.spinner("Analyzing shipping matrix and historical rates..."):
#             input_data = {
#                 "Dollars": [dollars]
#             }
#             predictions = predict_freight_cost(input_data)['Predicted_Freight']
            
#             st.markdown(f"""
#             <div class="result-metric success">
#                 <span style="color:#64748b; font-size:1.1rem; text-transform:uppercase; letter-spacing:1px; font-weight:600;">Predicted Freight Cost</span>
#                 <div class="result-value">${predictions[0]:,.2f}</div>
#                 <span style="color:#10b981; font-weight:500;">prediction generated successfully based on ${dollars:,.2f} invoice value.</span>
#             </div>
#             """, unsafe_allow_html=True)

# # -----------------------------------------------------------
# # Module 2: Invoice Flag Prediction
# # -----------------------------------------------------------
# else:
#     st.markdown("""
#     <div class="info-card">
#         <h3 style="margin-top:0;">🎯 Objective</h3>
#         <p style="margin-bottom:0; color:#475569;">Predict whether a vendor invoice should be <b>flagged for manual approval</b> based on abnormal cost, freight, or delivery discrepancy patterns.</p>
#     </div>
#     """, unsafe_allow_html=True)

#     with st.container():
#         with st.form("invoice_flag_form"):
#             st.markdown("#### 📝 Input Discrepancy Factors")
#             col1, col2, col3 = st.columns(3)

#             with col1:
#                 invoice_quantity = st.number_input(
#                     "Invoice Quantity",
#                     min_value=1,
#                     value=50,
#                     help="Quantity claimed on the vendor invoice"
#                 )
#                 freight = st.number_input(
#                     "Freight Cost ($)",
#                     min_value=0.0,
#                     value=15.00
#                 )
                
#             with col2:
#                 invoice_dollars = st.number_input(
#                     "Invoice Dollars ($)",
#                     min_value=1.0,
#                     value=1500.00,
#                     help="Amount billed by the vendor"
#                 )
#                 total_item_quantity = st.number_input(
#                     "Purchased Quantity",
#                     min_value=1,
#                     value=50,
#                     help="Internal quantity officially purchased"
#                 )

#             with col3:
#                 total_item_dollars = st.number_input(
#                   "Purchased Dollars ($)",
#                   min_value=1.0,
#                   value=1500.00,
#                   help="Internal expected cost of items"
#                 )

#             st.write("")
#             submit_flag = st.form_submit_button("Evaluate Risk Status 🛡️")

#     if submit_flag:
#         with st.spinner("Running discrepancy analysis..."):
#             input_data = {
#                 "invoice_quantity": [invoice_quantity],
#                 "invoice_dollars": [invoice_dollars],
#                 "Freight": [freight],
#                 "total_item_quantity": [total_item_quantity],
#                 "total_item_dollars": [total_item_dollars]
#             }

#             flag_prediction = predict_invoice_flag(input_data)['flag_invoice']
#             is_flagged = bool(flag_prediction[0])

#             if is_flagged:
#                 st.markdown("""
#                 <div class="result-metric danger">
#                     <span style="color:#ef4444; font-size:3rem;">🚨</span><br>
#                     <span style="color:#64748b; font-size:1.1rem; text-transform:uppercase; letter-spacing:1px; font-weight:600;">Status</span>
#                     <div style="font-size: 2rem; font-weight: 800; color: #ef4444; margin: 1rem 0;">Requires Manual Approval</div>
#                     <span style="color:#ef4444; font-weight:500;">High discrepancy detected between invoice and purchase orders.</span>
#                 </div>
#                 """, unsafe_allow_html=True)
#             else:
#                 st.markdown("""
#                 <div class="result-metric success">
#                     <span style="color:#10b981; font-size:3rem;">✅</span><br>
#                     <span style="color:#64748b; font-size:1.1rem; text-transform:uppercase; letter-spacing:1px; font-weight:600;">Status</span>
#                     <div style="font-size: 2rem; font-weight: 800; color: #10b981; margin: 1rem 0;">Safe for Auto-Approval</div>
#                     <span style="color:#10b981; font-weight:500;">No significant anomalies detected. Standard automated processing authorized.</span>
#                 </div>
#                 """, unsafe_allow_html=True)


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
    page_icon="▣",
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
