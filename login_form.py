import streamlit as st

# ─── Page Configuration ─────────────────────────────────────────────
st.set_page_config(
    page_title="Student Registration",
    page_icon="🎓",
    layout="centered"
)

# ─── Custom CSS Styling ─────────────────────────────────────────────
st.markdown("""
<style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        min-height: 100vh;
    }

    /* Main Card Container */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 40px 36px;
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        max-width: 520px;
        margin: 30px auto;
    }

    /* Header Title */
    .logo-section {
        text-align: center;
        margin-bottom: 8px;
    }
    .logo-icon {
        font-size: 48px;
        display: block;
        margin-bottom: 6px;
    }
    .logo-title {
        font-family: 'Segoe UI', sans-serif;
        font-size: 26px;
        font-weight: 700;
        color: #ffffff;
        margin: 0;
        letter-spacing: 0.5px;
    }
    .logo-subtitle {
        font-size: 13px;
        color: rgba(255,255,255,0.45);
        margin-top: 4px;
        font-weight: 400;
    }

    /* Section Labels */
    .section-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.8px;
        color: #e94560;
        margin-top: 28px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .section-label .line {
        flex: 1;
        height: 1px;
        background: rgba(233, 69, 96, 0.25);
    }

    /* Streamlit Input Overrides */
    .stTextInput label, .stTextarea label,
    .stSelectbox label, .stMultiselect label,
    .stFileUploader label, .stSlider label,
    .stNumberInput label {
        color: rgba(255, 255, 255, 0.75) !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;
    }
    .stTextInput input,
    .stNumberInput input {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        padding: 12px 16px !important;
        font-size: 14px !important;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus {
        border-color: #e94560 !important;
        box-shadow: 0 0 0 3px rgba(233, 69, 96, 0.2) !important;
        outline: none !important;
    }
    .stTextarea textarea {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-size: 14px !important;
        transition: border-color 0.3s ease;
    }
    .stTextarea textarea:focus {
        border-color: #e94560 !important;
        box-shadow: 0 0 0 3px rgba(233, 69, 96, 0.2) !important;
    }
    .stSelectbox div[data-baseid] {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }
    .stMultiselect div[data-baseid] {
        background: rgba(255, 255, 255, 0.07) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }

    /* Checkbox */
    .stCheckbox label {
        color: rgba(255, 255, 255, 0.75) !important;
        font-size: 14px !important;
    }

    /* Radio */
    .stRadio label {
        color: rgba(255, 255, 255, 0.75) !important;
        font-size: 14px !important;
    }
    .stRadio div[role="radiogroup"] label {
        color: rgba(255, 255, 255, 0.6) !important;
    }

    /* Slider */
    .stSlider .stSlider div[data-testid="stSliderSliderRange"] {
        background: #e94560 !important;
    }

    /* Buttons */
    .stButton button {
        background: linear-gradient(135deg, #e94560, #c62a47) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 32px !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        letter-spacing: 0.8px;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        width: 100%;
    }
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4) !important;
    }
    .stButton button:active {
        transform: translateY(0px);
    }

    /* Form Submit Button */
    .stFormSubmitButton button {
        background: linear-gradient(135deg, #e94560, #c62a47) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 14px 32px !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        width: 100%;
        cursor: pointer;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stFormSubmitButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4) !important;
    }

    /* File Uploader */
    .stFileUploader {
        border: 2px dashed rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
        padding: 16px !important;
        background: rgba(255,255,255,0.04) !important;
    }
    .stFileUploader span {
        color: rgba(255,255,255,0.6) !important;
    }

    /* Divider */
    .stDivider hr {
        border-color: rgba(255,255,255,0.12) !important;
    }

    /* Messages */
    .stSuccess {
        background: rgba(38, 166, 91, 0.15) !important;
        border: 1px solid rgba(38, 166, 91, 0.35) !important;
        border-radius: 10px !important;
        color: #5fcf8f !important;
    }
    .stWarning {
        background: rgba(255, 171, 0, 0.12) !important;
        border: 1px solid rgba(255, 171, 0, 0.3) !important;
        border-radius: 10px !important;
        color: #ffcc44 !important;
    }
    .stError {
        background: rgba(233, 69, 96, 0.15) !important;
        border: 1px solid rgba(233, 69, 96, 0.35) !important;
        border-radius: 10px !important;
        color: #f08090 !important;
    }
    .stInfo {
        background: rgba(30, 144, 255, 0.12) !important;
        border: 1px solid rgba(30, 144, 255, 0.3) !important;
        border-radius: 10px !important;
        color: #6db8ff !important;
    }

    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #12122a, #1a1a2e) !important;
        border-right: 1px solid rgba(255,255,255,0.08) !important;
    }
    .stSidebar .stSelectbox label,
    .stSidebar .stSidebar h3 {
        color: rgba(255,255,255,0.8) !important;
    }

    /* Table */
    .stDataFrame, table {
        border-radius: 12px !important;
        overflow: hidden;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }
    .stDataFrame th, table th {
        background: rgba(233, 69, 96, 0.2) !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        border-bottom: 1px solid rgba(255,255,255,0.12) !important;
    }
    .stDataFrame td, table td {
        color: rgba(255,255,255,0.7) !important;
        border-bottom: 1px solid rgba(255,255,255,0.06) !important;
        background: rgba(255,255,255,0.03) !important;
    }

    /* Column Headers */
    .col-header {
        text-align: center;
        padding: 18px 10px;
        background: rgba(255,255,255,0.06);
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    .col-header .col-icon { font-size: 24px; }
    .col-header h4 {
        color: #fff;
        margin: 8px 0 4px;
        font-size: 15px;
    }
    .col-header p {
        color: rgba(255,255,255,0.45);
        font-size: 12px;
        margin: 0;
    }

    /* Container Box */
    .custom-container {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 14px;
        padding: 20px 24px;
        margin-top: 12px;
    }
    .custom-container p {
        color: rgba(255,255,255,0.6);
        font-size: 14px;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────────────
st.sidebar.markdown("### 📚 Navigation")
option = st.sidebar.selectbox(
    "Choose Page",
    ["🏠 Home", "📝 Register", "🔐 Login", "📋 Records"]
)
st.sidebar.divider()
st.sidebar.info(f"📍 You are on: **{option}**")


# ─── Logo / Header ───────────────────────────────────────────────────
st.markdown("""
<div class="main-card">
  <div class="logo-section">
      <span class="logo-icon">🎓</span>
      <h1 class="logo-title">Anurag University</h1>
      <p class="logo-subtitle">Student Records Management System</p>
  </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# ─── Welcome Banner ──────────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(135deg, rgba(233,69,96,0.15), rgba(15,52,96,0.4));
    border: 1px solid rgba(233,69,96,0.25);
    border-radius: 14px;
    padding: 18px 22px;
    text-align: center;
    margin-bottom: 10px;
">
    <p style="color:#fff; font-size:18px; font-weight:700; margin:0;">👋 Welcome, Student!</p>
    <p style="color:rgba(255,255,255,0.5); font-size:13px; margin-top:4px;">Fill in your details below to get started</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ─── Section: Personal Information ──────────────────────────────────
st.markdown('<div class="section-label">👤 Personal Information <span class="line"></span></div>', unsafe_allow_html=True)

name = st.text_input("Full Name", placeholder="e.g. Harshith Gadwala")

if name == "":
    st.warning("⚠️  Name field cannot be empty.")
elif not name.replace(" ", "").isalpha():
    st.error("❌ Please enter only alphabets — no numbers or symbols.")
else:
    st.success(f"✅ Hello, {name}!")

age = st.slider("📅 Select Your Age", min_value=15, max_value=65, value=20)
st.info(f"🎂 You are **{age}** years old.")

gender = st.radio("⚧️  Select Your Gender", ["👨 Male", "👩 Female", "🧑 Other"])
st.caption(f"Selected: {gender}")

st.divider()

# ─── Section: Academic Details ───────────────────────────────────────
st.markdown('<div class="section-label">📚 Academic Details <span class="line"></span></div>', unsafe_allow_html=True)

country = st.selectbox("🌍 Select Your Country", ("🇮🇳 India", "🇦🇪 UAE (Dubai)", "🇺🇸 USA", "🇬🇧 UK", "🇦🇺 Australia"))
st.caption(f"Country: {country}")

skills = st.multiselect(
    "💻 Select Your Skills",
    ["🐍 Python", "🗄️ SQL", "🤖 Machine Learning", "📊 Data Science", "🌐 Web Development", "☁️ Cloud Computing"]
)
if skills:
    st.success(f"🎯 Great picks: {', '.join(skills)}")

st.divider()

# ─── Section: About You ─────────────────────────────────────────────
st.markdown('<div class="section-label">💬 About You <span class="line"></span></div>', unsafe_allow_html=True)

feedback = st.text_area("📝 Tell us about yourself", placeholder="Write a short bio or any additional info...", height=110)

st.divider()

# ─── Section: Documents ──────────────────────────────────────────────
st.markdown('<div class="section-label">📄 Documents <span class="line"></span></div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader("📎 Upload Your ID / Document", type=["pdf", "png", "jpg", "jpeg"])
if uploaded_file is not None:
    st.success("✅ Document uploaded successfully!")
else:
    st.caption("No file uploaded yet. Supported: PDF, PNG, JPG")

st.divider()

# ─── Section: Agreement ──────────────────────────────────────────────
st.markdown('<div class="section-label">✅ Agreement <span class="line"></span></div>', unsafe_allow_html=True)

agree = st.checkbox("📜 I agree to the Terms & Conditions and Privacy Policy")
if agree:
    st.success("👍 Thank you for agreeing to the terms.")

st.divider()

# ─── Registration Form ───────────────────────────────────────────────
st.markdown('<div class="section-label">📋 Registration <span class="line"></span></div>', unsafe_allow_html=True)

with st.form("registration_form"):
    st.markdown("##### 📝 Create Your Account")
    reg_first = st.text_input("First Name", placeholder="e.g. Harshith")
    reg_last  = st.text_input("Last Name",  placeholder="e.g. Gadwala")
    reg_email = st.text_input("Email Address", placeholder="you@email.com")
    reg_pwd   = st.text_input("Create Password", type="password", placeholder="Min 6 characters")
    reg_pwd2  = st.text_input("Confirm Password", type="password", placeholder="Re-enter your password")

    register_btn = st.form_submit_button("🚀 Register Now")

    if register_btn:
        if not reg_first or not reg_last or not reg_email or not reg_pwd:
            st.error("❌ All fields are required.")
        elif reg_pwd != reg_pwd2:
            st.error("❌ Passwords do not match.")
        elif len(reg_pwd) < 6:
            st.warning("⚠️  Password must be at least 6 characters.")
        else:
            st.success(f"🎉 Registration successful! Welcome, {reg_first} {reg_last}!")
            st.balloons()

st.divider()

# ─── Login Form ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">🔐 Login <span class="line"></span></div>', unsafe_allow_html=True)

with st.form("login_form"):
    st.markdown("##### 🔑 Sign In to Your Account")
    login_user = st.text_input("📧 Email Address", placeholder="you@email.com")
    login_pwd  = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
    login_btn  = st.form_submit_button("🔐 Log In")

    if login_btn:
        if not login_user or not login_pwd:
            st.error("❌ Please fill in all login fields.")
        else:
            st.success(f"✅ Logged in successfully as {login_user}!")

st.divider()

# ─── Info Columns ────────────────────────────────────────────────────
st.markdown('<div class="section-label">ℹ️  Quick Info <span class="line"></span></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="col-header">
        <span class="col-icon">🏫</span>
        <h4>Campus</h4>
        <p>Main Campus, Hyderabad</p>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="col-header">
        <span class="col-icon">📞</span>
        <h4>Support</h4>
        <p>24/7 Help Desk</p>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="col-header">
        <span class="col-icon">📬</span>
        <h4>Email</h4>
        <p>info@anurag.edu</p>
    </div>""", unsafe_allow_html=True)

st.divider()

# ─── Student Records Table ───────────────────────────────────────────
st.markdown('<div class="section-label">📊 Student Records <span class="line"></span></div>', unsafe_allow_html=True)

records = {
    '👤 Name':   ['Ravi Kumar', 'Harshith Gadwala', 'Rohit Mehta'],
    '🎂 Age':    [21, 20, 20],
    '📚 Course': ['M.Tech', 'B.Tech', 'BBA'],
    '📧 Email':  ['ravi@anurag.edu', 'harshith@anurag.edu', 'rohit@anurag.edu']
}
st.table(records)

# ─── Footer ───────────────────────────────────────────────────────────
st.markdown("""
<div style="
    text-align:center;
    margin-top:30px;
    padding:18px;
    border-top:1px solid rgba(255,255,255,0.08);
">
    <p style="color:rgba(255,255,255,0.3); font-size:12px; margin:0;">
        © 2025 Anurag University · Student Records Management System · All Rights Reserved
    </p>
    <p style="color:rgba(255,255,255,0.2); font-size:11px; margin-top:4px;">
        🔒 Your data is secure and encrypted
    </p>
</div>
""", unsafe_allow_html=True)