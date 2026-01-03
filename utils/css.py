import streamlit as st

def apply_css(total_cases, total_deaths):

    st.markdown("""
    <style>
    .kpi-container {
        display: flex;
        gap: 1rem;
    }

    .kpi-card {
        background-color: #faebeb;
        padding: 1.2rem;
        border-radius: 12px;
        width: 100%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    }

    .kpi-title {
        font-size: 1.3rem;
        font-weight: 450;
        color: #495c56;
        margin-bottom: 0.3rem;
    }

    .kpi-value {
        font-size: 1.8rem;
        font-weight: 600;
        color: #111;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="kpi-container">
        <div class="kpi-card">
            <div class="kpi-title">Total Active Cases</div>
            <div class="kpi-value">{total_cases}</div>
        </div>
        <div class="kpi-card">
            <div class="kpi-title">Total Deaths</div>
            <div class="kpi-value">{total_deaths}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
