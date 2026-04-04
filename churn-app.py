
import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="ChurnIQ — Churn Intelligence",
    page_icon="🔮",
    layout="wide"
)

# ─────────────────────────────────────────────
# CUSTOM CSS — Full Dark Luxury Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'Outfit', sans-serif;
    color: #f1f5f9;
}

/* Global label brightness — all Streamlit widget labels */
div[data-testid="stWidgetLabel"] p,
div[data-testid="stWidgetLabel"] label,
.stSlider label,
.stMarkdown strong,
.stMarkdown b {
    color: #ffffff !important;
    font-weight: 700 !important;
}
.stApp {
    background: #050810;
    background-image:
        radial-gradient(ellipse 80% 60% at 50% -10%, rgba(99,102,241,0.18) 0%, transparent 70%),
        radial-gradient(ellipse 40% 40% at 90% 80%, rgba(168,85,247,0.10) 0%, transparent 60%);
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 3rem 4rem; max-width: 1400px; }

/* ── Hero Banner ── */
.hero-banner {
    background: linear-gradient(135deg, #0f1629 0%, #111827 50%, #0f0a1e 100%);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 20px;
    padding: 2.5rem 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -60px; right: -60px;
    width: 220px; height: 220px;
    background: radial-gradient(circle, rgba(99,102,241,0.20) 0%, transparent 70%);
    border-radius: 50%;
}
.hero-banner::after {
    content: '';
    position: absolute;
    bottom: -40px; left: 40%;
    width: 300px; height: 120px;
    background: radial-gradient(ellipse, rgba(168,85,247,0.12) 0%, transparent 70%);
}
.hero-title {
    font-size: 2.8rem;
    font-weight: 800;
    background: linear-gradient(90deg, #a5b4fc, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
    letter-spacing: -0.5px;
}
.hero-sub {
    font-size: 1.05rem;
    color: #94a3b8;
    margin-top: 0.5rem;
    font-weight: 300;
}
.hero-badge {
    display: inline-block;
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.4);
    color: #a5b4fc;
    padding: 4px 14px;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 1rem;
}

/* ── Status pill ── */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.35);
    color: #6ee7b7;
    padding: 6px 16px;
    border-radius: 50px;
    font-size: 0.82rem;
    font-weight: 500;
    margin-bottom: 1.5rem;
}
.status-dot {
    width: 7px; height: 7px;
    background: #10b981;
    border-radius: 50%;
    animation: pulse 1.8s infinite;
}
@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.4); }
}

/* ── Tab styling ── */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(15,22,41,0.8);
    border-radius: 14px;
    padding: 6px;
    gap: 4px;
    border: 1px solid rgba(99,102,241,0.15);
    margin-bottom: 1.5rem;
}
.stTabs [data-baseweb="tab"] {
    border-radius: 10px;
    padding: 10px 24px;
    font-family: 'Outfit', sans-serif;
    font-weight: 500;
    font-size: 0.9rem;
    color: #64748b;
    border: none;
    transition: all 0.2s ease;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    color: white !important;
    box-shadow: 0 4px 15px rgba(99,102,241,0.35);
}

/* ── Section header ── */
.section-header {
    font-size: 1.4rem;
    font-weight: 700;
    color: #a5b4fc;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 0.8rem;
    border-bottom: 1px solid rgba(99,102,241,0.2);
}

/* ── Slider labels ── */
.input-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 2px;
}

/* ── Card / glass panel ── */
.glass-card {
    background: rgba(15,22,41,0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(99,102,241,0.18);
    border-radius: 16px;
    padding: 1.6rem;
    margin-bottom: 1rem;
}

/* ── Insight boxes ── */
.insight-box {
    background: rgba(15,22,41,0.7);
    border-left: 3px solid #818cf8;
    padding: 14px 18px;
    margin: 10px 0;
    border-radius: 10px;
    font-size: 0.9rem;
    color: #cbd5e1;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.2s ease;
    border: 1px solid rgba(99,102,241,0.12);
    border-left: 3px solid #818cf8;
}
.insight-box:hover {
    background: rgba(99,102,241,0.10);
    transform: translateX(4px);
}

/* ── Result cards ── */
.result-high {
    background: linear-gradient(135deg, rgba(239,68,68,0.15), rgba(220,38,38,0.08));
    border: 1px solid rgba(239,68,68,0.4);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    text-align: center;
}
.result-medium {
    background: linear-gradient(135deg, rgba(245,158,11,0.15), rgba(217,119,6,0.08));
    border: 1px solid rgba(245,158,11,0.4);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    text-align: center;
}
.result-low {
    background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(5,150,105,0.08));
    border: 1px solid rgba(16,185,129,0.4);
    border-radius: 16px;
    padding: 1.5rem 2rem;
    text-align: center;
}
.result-label {
    font-size: 0.8rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 0.5rem;
}
.result-score {
    font-size: 3.5rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    line-height: 1;
}

