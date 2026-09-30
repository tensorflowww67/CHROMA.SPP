import streamlit as st
import random

st.set_page_config(page_title="CHROMA Decision Support System", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&display=swap');

    /* Mismong ibinigay mong link ng larawan ang gagamitin bilang background na may light green gradient */
    .stApp {
        background: linear-gradient(rgba(16, 122, 79, 0.55), rgba(5, 77, 47, 0.75)), 
                    url('https://scontent.fmnl8-5.fna.fbcdn.net/v/t39.30808-6/470201821_1331740421596243_8563550805935973368_n.jpg?stp=dst-jpg_tt6&cstp=mx1124x1400&ctp=s1124x1400&_nc_cat=103&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=833d8c&_nc_ohc=bxFEs5suFEgQ7kNvwF0mxKh&_nc_oc=Adq1En6wqpTnYp42kfoJGLqAYh5M4vmzaiBZJJOkxSKNBGXx71j1FxlRYMzCGCmKbXc&_nc_zt=23&_nc_ht=scontent.fmnl8-5.fna&_nc_gid=ShC8TlO5BRlAfaFyaqduSw&_nc_ss=7b289&oh=00_AQOwEHNEySv663BfIG74qrrCHkw9piel2TnLDQH1vRVpZg&oe=6AC2891E');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Control Panel sidebar na may tamang berdeng kulay */
    section[data-testid="stSidebar"] {
        background-color: rgba(14, 90, 58, 0.90) !important;
        border-right: 1px solid rgba(110, 231, 183, 0.3);
    }
    section[data-testid="stSidebar"] .stMarkdown, section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] span {
        color: #ffffff !important;
        font-family: 'Orbitron', sans-serif;
    }

    /* Estilo ng slider track para maging kulay pula */
    .stSlider [data-baseweb="slider"] div[role="slider"] {
        background-color: #ef4444 !important;
    }

    /* Header box sa itaas na may tamang transparensya */
    .top-header {
        background: rgba(14, 90, 58, 0.82);
        border: 1px solid rgba(110, 231, 183, 0.4);
        padding: 2rem;
        border-radius: 16px;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(4px);
    }

    /* Glassmorphism cards para sa analytics */
    .glass-card {
        background: rgba(14, 90, 58, 0.82);
        border: 1px solid rgba(110, 231, 183, 0.4);
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(4px);
        margin-bottom: 1rem;
    }

    .futuristic-font {
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 1px;
    }

    /* Estilo ng Button */
    .stButton>button {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        color: white;
        border-radius: 8px;
        font-weight: 700;
        width: 100%;
        border: none;
        padding: 0.75rem 1rem;
        font-family: 'Orbitron', sans-serif;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #047857 0%, #065f46 100%);
    }

    h1, h2, h3, h4, p, span, label {
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. TOP HEADER SECTION
st.markdown("""
    <div class="top-header">
        <h1 class="futuristic-font" style="margin: 0; font-size: 2.2rem; font-weight: 900;">CHROMA: DECISION SUPPORT SYSTEM PLAN</h1>
        <p class="futuristic-font" style="font-size: 1rem; margin-top: 0.4rem; opacity: 0.9;">
            Advanced Heavy-Metal Remediation Analytics for the Obando-Marilao-Meycauayan River System using Chaetomorpha Biomass
        </p>
    </div>
""", unsafe_allow_html=True)

# 2. SIDEBAR CONTROL PANEL
st.sidebar.markdown("<h2 class='futuristic-font' style='font-size: 1.4rem;'>CONTROL PANEL</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='font-size: 0.9rem; opacity: 0.85;'>Choose a mode:</p>", unsafe_allow_html=True)

mode = st.sidebar.radio("", ["Interactive Slider", "LGU Optimization Plan"])

st.sidebar.markdown("<hr style='border-color: rgba(255,255,255,0.2);'>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 class='futuristic-font' style='font-size: 1.2rem;'>CONDITIONS</h3>", unsafe_allow_html=True)

if mode == "Interactive Slider":
    ph = st.sidebar.slider("pH Level", 4.5, 8.0, 6.5, 0.1)
    temp = st.sidebar.slider("Water Temperature (°C)", 24.0, 32.0, 28.0, 0.5)
    soak_time = st.sidebar.slider("Soak Time", 20.0, 120.0, 60.0, 5.0)
    biomass_count = st.sidebar.slider("Chaetomorpha count (grams)", 5.0, 35.0, 15.0, 1.0)
    
    score = 85 - (ph - 6.5)**2 * 15 + (soak_time / 120) * 10 + (biomass_count / 35) * 10 - abs(temp - 28) * 0.5
    score = min(max(score, 50.0), 98.5)
    eco_index = (biomass_count * 1.2) + (soak_time * 0.1)

    # 3. MAIN DASHBOARD CONTENT
    col_left, col_right = st.columns([1.5, 1], gap="medium")

    with col_left:
        st.markdown("<h3 class='futuristic-font' style='font-size: 1.1rem; margin-bottom: 0.2rem;'>REAL-TIME PREDICTION ANALYTICS</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.85rem; opacity: 0.85; margin-bottom: 1rem;'>Modifying parameters on the control panel instantly updates the biosorption performance metrics</p>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="glass-card" style="text-align: center;">
                <h3 class="futuristic-font" style="font-size: 1.3rem; font-weight: 600; margin-bottom: 0.5rem;">Expected Heavy Metal Removal</h3>
                <h1 class="futuristic-font" style="font-size: 3.5rem; font-weight: 900; color: #34d399; margin: 0.5rem 0;">{score:.2f}%</h1>
                <p class="futuristic-font" style="font-size: 0.95rem; font-weight: 500; margin-top: 1rem; color: #6ee7b7;">Optimal Efficiency Range Active</p>
            </div>
        """, unsafe_allow_html=True)

    with col_right:
        st.markdown("<h3 class='futuristic-font' style='font-size: 1.1rem; margin-bottom: 0.2rem;'>SECONDARY ANALYSIS</h3>", unsafe_allow_html=True)
        st.markdown("<p style='font-size: 0.85rem; opacity: 0; margin-bottom: 1rem;'>&nbsp;</p>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="glass-card">
                <h3 class="futuristic-font" style="font-size: 1.2rem; font-weight: 600; margin-bottom: 0.5rem;">Eco-Sorption Index</h3>
                <h1 class="futuristic-font" style="font-size: 3rem; font-weight: 900; color: #34d399; margin: 0.5rem 0;">{eco_index:.1f} pts</h1>
                <p class="futuristic-font" style="font-size: 0.85rem; opacity: 0.9; margin-top: 1.5rem;">Resource viability score based on biomass load.</p>
            </div>
        """, unsafe_allow_html=True)

else:
    target_removal = st.sidebar.slider("Minimum Target Removal (%)", 50.0, 95.0, 85.0)
    
    st.markdown("<h3 class='futuristic-font'>LGU OPTIMIZATION PLAN</h3>", unsafe_allow_html=True)
    st.write("Execute computation to generate the optimal combination of treatment parameters matching municipal remediation requirements.")
    
    if st.button("Generate Optimal Treatment Plan"):
        best_score = 0
        best_params = None
        
        random.seed(42)
        for _ in range(2000):
            ph_s = random.uniform(4.5, 8.0)
            temp_s = random.uniform(24, 32)
            time_s = random.uniform(20, 120)
            bio_s = random.uniform(5, 35)
            
            sc = 85 - (ph_s - 6.5)**2 * 15 + (time_s / 120) * 10 + (bio_s / 35) * 10 - abs(temp_s - 28) * 0.5
            sc = min(max(sc, 50.0), 98.5)
            
            if sc >= target_removal and sc > best_score:
                best_score = sc
                best_params = (ph_s, temp_s, time_s, bio_s)
                
        if best_params:
            st.success("Optimal recommendation successfully generated for the municipality.")
            
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f"<div class='glass-card'><p style='margin:0;'>Optimal pH</p><h3 class='futuristic-font'>{best_params[0]:.2f}</h3></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div class='glass-card'><p style='margin:0;'>Temperature</p><h3 class='futuristic-font'>{best_params[1]:.1f} °C</h3></div>", unsafe_allow_html=True)
            with c3:
                st.markdown(f"<div class='glass-card'><p style='margin:0;'>Soak Time</p><h3 class='futuristic-font'>{best_params[2]:.1f} mins</h3></div>", unsafe_allow_html=True)
            with c4:
                st.markdown(f"<div class='glass-card'><p style='margin:0;'>Biomass Count</p><h3 class='futuristic-font'>{best_params[3]:.1f} g</h3></div>", unsafe_allow_html=True)
            
            st.markdown(f"""
                <div class="glass-card" style="margin-top: 1rem; border-left: 6px solid #34d399;">
                    <h4 style="margin-bottom: 0;">Predicted Removal Rate</h4>
                    <h1 class="futuristic-font" style="color: #34d399; font-size: 2.5rem; margin: 0.2rem 0;">{best_score:.2f}%</h1>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning("No matching parameter combination found for the specified target. Try lowering the target removal percentage.")