/* ── Predict button ── */
.stButton > button {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 2.5rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 20px rgba(99,102,241,0.35) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 30px rgba(99,102,241,0.5) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
}

/* ── Sliders ── */
.stSlider [data-baseweb="slider"] { margin-top: 0; }

/* Thumb value bubble */
.stSlider [data-testid="stThumbValue"] {
    background: #6366f1 !important;
    color: #ffffff !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
}

/* Slider label — the main text like "Age", "Login Frequency" */
.stSlider label,
.stSlider > label,
div[data-testid="stSlider"] label,
div[data-testid="stSlider"] > div > label {
    color: #f1f5f9 !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    letter-spacing: 0.2px !important;
    font-family: 'Outfit', sans-serif !important;
}

/* Slider min/max range numbers */
.stSlider [data-testid="stTickBarMin"],
.stSlider [data-testid="stTickBarMax"] {
    color: #94a3b8 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
}

/* Active track color */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: #6366f1 !important;
    border: 3px solid #a5b4fc !important;
    box-shadow: 0 0 10px rgba(99,102,241,0.6) !important;
    width: 20px !important;
    height: 20px !important;
}

/* Filled track */
.stSlider [data-baseweb="slider"] div[class*="Track"] div:first-child {
    background: linear-gradient(90deg, #4f46e5, #818cf8) !important;
}

/* All widget labels globally */
.stSlider p, .stSlider span {
    color: #f1f5f9 !important;
}

/* Section subheadings inside glass card */
.glass-card p, .glass-card strong, .glass-card b {
    color: #e2e8f0 !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
}

/* All markdown bold text in input area */
div[data-testid="column"] strong {
    color: #ffffff !important;
    font-size: 1.05rem !important;
    font-weight: 700 !important;
}

/* General label brightness boost */
label, .stMarkdown p {
    color: #e2e8f0 !important;
}


/* ── Metric cards ── */
.metric-card {
    background: rgba(15,22,41,0.8);
    border: 1px solid rgba(99,102,241,0.18);
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    text-align: center;
}
.metric-value {
    font-size: 2rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    background: linear-gradient(90deg, #a5b4fc, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.metric-label {
    font-size: 0.72rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 600;
    margin-top: 2px;
}

/* ── Info tip ── */
.tip-box {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 12px;
    padding: 12px 18px;
    font-size: 0.85rem;
    color: #a5b4fc;
    margin: 1rem 0;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* ── Dataframe ── */
.stDataFrame { border-radius: 12px; overflow: hidden; }

/* ── Divider ── */
hr { border-color: rgba(99,102,241,0.15) !important; margin: 2rem 0 !important; }

/* ── Footer ── */
.footer-text {
    text-align: center;
    color: #334155;
    font-size: 0.8rem;
    font-weight: 500;
    padding: 1rem 0;
    letter-spacing: 0.5px;
}
.footer-text span {
    color: #6366f1;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# LOAD MODEL
# ─────────────────────────────────────────────
model = joblib.load("random_forest_model.joblib")
columns = joblib.load("model_columns.joblib")
means = joblib.load("feature_means.joblib")

# ─────────────────────────────────────────────
# HERO BANNER
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-badge">🔮 AI-Powered Analytics</div>
    <div class="hero-title">ChurnIQ Dashboard</div>
    <div class="hero-sub">Customer Churn Intelligence — Predict risk, understand behavior, retain customers</div>
</div>
""", unsafe_allow_html=True)

# Model loaded pill
st.markdown("""
<div class="status-pill">
    <div class="status-dot"></div>
    Random Forest Model · Active & Ready
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🎯  Churn Prediction", "📊  EDA Insights", "⚡  Feature Importance"])

# ═══════════════════════════════════════════
# TAB 1 — PREDICTION
# ═══════════════════════════════════════════
with tab1:

    st.markdown('<div class="section-header">🧑‍💼 Enter Customer Profile</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("**👤 Demographics & Activity**")
        age = st.slider("Age", 20, 80, 30)
        total_purchases = st.slider("Total Purchases", 0, 100, 10)
        login_frequency = st.slider("Login Frequency (per month)", 0, 50, 10)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("**🛒 Purchase & Support Behavior**")
        avg_order_value = st.slider("Average Order Value (₹)", 100, 5000, 500)
        days_since_last_purchase = st.slider("Days Since Last Purchase", 0, 120, 30)
        customer_service_calls = st.slider("Customer Service Calls", 0, 20, 2)
        cart_abandonment_rate = st.slider("Cart Abandonment Rate", 0.0, 1.0, 0.3)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tip-box">
        💡 <b>Tip:</b> High inactivity + frequent complaints = elevated churn risk. Use sliders to simulate scenarios.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔮  Run Churn Prediction"):

        # ── Core ML logic (unchanged) ──
        input_dict = means.to_dict()
        input_dict.update({
            'Age': age,
            'Total_Purchases': total_purchases,
            'Average_Order_Value': avg_order_value,
            'Login_Frequency': login_frequency,
            'Days_Since_Last_Purchase': days_since_last_purchase,
            'Customer_Service_Calls': customer_service_calls,
            'Cart_Abandonment_Rate': cart_abandonment_rate
        })
        input_df = pd.DataFrame([input_dict])[columns]
        prob = model.predict_proba(input_df)[0][1]
        threshold = 0.4
        prediction = 1 if prob > threshold else 0

        st.markdown("---")
        st.markdown('<div class="section-header">📋 Prediction Result</div>', unsafe_allow_html=True)

        res_col1, res_col2, res_col3 = st.columns([1.2, 1, 1])

        with res_col1:
            if prob > 0.7:
                st.markdown(f"""
                <div class="result-high">
                    <div class="result-label" style="color:#f87171;">🔴 High Risk</div>
                    <div class="result-score" style="color:#ef4444;">{prob:.1%}</div>
                    <div style="color:#94a3b8;font-size:0.8rem;margin-top:8px;">Immediate action needed</div>
                </div>""", unsafe_allow_html=True)
            elif prob > 0.4:
                st.markdown(f"""
                <div class="result-medium">
                    <div class="result-label" style="color:#fbbf24;">🟡 Medium Risk</div>
                    <div class="result-score" style="color:#f59e0b;">{prob:.1%}</div>
                    <div style="color:#94a3b8;font-size:0.8rem;margin-top:8px;">Monitor closely</div>
                </div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="result-low">
                    <div class="result-label" style="color:#6ee7b7;">🟢 Low Risk</div>
                    <div class="result-score" style="color:#10b981;">{prob:.1%}</div>
                    <div style="color:#94a3b8;font-size:0.8rem;margin-top:8px;">Customer is stable</div>
                </div>""", unsafe_allow_html=True)

        with res_col2:
            st.markdown(f"""
            <div class="metric-card" style="height:100%;">
                <div class="metric-value">{prob:.2%}</div>
                <div class="metric-label">Churn Probability</div>
                <div style="height:1px;background:rgba(99,102,241,0.2);margin:12px 0;"></div>
                <div class="metric-value" style="font-size:1.4rem;">{(1-prob):.2%}</div>
                <div class="metric-label">Retention Probability</div>
            </div>""", unsafe_allow_html=True)

        with res_col3:
            st.markdown(f"""
            <div class="metric-card" style="height:100%;">
                <div class="metric-value" style="font-size:1.6rem;">{"CHURN" if prediction == 1 else "RETAIN"}</div>
                <div class="metric-label">Model Decision</div>
                <div style="height:1px;background:rgba(99,102,241,0.2);margin:12px 0;"></div>
                <div class="metric-value" style="font-size:1.4rem;">0.40</div>
                <div class="metric-label">Decision Threshold</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.progress(int(prob * 100))

        # ── Plotly bar chart (styled) ──
        fig = go.Figure(data=[
            go.Bar(
                x=["Churn Risk", "Retention"],
                y=[prob, 1 - prob],
                marker=dict(
                    color=["rgba(239,68,68,0.85)", "rgba(16,185,129,0.85)"],
                    line=dict(color=["#ef4444", "#10b981"], width=2)
                ),
                text=[f"{prob:.1%}", f"{1-prob:.1%}"],
                textposition="outside",
                textfont=dict(color="white", size=14, family="JetBrains Mono"),
                width=0.45
            )
        ])
        fig.update_layout(
            title=dict(text="Churn Probability Breakdown", font=dict(color="#a5b4fc", size=16, family="Outfit"), x=0.03),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,22,41,0.5)",
            font=dict(color="#94a3b8", family="Outfit"),
            xaxis=dict(gridcolor="rgba(99,102,241,0.1)", tickfont=dict(size=13)),
            yaxis=dict(gridcolor="rgba(99,102,241,0.1)", range=[0, 1.15], tickformat=".0%"),
            height=320,
            margin=dict(l=10, r=10, t=50, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════
# TAB 2 — EDA INSIGHTS
# ═══════════════════════════════════════════
with tab2:

    st.markdown('<div class="section-header">📊 Exploratory Data Analysis</div>', unsafe_allow_html=True)

    eda_col1, eda_col2 = st.columns([1, 1.4], gap="large")

    with eda_col1:
        st.markdown("**🔍 Key Behavioral Signals**")
        insights = [
            ("📅", "Higher days since last purchase → elevated churn probability"),
            ("📞", "More customer service calls → growing dissatisfaction"),
            ("🛒", "High cart abandonment → checkout friction & intent drop-off"),
            ("🔐", "Low login frequency → disengagement from platform"),
            ("💎", "High-value customers require dedicated retention strategies"),
        ]
        for icon, text in insights:
            st.markdown(f"""
            <div class="insight-box">
                <span style="font-size:1.2rem;">{icon}</span>
                <span>{text}</span>
            </div>""", unsafe_allow_html=True)

    with eda_col2:
        df_plot = pd.DataFrame({
            "Type": ["Churned Customers", "Retained Customers"],
            "Avg Days Since Purchase": [36, 26]
        })
        fig = go.Figure(data=[
            go.Bar(
                x=df_plot["Type"],
                y=df_plot["Avg Days Since Purchase"],
                marker=dict(
                    color=["rgba(239,68,68,0.8)", "rgba(99,102,241,0.8)"],
                    line=dict(color=["#ef4444", "#818cf8"], width=2)
                ),
                text=["36 days", "26 days"],
                textposition="outside",
                textfont=dict(color="white", size=13, family="JetBrains Mono"),
                width=0.4
            )
        ])
        fig.update_layout(
            title=dict(text="Purchase Recency: Churn vs Retained", font=dict(color="#a5b4fc", size=15, family="Outfit"), x=0.03),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,22,41,0.5)",
            font=dict(color="#94a3b8", family="Outfit"),
            xaxis=dict(gridcolor="rgba(99,102,241,0.08)"),
            yaxis=dict(gridcolor="rgba(99,102,241,0.08)", title="Avg Days"),
            height=350,
            margin=dict(l=10, r=10, t=50, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

# ═══════════════════════════════════════════
# TAB 3 — FEATURE IMPORTANCE
# ═══════════════════════════════════════════
with tab3:

    st.markdown('<div class="section-header">⚡ Model Feature Importance</div>', unsafe_allow_html=True)

    importance = model.feature_importances_
    feature_df = pd.DataFrame({
        "Feature": columns,
        "Importance": importance
    }).sort_values(by="Importance", ascending=False).head(10)

    fi_col1, fi_col2 = st.columns([1, 1.6], gap="large")

    with fi_col1:
        st.markdown("**📋 Importance Scores**")
        st.dataframe(
            feature_df.style
            .background_gradient(subset=["Importance"], cmap="Blues")
            .format({"Importance": "{:.4f}"}),
            use_container_width=True,
            hide_index=True
        )

        st.markdown("<br>", unsafe_allow_html=True)
        key_insights = [
            ("📞", "Customer Service Calls = strongest churn signal"),
            ("🛒", "Cart abandonment = checkout friction indicator"),
            ("🔐", "Login engagement = platform health signal"),
        ]
        for icon, text in key_insights:
            st.markdown(f"""
            <div class="insight-box">
                <span style="font-size:1.1rem;">{icon}</span>
                <span>{text}</span>
            </div>""", unsafe_allow_html=True)

    with fi_col2:
        colors = [
            f"rgba(99,102,241,{0.95 - i*0.07})" for i in range(len(feature_df))
        ]
        fig = go.Figure(data=[
            go.Bar(
                x=feature_df["Importance"],
                y=feature_df["Feature"],
                orientation='h',
                marker=dict(
                    color=colors,
                    line=dict(color="rgba(165,180,252,0.4)", width=1)
                ),
                text=[f"{v:.4f}" for v in feature_df["Importance"]],
                textposition="outside",
                textfont=dict(color="#a5b4fc", size=11, family="JetBrains Mono"),
            )
        ])
        fig.update_layout(
            title=dict(text="Top 10 Features by Importance", font=dict(color="#a5b4fc", size=15, family="Outfit"), x=0.03),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(15,22,41,0.5)",
            font=dict(color="#94a3b8", family="Outfit"),
            xaxis=dict(gridcolor="rgba(99,102,241,0.1)", title="Importance Score"),
            yaxis=dict(gridcolor="rgba(99,102,241,0.08)", autorange="reversed"),
            height=430,
            margin=dict(l=10, r=80, t=50, b=10),
        )
        st.plotly_chart(fig, use_container_width=True)

# ─────────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="footer-text">
    🔮 ChurnIQ &nbsp;·&nbsp; Built by <span>Kuldeep Patidar</span> &nbsp;·&nbsp; Data Analyst Project &nbsp;·&nbsp; Powered by Random Forest
</div>
""", unsafe_allow_html=True)